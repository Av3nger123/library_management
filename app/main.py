from fastapi import FastAPI
from app.routes.api import router
app = FastAPI()



@app.get("/health")
async def health():
    return "OK"

app.include_router(router)