from fastapi import FastAPI
from app.core.config import settings
from app.routers.todos import router as todos_router

app = FastAPI()
app.include_router(todos_router, prefix=settings.API_PREFIX)


@app.get("/health")
def health_check():
    return {"status": "ok"}
