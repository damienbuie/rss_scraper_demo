"""
Agent-based content analyzer using OpenAI Agents framework
"""
import asyncio
from agents import Agent, Runner
from typing import List, Dict, Optional
from config import AREAS_OF_INTEREST, AGENT_CONFIG
import re

class NewsAnalyzer:
    def __init__(self):
        self.areas_of_interest = AREAS_OF_INTEREST
        self.config = AGENT_CONFIG
        self.agent = self._create_agent()
    
    def _create_agent(self) -> Agent:
        """Create the news analysis agent"""
        areas_list = "\n".join([f"- {area}" for area in self.areas_of_interest])
        
        instructions = f"""
        You are a news article analyzer. Your task is to:
        1. Analyze news articles for relevance to specific areas of interest
        2. Determine if an article is relevant to any of these areas:
        
        {areas_list}
        
        3. Assign a relevance score from 0.0 to 1.0 where:
           - 1.0 = Highly relevant, directly discusses one or more areas
           - 0.7-0.9 = Moderately relevant, significant implications
           - 0.5-0.6 = Somewhat relevant, tangential connection
           - 0.0-0.4 = Not relevant
        
        4. Identify which specific areas of interest the article relates to
        
        Be thorough but efficient. An article is relevant if it:
        - Directly discusses one or more areas of interest
        - Has significant implications for these areas
        - Reports on developments, research, or news related to these topics
        
        Always provide your analysis in this exact format:
        RELEVANCE_SCORE: [0.0-1.0]
        AREAS: [comma-separated list of areas or "none"]
        SUMMARY: [brief 1-2 sentence explanation of relevance]
        """
        
        return Agent(
            name="NewsAnalyzer",
            instructions=instructions,
            model=self.config.get("model", "gpt-4o-mini"),
        )
    
    async def analyze_article(
        self,
        title: str,
        content: str,
        url: str
    ) -> Dict[str, any]:
        """
        Analyze a single article for relevance
        
        Returns:
            {
                "relevant": bool,
                "relevance_score": float,
                "areas_of_interest": List[str],
                "summary": str
            }
        """
        # Truncate content if too long (to save tokens)
        max_length = self.config.get("max_content_length", 5000)
        truncated_content = content[:max_length] if len(content) > max_length else content
        
        prompt = f"""
        Analyze this news article for relevance to the areas of interest:
        
        Title: {title}
        URL: {url}
        Content: {truncated_content}
        
        Please provide your analysis in the required format:
        RELEVANCE_SCORE: [0.0-1.0]
        AREAS: [comma-separated list or "none"]
        SUMMARY: [brief explanation]
        """
        
        try:
            result = await Runner.run(self.agent, input=prompt)
            analysis = self._parse_analysis(result.final_output)
            return analysis
        except Exception as e:
            print(f"Error analyzing article {url}: {str(e)}")
            return {
                "relevant": False,
                "relevance_score": 0.0,
                "areas_of_interest": [],
                "summary": f"Analysis error: {str(e)}"
            }
    
    def _parse_analysis(self, analysis_text: str) -> Dict:
        """Parse the agent's analysis output"""
        relevance_score = 0.0
        areas = []
        summary = ""
        
        lines = analysis_text.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith('RELEVANCE_SCORE:'):
                try:
                    score_text = line.split(':', 1)[1].strip()
                    # Extract first float number
                    score_match = re.search(r'\b(0\.\d+|1\.0)\b', score_text)
                    if score_match:
                        relevance_score = float(score_match.group(1))
                except (ValueError, AttributeError):
                    pass
            elif line.startswith('AREAS:'):
                areas_text = line.split(':', 1)[1].strip().lower()
                if areas_text != "none" and areas_text:
                    # Split by comma and clean up
                    areas = [area.strip() for area in areas_text.split(',')]
                    # Filter to only include valid areas of interest
                    valid_areas = []
                    for area in areas:
                        # Check if it matches any of our areas of interest
                        for interest in self.areas_of_interest:
                            if interest.lower() in area or area in interest.lower():
                                valid_areas.append(interest)
                                break
                    areas = list(set(valid_areas))  # Remove duplicates
            elif line.startswith('SUMMARY:'):
                summary = line.split(':', 1)[1].strip()
        
        # If parsing failed, try to extract score from text
        if relevance_score == 0.0:
            # Look for number between 0 and 1
            scores = re.findall(r'\b(0\.\d+|1\.0)\b', analysis_text)
            if scores:
                relevance_score = float(scores[0])
        
        # Default summary if not found
        if not summary:
            summary = analysis_text[:200] if analysis_text else "No summary available"
        
        # Determine relevance based on threshold
        threshold = self.config.get("relevance_threshold", 0.5)
        
        return {
            "relevant": relevance_score >= threshold,
            "relevance_score": relevance_score,
            "areas_of_interest": areas,
            "summary": summary
        }
    
    async def analyze_batch(self, articles: List[Dict], rate_limit: float = 0.5) -> List[Dict]:
        """Analyze multiple articles with rate limiting"""
        analyzed_articles = []
        
        for i, article in enumerate(articles):
            if i > 0:
                await asyncio.sleep(rate_limit)  # Rate limit API calls
            
            analysis = await self.analyze_article(
                title=article.get("title", ""),
                content=article.get("content", ""),
                url=article.get("url", "")
            )
            
            # Merge analysis with article data
            analyzed_article = {
                **article,
                **analysis
            }
            analyzed_articles.append(analyzed_article)
            
            # Print progress
            if (i + 1) % 10 == 0:
                print(f"Analyzed {i + 1}/{len(articles)} articles...")
        
        return analyzed_articles


