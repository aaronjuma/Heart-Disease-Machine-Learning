import tensorflow as tf

class Model:
    def __init__(self):
        self.model = tf.keras.models.load_model('modeler')

    def predict(self, dict):
        input_dict = {name: tf.convert_to_tensor([value]) for name, value in dict.items()}
        predictions = self.model.predict(input_dict)
        value = predictions[0][0]
        return round(value*100, 2)

