from fastapi import FastAPI
from utils.database import init_db
from Admin.api import router as AdminAPI
from Books.api import router as BooksAPI
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

init_db()

app.include_router(AdminAPI)
app.include_router(BooksAPI)

PORT = int(os.getenv("PORT", 14565))

if __name__ == "__main__":  # <-- Fixed the typo here
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT, reload=True)
