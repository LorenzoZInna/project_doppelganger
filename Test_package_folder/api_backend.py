from fastapi import FastAPI
from fastapi.responses import JSONResponse
from Test_package_folder.emotion_to_track_mvp import get_random_track_embed_code
from PIL import Image
from Test_package_folder.streamlit_app_frontend import main
from Test_package_folder.image_preprocessing import image_preprocessing, get_image
import pickle
from tensorflow.keras.models import load_model

app = FastAPI ()

@app.get("/")

def root():
    return{'greeting':"entered fastAPI ! Very nice :)"}

@app.post("/predict")

async def predict(img):
    img = img.file.read()
    ######################
    img = Image.open(BytesIO(img))
    print(img.size)

    img_pre_proc=image_preprocessing(img)
    print('success')
    model = load_model('models/happy_sad_mod.h5')
    res = model.predict(img_pre_proc)[0][0]
    res_type=type(res)
    print (f'RESULT IS {res}, with type {res_type}')

    if res > 0.5:
        emotion = 'happy'
        prob = str(1 - res)
    else:
        emotion ='sad'
        prob = str(res)
    print (f"Emotion is: {emotion}, with probability of: {prob}")
    return {"Emotion": emotion, "with probability of": prob}



@app.get("/return_song")
def return_song(emotion):


    link1=get_random_track_embed_code(emotion)
    return JSONResponse(content={"link to spotify": str(link1)})
