from fastapi import FastAPI
from utils.database import init_db
from Admin.api import router as AdminAPI
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Initialize the database
init_db()

# Include the Admin API router
app.include_router(AdminAPI)

# Get the port from environment variables, defaulting to 14565
PORT = int(os.getenv("PORT", 14565))

if __name__ == "__main__":  # <-- Fixed the typo here
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT, reload=True)
