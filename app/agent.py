import os
import google.generativeai as genai
from dotenv import load_dotenv
from app.tools.search_activities import search_activities

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

def build_prompt(city, vibe, activity_results):
    activity_text = "\n".join(
        f"- {a['name']} ({a['type']}): {a['link']}" for a in activity_results
    )

    return f"""
You're Party Dos, a cheeky AI party planner.

Destination: {city}
Vibe: {vibe}

Here are 3 possible activities:
{activity_text}

Write a fun, day-by-day itinerary including these activities and extras.
"""

def generate_itinerary(city, vibe):
    activities = search_activities(city, vibe)
    prompt = build_prompt(city, vibe, activities)

    response = model.generate_content(prompt)
    return {
        "itinerary": response.text,
        "activities": activities
    }
