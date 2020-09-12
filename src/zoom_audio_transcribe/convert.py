import logging
import os
from pathlib import Path

from pydub import AudioSegment

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def _convert_from_m4a_to_wav(path: str) -> None:
    """Convert the m4a file to wav format.

    Args:
        path: Path of the file to be converted.
    """
    if not os.path.exists(path):
        raise ValueError("Path not found: {}".format(path))

    file_name = os.path.split(path.rstrip("/"))[-1]
    audio_only = Path(path) / "audio_only.m4a"

    if not audio_only.exists:
        raise ValueError("No audio file found for {}".format(audio_only))

    audio_recording = AudioSegment.from_file(audio_only, format="m4a")
    logging.info(
        "Audio file {} loaded. Starting the conversion process to wav".format(file_name)
    )

    audio_recording.export("{}/{}.wav".format(path, file_name), format("wav"))

    logging.info("Conversion complete. File saved at {}/{}.wav".format(path, file_name))
