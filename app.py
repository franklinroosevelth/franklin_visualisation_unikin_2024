from flask import Flask, request, render_template, jsonify
from settings import *
import base64
from ultralytics import YOLO
import cv2
import numpy as np

app = Flask(__name__)


@app.route("/")
def form_upload():
    # detect_object()
    return render_template('upload_img.html') 

@app.route("/img_b64", methods=['POST'])
def img_b64():
    if request.method == 'POST':
        img_upload = request.files['file']
        img_b64 = detect_object(img_upload.read())
        
        return jsonify({"img_b64": img_b64}), 200, {'Content-Type': 'application/json; charset=utf-8'}
    return jsonify({"error": "Method not allowed"}), 405

def detect_object(image_file):
    image = cv2.imdecode(np.frombuffer(image_file, np.uint8), cv2.IMREAD_COLOR)
    
    # Charger le modèle YOLOv8 pré-entraîné
    model = YOLO('yolov8n.pt')

    # Charger une image à partir d'un fichier
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Effectuer la détection d'objets sur l'image
    results = model(image_rgb)

    # Vous pouvez aussi afficher l'image avec matplotlib
    annotated_image = results[0].plot()  # Affiche la première image avec les résultats

    # Convertir l'image en format PNG et l'encoder en base64
    _, buffer = cv2.imencode('.png', annotated_image)
    image_b64 = base64.b64encode(buffer).decode('utf-8')

    return image_b64


if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)
