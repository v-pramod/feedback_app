Feedback Collection Form
Use Case: Build a feedback form for a product, collecting user input and storing it.
Create a python fast api application, That exposes 2 endpoints "/api/v1/submitfeedback" and "/api/v1/getfeedbackresponse"

when "/api/v1/submitfeedback" is hit, handle below JSON request:
{
"userName": "Name",
"feedback" : [
{
"question": "question 1",
"rating": 3
},
{
"question": "question 2",
"rating": 3
},
{
"question": "question 3",
"rating": 3
}
]
}

Refer, @existingAPI.py on how to call gemini api and get back the response in below format
{
"userName": "Name",
"feedback" : [
{
"question": "question 1",
"rating": 3,
"geminiResponse" : [
{
"sentimentAnalysisScore": 3,
"response":"reponse from gemini"
}
]
},
{
"question": "question 2",
"rating": 3,
"geminiResponse" : [
{
"sentimentAnalysisScore": 3,
"response":"reponse from gemini"
}
]
},
{
"question": "question 3",
"rating": 3,
"geminiResponse" : [
{
"sentimentAnalysisScore": 3,
"response":"reponse from gemini"
}
]
}
]
}

create a csv file named feedback.csv with the headers as below:
username, question, rating, geminiSentimentScore, geminiResponse
store the response in this file

when "/api/v1/getfeedbackresponse" is hit, respond back with the data stored in feedback.csv file in form of JSON
