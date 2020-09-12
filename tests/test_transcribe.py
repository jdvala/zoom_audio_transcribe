import os
from pathlib import Path
from unittest.mock import Mock, patch

from zoom_audio_transcribe.convert import _convert_from_m4a_to_wav
from zoom_audio_transcribe.transcribe import transcribe

ASSETS = Path(__file__).parent / "assets"


def test_convert():
    _convert_from_m4a_to_wav(os.path.join(ASSETS))
    assert os.path.exists(os.path.join(ASSETS, "assets.wav")) is True

    # clean up, remove assets.wav
    os.remove(os.path.join(ASSETS, "assets.wav"))


@patch("zoom_audio_transcribe.transcribe._download_model", Mock(return_value=True))
def test_transcribe():
    test_asset = os.path.join(ASSETS, "test.wav")
    text = transcribe(test_asset)
    assert text == "what zero zero zero one two zero one eight zero"
