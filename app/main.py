from fastapi import FastAPI
from app.models import PlanRequest, PlanResponse
from app.agent import generate_itinerary

app = FastAPI()

@app.post("/plan", response_model=PlanResponse)
def plan_trip(req: PlanRequest):
    return generate_itinerary(req.destination, req.vibe)
