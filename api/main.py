from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List
from datetime import datetime
import uvicorn
import os

app = FastAPI(title="VIP Party Bouncer API")

# Helper used to protect against path differences in Vercel vs Local
# We now store HTML in api/templates to ensure they are bundled with the function
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(CURRENT_DIR, "templates")

# CORS Configuration - Allow all origins for TV and Phone
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory leaderboard storage
leaderboard_storage: List[dict] = []

class ScoreSubmission(BaseModel):
    player_name: str
    email: str
    score: int
    timestamp: str = None

class LeaderboardEntry(BaseModel):
    player_name: str
    email: str
    score: int
    timestamp: str
    rank: int

@app.get("/")
async def read_root():
    """Serve the mobile game interface"""
    return FileResponse(os.path.join(TEMPLATES_DIR, "index.html"))

@app.get("/leaderboard-view")
async def read_leaderboard_view():
    """Serve the TV leaderboard display"""
    return FileResponse(os.path.join(TEMPLATES_DIR, "leaderboard.html"))

@app.post("/api/score")
async def submit_score(submission: ScoreSubmission):
    """Submit a new score to the leaderboard"""
    if not submission.player_name or len(submission.player_name.strip()) == 0:
        raise HTTPException(status_code=400, detail="Player name is required")
    
    if submission.score < 0:
        raise HTTPException(status_code=400, detail="Score must be non-negative")
    
    # Add timestamp if not provided
    if not submission.timestamp:
        submission.timestamp = datetime.now().isoformat()
    
    # Create leaderboard entry
    entry = {
        "player_name": submission.player_name.strip(),
        "email": submission.email.strip(),
        "score": submission.score,
        "timestamp": submission.timestamp
    }
    
    # Add to storage and sort by score (descending)
    leaderboard_storage.append(entry)
    leaderboard_storage.sort(key=lambda x: x["score"], reverse=True)
    
    # Keep only top 50 entries
    if len(leaderboard_storage) > 50:
        leaderboard_storage[:] = leaderboard_storage[:50]
    
    return {"message": "Score submitted successfully", "entry": entry}

@app.get("/api/leaderboard", response_model=List[LeaderboardEntry])
async def get_leaderboard(limit: int = 10):
    """Get the top scores from the leaderboard"""
    if limit < 1 or limit > 50:
        raise HTTPException(status_code=400, detail="Limit must be between 1 and 50")
    
    # Add ranks to the entries
    ranked_entries = [
        {
            **entry,
            "rank": idx + 1
        }
        for idx, entry in enumerate(leaderboard_storage[:limit])
    ]
    
    return ranked_entries
@app.get("/api/hello")
async def say_hello():
    """Simple hello endpoint to test API"""
    return {"message": "Hello from VIP Party Bouncer API!"}

@app.delete("/api/leaderboard/reset")
async def reset_leaderboard():
    """Reset the leaderboard (admin function)"""
    leaderboard_storage.clear()
    return {"message": "Leaderboard reset successfully"}

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "total_scores": len(leaderboard_storage)
    }

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
