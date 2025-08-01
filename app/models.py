from pydantic import BaseModel

class PlanRequest(BaseModel):
    destination: str
    vibe: str

class Activity(BaseModel):
    name: str
    type: str
    link: str

class PlanResponse(BaseModel):
    itinerary: str
    activities: list[Activity]
