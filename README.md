# 🪐 Orbit

Orbit is the centralized entry point for all my personal services and platforms. 
It acts as a dynamic hub that displays currently active platforms (like MTrack, MyInves, etc.), allowing easy access through a clean and simple interface.

## 🎯 Project Purpose

As the number of deployed services grows, remembering various links and subdomains can become difficult. Orbit solves this problem by providing a dashboard where services "self-register" and are continuously monitored.

## 🏗️ Architecture

The project is divided into two lightweight but powerful components:

- **Frontend (Vue.js):** A minimal Single Page Application (SPA) that displays a grid of cards. Clicking on a card redirects you to the corresponding service. The design is managed using a custom preset (`orbit-ecosystem-preset.js`).
- **Backend (Python + FastAPI):** A lightweight server that handles:
  - An API to expose the list of active platforms to the frontend.
  - A registration API (Service Discovery) so that applications can autonomously subscribe to Orbit.
  - A scheduled *Healthcheck* system (running every hour) to verify the status of registered services, keeping the dashboard up to date.

## 🚀 Workflow

1. **Registration:** When a new service is deployed, it makes a call to the Orbit backend to register itself, sending its name, URL, and a brief description.
2. **Monitoring:** Orbit performs an hourly health check on all registered services to ensure they are still reachable.
3. **Display:** The frontend fetches data from the backend and dynamically generates the UI, showing only the services that are currently operational.

## 🛠️ Technologies Used

- **Frontend:** Vue.js
- **Backend:** Python 3, FastAPI, Uvicorn