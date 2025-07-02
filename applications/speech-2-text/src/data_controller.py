""" """
import whisper
import requests

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

class LlmRefiner():
    def __init__(self):
        self.ollma_k8s_url: str = "http://ollama.ollama-ns.svc.cluster.local/api/generate" # http://<service-name>.<namespace>.svc.cluster.local

    def pretiffy(self, text: str):
        """ """

