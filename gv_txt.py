import io
import os

from google.cloud import vision
from google.cloud.vision import types

# import your google credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="apikey.json"

vision_client = vision.ImageAnnotatorClient()

# put your image in the file_name blank
file_name = ''

with io.open(file_name, 'rb') as image_file:
    content = image_file.read()
    image = types.Image(content=content)

response = vision_client.text_detection(image=image)
texts = response.text_annotations
print('Texts:')

for text in texts:
    print('\n"{}"'.format(text.description))

    vertices = (['({},{})'.format(vertex.x, vertex.y)
                for vertex in text.bounding_poly.vertices])

    print('bounds: {}'.format(','.join(vertices)))