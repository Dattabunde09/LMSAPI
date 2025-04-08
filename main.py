# from fastapi import FastAPI
# from utils.database import init_db
# from Admin.api import router as AdminAPI
# from Books.api import router as BooksAPI
# import os
# from dotenv import load_dotenv

# load_dotenv()

# app = FastAPI()

# init_db()

# app.include_router(AdminAPI)
# app.include_router(BooksAPI)

# PORT = int(os.getenv("PORT", 14565))

# if __name__ == "__main__":  # <-- Fixed the typo here
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=PORT, reload=True)


# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from utils.database import init_db
# from Admin.api import router as AdminAPI
# from Books.api import router as BooksAPI
# import os
# from dotenv import load_dotenv

# load_dotenv()

# app = FastAPI()

# # Initialize database
# init_db()

# # Allow CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allow all origins for now (for development)
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Include your routers
# app.include_router(AdminAPI)
# app.include_router(BooksAPI)

# PORT = int(os.getenv("PORT", 14565))

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=PORT, reload=True)



#========================================================

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils.database import init_db
from Admin.api import router as AdminAPI
from Books.api import router as BooksAPI
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Create FastAPI app
app = FastAPI()

# Initialize the database
init_db()

# CORS setup: Allow frontend URL only
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",  # Allow your local frontend
        "http://localhost:5500"   # (Optional) VS Code Live Server sometimes uses this
    ],
    allow_credentials=True,
    allow_methods=["*"],         # Allow all methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],         # Allow all headers (e.g., Content-Type)
)

# Include routers
app.include_router(AdminAPI)
app.include_router(BooksAPI)

# Define port from .env or use default
PORT = int(os.getenv("PORT", 14565))

# Run with Uvicorn when using `python main.py`
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT, reload=True)
