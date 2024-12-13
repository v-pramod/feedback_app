from fastapi import FastAPI, HTTPException
from models import FeedbackRequest, FeedbackResponse
import google.generativeai as genai
from config import GEMINI_API_KEY
import csv
import os
from datetime import datetime

app = FastAPI(title="Feedback Collection API")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash-exp")

# Define the CSV file path
CSV_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "feedback_responses.csv"
)


def ensure_csv_exists():
    """Create CSV file with headers if it doesn't exist"""
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                [
                    "Timestamp",
                    "Username",
                    "Question",
                    "Rating",
                    "Sentiment Score",
                    "Gemini Response",
                ]
            )


def analyze_feedback(question: str, rating: int) -> tuple[int, str]:
    """
    Analyze feedback using Gemini API and return sentiment score and response
    """
    prompt = (
        f"Analyze this feedback - Question: {question}, Rating: {rating}/5. "
        f"Provide a brief response and determine a sentiment score from 1-5 where 5 is most positive."
    )

    try:
        response = model.generate_content(prompt)
        # For simplicity, we're using the same rating as sentiment score
        # In a real application, you'd want to parse Gemini's response to get the actual sentiment
        return rating, response.text
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error analyzing feedback: {str(e)}"
        )


@app.post("/api/v1/submitfeedback", response_model=FeedbackResponse)
async def submit_feedback(request: FeedbackRequest) -> FeedbackResponse:
    """
    Submit feedback and get AI-powered analysis
    """
    # Ensure CSV file exists
    ensure_csv_exists()

    # Process each feedback item
    for item in request.feedback:
        sentiment_score, gemini_response = analyze_feedback(item.question, item.rating)
        item.geminiResponse = [
            {"sentimentAnalysisScore": sentiment_score, "response": gemini_response}
        ]

        # Write feedback response to CSV
        try:
            with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                writer.writerow(
                    [
                        timestamp,
                        request.userName,
                        item.question,
                        item.rating,
                        sentiment_score,
                        gemini_response,
                    ]
                )
        except Exception as e:
            print(f"Error writing to CSV: {str(e)}")
            # Continue processing even if CSV writing fails

    return request


@app.get("/api/v1/getfeedbackresponse")
async def get_feedback_response():
    """
    Endpoint to retrieve feedback responses
    Note: In a real application, this would typically interact with a database
    """
    return {
        "message": "This endpoint would return stored feedback responses from a database"
    }
