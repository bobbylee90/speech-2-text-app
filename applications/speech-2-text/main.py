import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import whisper

app = FastAPI()

model = whisper.load_model("base.en").to("cuda:0")
# result = model.transcribe("/home/chunwei/Downloads/data/english/eng.mp3")
# print(result)
# print(result.get("text"))

@app.get("/")
async def landing():
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

