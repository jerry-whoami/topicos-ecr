from fastapi import FastAPI

app = FastAPI()

@app.get("/hello-app")
def hello_app():
    return {"message": "Hello, world!"}

