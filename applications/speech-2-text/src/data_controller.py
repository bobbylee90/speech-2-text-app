""" """
import whisper

class Speech2Text():
    def __init__(self, audio_path: str):
        """ """
        self.audio_path: str = audio_path

    def __call__(self, model:whisper):
        """ """
        result: dict = model.transcribe(self.audio_path)
        return result

def callbacks(*args, **kwargs):
    """ """