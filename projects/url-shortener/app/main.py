from fastapi import FastAPI
from app.routes.urls import router

app = FastAPI()

app.include_router(router)


@app.get("/")
def root():
    return {"message": "URL Shortener API"}