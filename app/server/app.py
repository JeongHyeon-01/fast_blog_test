from fastapi import FastAPI

app = FastAPI()

@app.get("/", tags=["Root"])
async def read_root() -> dict :
    return {"message": "Welcome top your beanie powerd app"}