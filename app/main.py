from fastapi import FastAPI
from app.routers import openai_router
app = FastAPI()

app.include_router(openai_router)

@app.get("/health")
async def root():
    return {
        "status": "healthy"
    }


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
