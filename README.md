# zoom_audio_transcribe
![GH](https://github.com/jdvala/zoom-audio-transcribe/workflows/GH/badge.svg)
[![Code Coverage](https://codecov.io/gh/jdvala/zoom_audio_transcribe/branch/master/graph/badge.svg)](https://codecov.io/gh/jdvala/zoom_audio_transcribe)

Transcribe zoom meetings audio locally.

Transcribe zoom meetings audio locally, using ![vosk-api](https://github.com/alphacep/vosk-api).


## Install

Supported python version >=3.6. Supported OS, Linux. Support for Windows and OSX will come in second version.

```bash
pip install zoom_audio_transcribe
```


## Usage

```bash
$ zoom_audio_transcribe
```

![init](https://github.com/jdvala/zoom-audio-transcribe/blob/master/screenshots/init.png)

Once you are at the menu, select the appropiate meeting and let it run.

![Done](https://github.com/jdvala/zoom-audio-transcribe/blob/master/screenshots/done.png)

Once the transcription is done the, file will be saved in the same folder as the zoom meetings recording. For linux users its `/home/$USER/Documents/Zoom/{meeting_which_was_selected}
