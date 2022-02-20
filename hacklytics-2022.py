# export GOOGLE_APPLICATION_CREDENTIALS=kyourcredentials.json
import io
import cv2
import ctypes
import os
import stat
import sys
from PIL import Image

# Imports the Google Cloud client library
from google.cloud import vision
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'hackalytics-2022-edddba28c1d0.json'


# Instantiates a client
client = vision.ImageAnnotatorClient()

def detectFaces(image: bytes)->list:
    """Detects faces in an image. 
    Takes in a bytes object representing an image.
    Returns a list of tuples containing two corners 
    defining the bounding box of each image.
    """
    outList = []
    response = client.face_detection(image=image)
    faces = response.face_annotations

    for face in faces:
        vertices = ([(vertex.x, vertex.y) for vertex in face.bounding_poly.vertices])
        outList.append((vertices[1], vertices[3]))
    return outList


cap = cv2.VideoCapture(0)
fps = 30
frameInterval = int(1000 / 30)


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    imageStream = vision.Image(content=cv2.imencode('.png', frame)[1].tobytes())

    # print OCR text
    bBoxCoords = detectFaces(imageStream)

    for bBox in bBoxCoords:
        topRight = bBox[0]
        bottomLeft = bBox[1]
        x, y = bottomLeft[0], topRight[1]
        w, h = topRight[0] - bottomLeft[0], bottomLeft[1] - topRight[1]

        # Grab bounding box with Numpy slicing and blur
        blurRect = frame[y:y+h, x:x+w]
        blur = cv2.GaussianBlur(blurRect, (101,101), 0) 
        # Insert ROI back into image
        frame[y:y+h, x:x+w] = blur
        imageStream1 = vision.Image(content=cv2.imencode('.png', frame)[1].tobytes())
        detectFaces(imageStream1)

    cv2.imshow('frame',frame)

    c = cv2.waitKey(frameInterval)
    #exit feed with escape key
    if c == 27:
        break



# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
