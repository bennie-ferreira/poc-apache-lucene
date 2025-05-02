from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def heathcheck():
    return {"status": "OK"}
