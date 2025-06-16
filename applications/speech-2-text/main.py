""" """
import uvicorn
import whisper
from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import RedirectResponse
from src.data_model import S2TModel
from src.data_controller import Speech2Text, callbacks


app = FastAPI()

model = whisper.load_model("base.en").to("cuda:0")

@app.get("/")
async def landing():
    """ """
    return RedirectResponse(url="/docs")

@app.post("/inference")
def predict(payload:S2TModel, background_tasks: BackgroundTasks):
    """ """
    # logic
    infer = Speech2Text(audio_path=payload.audio_path)
    result: dict = infer(model=model)
    background_tasks.add_task(callbacks, "background processing started")
    return {"text": result.get("text","")}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

