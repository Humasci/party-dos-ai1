import json

def search_activities(city, vibe):
    with open("data/vendor_data.json") as f:
        vendors = json.load(f)

    return [
        v for v in vendors
        if v["city"].lower() == city.lower()
        and vibe.lower() in v["vibe"].lower()
    ][:3]
