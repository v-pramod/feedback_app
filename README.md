# Feedback Collection API

A FastAPI application for collecting and analyzing user feedback using Google's Gemini AI.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Add your Gemini API key to the `.env` file

3. Run the application:
```bash
uvicorn main:app --reload
```

## API Endpoints

### POST /api/v1/submitfeedback
Submit user feedback for AI analysis.

Example request:
```json
{
  "userName": "Name",
  "feedback": [
    {
      "question": "question 1",
      "rating": 3
    }
  ]
}
```

### GET /api/v1/getfeedbackresponse
Retrieve feedback responses (to be implemented with database integration).
