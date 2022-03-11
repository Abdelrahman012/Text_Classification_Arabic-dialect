from pyexpat import model
from keras.models import model_from_json
import pickle
from tensorflow.keras.models import load_model

class Model(object) :
    
    
    def __init__(self) :
        self.loaded_model = pickle.load(open("E:\\AIM_APP\\Any additional files\\Models\\mlnb.sav", 'rb'))

    def get_model(self):
        return self.loaded_model
