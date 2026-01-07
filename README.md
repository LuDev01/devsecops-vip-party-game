# 🎭 VIP Party Bouncer Game

A DevSecOps-themed swipe game built with Vanilla JS and FastAPI. Protect the party from security threats by making quick decisions!

## 🎮 Game Features

- **Swipe Mechanics**: Swipe right to accept, left to reject, or let time run out (auto-fail)
- **Lives System**: 3 chances to make the right call
- **Real-time Timer**: 5 seconds per decision with visual countdown
- **DevSecOps Analogies**: Learn security concepts through gameplay
- **Live Leaderboard**: TV-ready cyberpunk dashboard with real-time updates

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the Server

```bash
python main.py
```

The server will start at `http://localhost:8000`

### 3. Play the Game

**Mobile/Phone (Game Interface):**
- Open `http://localhost:8000` in your browser
- Swipe right (✅) to accept safe guests
- Swipe left (❌) to reject dangerous threats
- Don't let the timer run out!

**TV Display (Leaderboard):**
- Open `http://localhost:8000/leaderboard-view` on a large screen
- Auto-updates every 2 seconds
- Shows top 10 players with cyberpunk aesthetics

## 🎯 Guest Types

### Safe Guests ✅
- 🍕 Pizza delivery for the devs
- 🔍 Inspector with a valid badge
- 📦 Package courier with ID
- 🎸 Band member on the list
- 👔 Manager with credentials

### Dangerous Threats ❌
- 🕵️ Sneaky person with a crowbar → **Unauthorized Access**
- 💣 Guy carrying a ticking bomb → **Critical Vulnerability**
- 🔪 Suspicious figure in a hoodie → **Malicious Actor**
- 💉 Stranger with injection kit → **SQL Injection**
- 🦠 Person spreading malware USB → **Malware Distribution**

## 🏗️ Architecture

### Frontend
- **index.html**: Mobile-optimized swipe game
  - CardManager class for card stack management
  - GameState object for lives/score/timer
  - Touch events for swipe detection
  - CSS animations for smooth transitions

- **leaderboard.html**: TV dashboard display
  - Cyberpunk/neon aesthetic
  - Auto-refresh every 2 seconds
  - Animated entries for new scores
  - Responsive grid layout

### Backend (FastAPI)
- **main.py**: REST API with CORS enabled
  - `POST /api/score` - Submit game scores
  - `GET /api/leaderboard` - Fetch top scores
  - In-memory storage (top 50 scores)
  - Health check endpoint

## 📡 API Endpoints

### Submit Score
```http
POST /api/score
Content-Type: application/json

{
  "player_name": "Alice",
  "score": 800,
  "timestamp": "2026-01-06T10:30:00"
}
```

### Get Leaderboard
```http
GET /api/leaderboard?limit=10
```

Response:
```json
[
  {
    "player_name": "Alice",
    "score": 800,
    "timestamp": "2026-01-06T10:30:00",
    "rank": 1
  }
]
```

## 🎨 Tech Stack

- **Frontend**: Vanilla JavaScript (ES6), CSS3 Animations
- **Backend**: FastAPI, Uvicorn
- **Storage**: In-memory Python list (sorted)
- **Styling**: CSS Grid, Flexbox, Custom Animations

## 🔧 Configuration

Edit `main.py` to customize:
- Port number (default: 8000)
- CORS settings
- Leaderboard size (default: top 50)

## 📱 Browser Support

- Modern browsers with ES6 support
- Touch events for mobile devices
- Responsive design for phones and tablets

## 🎯 Game Rules

1. **Accept (Swipe Right)**: Let safe guests into the party
2. **Reject (Swipe Left)**: Keep dangerous threats out
3. **Timer**: Make your decision within 5 seconds
4. **Lives**: You have 3 chances - lose all and it's game over!
5. **Scoring**: +100 points for each correct decision

## 🏆 Leaderboard Features

- Top 10 players displayed
- Real-time updates every 2 seconds
- Animated new entries
- Connection status indicator
- Gold/Silver/Bronze styling for top 3

## 📝 Notes

- The leaderboard resets when the server restarts
- For persistent storage, replace the in-memory list with a database
- Adjust timer duration in index.html (default: 5 seconds)

## 🎉 Have Fun!

Protect the party and climb the leaderboard! 🎭🔒
