import warnings
warnings.filterwarnings("ignore", message=r"Passing", category=FutureWarning)

from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.applications.vgg16 import decode_predictions
import numpy as np

model = VGG16(weights='imagenet', include_top=True)

def identify_frames(img_path):    
  img = image.load_img(img_path, color_mode='rgb', target_size=(224, 224))
  x = image.img_to_array(img)
  x = np.expand_dims(x, axis=0)
  x = preprocess_input(x)
  features = model.predict(x)
  return features

