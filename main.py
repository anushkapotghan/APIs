from fastapi import FastAPI
from router import router  # Import your API from router.py
import asyncio
from router import scan_files_for_warnings  # Import background task

app = FastAPI()

# Include all routes from router
app.include_router(router)

# Start background scan task
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(scan_files_for_warnings())
