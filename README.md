# 🌍 Geo-Aid

**Geo-Aid** is a real-time, location-based disaster awareness and community response platform designed to help people **prepare, respond, and act** during natural disasters.

It integrates **live updates, geolocation-based insights, precautionary guidance, and community participation** into a single, accessible web platform.

---

## 🚀 Features

- 📡 **Live Disaster Updates**  
  Fetches real-time disaster-related news using external APIs

- 🧭 **Location-Based Visualization**  
  Interactive maps using **OpenStreetMap + Leaflet** to view nearby resources and affected areas

- 📸 **Citizen Reporting (Prototype)**  
  Upload and view disaster-related images (demo implementation)

- 📘 **Disaster Awareness & Precautions**  
  Structured survival guides for floods, earthquakes, cyclones, etc.

- 🤝 **Volunteer System (Prototype)**  
  Users can register as volunteers (remote/on-site)

- 💰 **Donation Module (UI Prototype)**  
  Structured interface for contributing to relief efforts

- 🔐 **Authentication System**  
  Secure login/register system using **Flask sessions + hashed passwords**

---

## 🧠 Tech Stack

### Frontend
- HTML  
- CSS  
- JavaScript  

### Backend
- Flask (Python)  

### Database (Current)
- JSON-based storage (for authentication prototype)

### Planned Database
- MySQL (for scalability)

### APIs & Tools
- OpenStreetMap (Leaflet.js)  
- News API  
- Pandas & Matplotlib (data analysis - planned/partial)

---

## 🏗️ System Architecture

Geo-Aid follows a **3-layer architecture**:

1. **Client Layer (Frontend)**  
   Handles UI, maps, and user interaction

2. **Application Layer (Flask Backend)**  
   Manages authentication, routing, and API integration

3. **Data Layer**  
   - JSON (current lightweight storage)  
   - External APIs for real-time data  

---

## ⚡ How It Works

1. Users log in to the platform  
2. View **live disaster updates**  
3. Access **location-based resources via maps**  
4. Read **precautionary guidelines**  
5. Participate via **volunteering or donations**

---

## 🎯 Problem It Solves

- Fragmented disaster information  
- Spread of misinformation  
- Lack of localized guidance  
- Poor coordination between citizens and responders  

---

## 💡 Innovation

Geo-Aid combines:

- 📢 Awareness (real-time updates)  
- 📍 Localization (map-based insights)  
- 🤝 Action (community participation)  

➡️ Transforming disaster response into a **connected, community-driven system**

---

## 🌱 Future Scope

- 🤖 AI-based flood risk prediction  
- 📶 Offline support (PWA)  
- 🌐 Multi-language support  
- 🏛 NGO & Government integration  
- 📊 Real-time analytics and alert prioritization  

---

## 🛠️ Installation & Setup

```bash
git clone https://github.com/Viraj1849V/Geo-Aid.git
cd Geo-Aid
pip install -r requirements.txt
python app2.py

---

**## Deployment**

The project is deployed using Render (Flask + Gunicorn).

**## Limitations (Current)**

Uses prototype-level data in some modules
Limited real-time API integration
No full-scale database yet
Designed as MVP (Minimum Viable Product)

**## Authors**

Viraj Pathare
Ayush Chandwadkar
Aryan Patel
Heet Oswal
Dr. Sandhya Waghere
