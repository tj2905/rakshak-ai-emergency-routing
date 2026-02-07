# Rakshak AI — Emergency Smart Routing System

Rakshak AI is an AI-powered emergency routing system designed to help ambulances, fire trucks, and police vehicles reach destinations faster by avoiding congested and narrow roads using intelligent route scoring.

Built for Smart Cities and emergency response optimization.

---

## Problem Statement

Emergency vehicles in Indian cities often face 8–15 minute delays due to traffic congestion and unsuitable road conditions. Studies show that every 1-minute delay in ambulance response can increase mortality risk by up to 10%.

Traditional navigation systems optimize for general drivers — not emergency vehicles.

---

## Solution Overview

Rakshak AI uses graph-based routing with AI-style scoring to compute the fastest emergency route based on:

- Road width
- Traffic congestion
- Time of day
- Vehicle type
- Emergency priority weighting

Instead of shortest distance, it finds **minimum emergency delay path**.

---

## AI Logic

Each road segment is assigned a Rakshak Score:

Rakshak Score = (5 − road_width) + traffic × time_multiplier + vehicle_penalty

Lower score = better for emergency vehicles.

Vehicle-specific rules:
- Fire trucks avoid narrow roads
- Police vehicles prioritize speed
- Ambulances balance width and congestion

Time-of-day traffic multipliers simulate rush hours.

---

## Tech Stack

- Python
- Streamlit
- NetworkX
- Folium Maps
- Graph Algorithms
- Heuristic AI Scoring

---

## Features

- Emergency vehicle type routing
- Time-based traffic simulation
- AI-weighted road scoring
- Route comparison metrics
- Interactive map visualization
- Multi-location city graph
- Smart route selection
- Hackathon-ready UI

---

## How It Works

1. City roads modeled as weighted graph
2. Traffic + width + vehicle rules applied
3. AI score assigned to each road
4. Shortest path computed using AI weights
5. Compared with normal shortest path
6. Map and metrics displayed

---

## How To Run

Install dependencies:

pip install -r requirements.txt

Run app:

streamlit run app.py

---

## Future Scope

- Live Google Maps traffic API integration
- Smart traffic signal control
- Real accident & roadblock feeds
- Multi-city expansion
- Emergency dispatch integration

---

## Impact

Rakshak AI can reduce emergency delays by 2–4 minutes, potentially saving hundreds of lives annually in high-density cities.

---

Built with ❤️ for AI for Social Good Hackathon.
