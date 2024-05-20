from fastapi import FastAPI

app = FastAPI()

@app.get("/sayHello")
async def say_hello():
    return {"message": "Hello User."}
