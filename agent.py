import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GENAI_API_KEY")

# Load course database
with open("data/course.json", "r") as file:
    courses = json.load(file)


def get_course_recommendation(name, skills, goal):

    course_data = ""

    for course in courses:
        course_data += f"""
Course Name: {course['name']}
Category: {course['category']}
Description: {course['description']}
Skills: {", ".join(course['skills'])}
Level: {course['level']}
Prerequisites: {", ".join(course['prerequisites']) if course['prerequisites'] else "None"}

"""

    prompt = f"""
You are an intelligent AI Course Recommendation Agent.

Student Name:
{name}

Current Skills:
{skills}

Career Goal:
{goal}

Available Courses:
{course_data}

Analyze the student's profile.

Recommend ONLY the best 3 courses from the above list.

Return Markdown.

Include:


## Student

## Skill Analysis

## Recommended Courses

## Learning Roadmap

## Career Advice
"""

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:5000",
        "X-Title": "AI Course Recommendation Agent"
    }

    body = {
        "model": "openai/gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": "You are an AI Career Recommendation Agent."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=body
    )

    data = response.json()

    if response.status_code != 200:
        return f"Error: {data}"

    return data["choices"][0]["message"]["content"]