from fastapi import FastAPI
from package_folder.emotion_to_track_mvp import get_random_track_embed_code
from fastapi.responses import JSONResponse
from streamlit_app import main
import pickle

app = FastAPI ()

@app.get("/")

def root():
    return{'greeting':"gooodbye111"}
#comment
#process face from model -> emotion
#emotion_output = model result
#
#model must be running on API instead of streamlit! (lighter stuff)
#save model results as h5!
"""
@app.get("/get_emotion_model"):
def get_emotion_model():
"""


emotion='happy'

@app.get("/return_song")
def return_song(emotion):


    link1=get_random_track_embed_code(emotion)
    return JSONResponse(content={"link to spotify": str(link1)})
