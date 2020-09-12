import json
import logging
import os
import shutil
import wave
import zipfile
from pathlib import Path

import requests
from halo import Halo
from vosk import KaldiRecognizer, Model, SetLogLevel

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)
SetLogLevel(-1)

MODEL_PATH = os.path.join(Path(__file__).parent, "model")


@Halo(text="Downloading models.", text_color="green")
def _download_model() -> bool:
    """Downloads vosk model."""
    if os.path.exists(MODEL_PATH) and os.listdir(MODEL_PATH):
        logger.info("Model already exist.")
        return True
    logging.info("Model not found. Starting the download.")

    model = requests.get(
        "http://alphacephei.com/vosk/models/vosk-model-small-en-us-0.3.zip"
    )
    with open("/tmp/en-small.zip", "wb") as f:
        f.write(model.content)

    logger.info("File download complete, unzipping.")
    with zipfile.ZipFile("/tmp/en-small.zip", "r") as zip_ref:
        zip_ref.extractall("/tmp/")

    os.mkdir(MODEL_PATH)

    for file_name in os.listdir("/tmp/vosk-model-small-en-us-0.3/"):
        shutil.move(
            "/tmp/vosk-model-small-en-us-0.3/{}".format(file_name),
            "{}/{}".format(MODEL_PATH, file_name),
        )
    logger.info("Model download complete.")
    return True


@Halo(text="Transcribing", text_color="green")
def transcribe(path: str) -> str:
    """Transcribe."""
    # check if the models is already present
    if not _download_model():
        raise ValueError("Unable to automatically download the model.")
        exit(1)

    wf = wave.open(path, "rb")
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        logger.info("Audio file must be WAV format mono PCM.")
        exit(1)

    model = Model(MODEL_PATH)
    rec = KaldiRecognizer(model, wf.getframerate())

    while True:
        data = wf.readframes(wf.getnframes())
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            full_result = rec.Result()
            text = json.loads(full_result)["text"]
        else:
            partial_result = rec.PartialResult()
            text = json.loads(partial_result)["partial"]
    return text
