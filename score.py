import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.post("/predict")
def predict(data: dict):
    return {"prediction": "some result"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5001)
