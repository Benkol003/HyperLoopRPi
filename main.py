from fastapi import FastAPI

app = FastAPI()

##fill out to add data
@app.get("/")
async def root():
    return {"message: ": "Hello World"}

