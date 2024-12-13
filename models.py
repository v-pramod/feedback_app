from typing import List
from pydantic import BaseModel

class GeminiResponse(BaseModel):
    sentimentAnalysisScore: int
    response: str

class FeedbackItem(BaseModel):
    question: str
    rating: int
    geminiResponse: List[GeminiResponse] = []

class FeedbackRequest(BaseModel):
    userName: str
    feedback: List[FeedbackItem]

class FeedbackResponse(BaseModel):
    userName: str
    feedback: List[FeedbackItem]
