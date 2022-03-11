from keras.models import model_from_json

class Model(object) :
    
    
    def __init__(self) :

        self.json_file = open('E:\\AIM_APP\\Any additional files\\Models\\model.json', 'r')
        self.loaded_model_json =self.json_file.read()
        self.json_file.close()
        self.loaded_model = model_from_json(self.loaded_model_json)
        self.loaded_model.load_weights("E:\\AIM_APP\\Any additional files\\Models\\model.h5")
    def get_model(self):
        return self.loaded_model
