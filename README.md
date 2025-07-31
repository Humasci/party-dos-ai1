# 🥳 Party Dos AI – Group Party Planner Concierge

AI-powered group itinerary planner for stag dos, hen dos, birthdays, and other unforgettable party weekends.

Built on Google’s Travel Concierge Agent (ADK) with custom tools for nightlife, experiences, and group coordination.

---

## 🚀 Features

- 🧠 GPT-powered AI Concierge Agent
- 🗓️ Day-by-day itinerary builder with real vendors
- 🔍 Activity search via affiliate APIs (GetYourGuide, Tiqets, Booking, Expedia)
- 🗳️ Group voting (on activities, dates)
- 💬 Chat interface to refine plans with AI
- 💸 Stripe integration (optional phase 2)
- 🛍️ Connected Shopify store for party merch & downloads

---

## 💾 Project Structure

```plaintext
party-dos-ai/
├── frontend/        # React or Framer frontend
├── backend/         # FastAPI or Flask server
│   ├── agents/        # Fork of Google ADK Travel Concierge
│   ├── tools/         # Custom tools (search, poll, payments)
│   ├── rag/           # Vector DB setup for vendor search
├── data/            # Vendor seed data (CSV/JSON)
├── scripts/         # Scraping, embedding, import utilities
└── README.md
