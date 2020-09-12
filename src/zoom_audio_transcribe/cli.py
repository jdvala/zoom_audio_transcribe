from __future__ import print_function, unicode_literals

import os
from os.path import expanduser
from typing import Dict, List

from art import tprint
from PyInquirer import Separator, prompt

from zoom_audio_transcribe.convert import _convert_from_m4a_to_wav
from zoom_audio_transcribe.transcribe import transcribe

ZOOM_DIR = os.path.join(expanduser("~"), "Documents", "Zoom")


def _get_zoom_list_recordings_list() -> List[str]:
    """Get the list of all the recordings."""
    # The local path for zoom recording is ~/Documents/Zoom
    # Get the home directory
    file_list = os.listdir(ZOOM_DIR)
    files = []
    for f in file_list:
        files.append(f)
        files.append(Separator())
    return files


def user_response() -> Dict[str, str]:
    questions = [
        {
            "type": "list",
            "name": "zoom_recording",
            "choices": _get_zoom_list_recordings_list(),
            "message": "Which zoom recording do you want to convert?",
        }
    ]

    answers = prompt(questions)
    return answers


def main() -> None:
    """Main."""
    tprint("Zoom Audio Transcribe")
    user_res = user_response()
    folder_name = user_res["zoom_recording"]

    _convert_from_m4a_to_wav(os.path.join(ZOOM_DIR, folder_name))

    transcribed_text = transcribe(
        os.path.join(os.path.join(ZOOM_DIR, folder_name, f"{folder_name}.wav"))
    )

    with open(os.path.join(ZOOM_DIR, folder_name, f"{folder_name}.txt"), "w") as f:
        f.write(transcribed_text)


if __name__ == "__main__":
    main()
