# Projet de Détection d'Objets avec YOLO et Flask

Ce projet est une application web basée sur le framework Python Flask permettant de détecter des objets dans des images téléchargées par l'utilisateur à l'aide du modèle YOLO (You Only Look Once) avec OpenCV. Le frontend est gérer par jQuery.

## Fonctionnalités

- **Téléchargement d'image** : L'utilisateur va importer l'image depuis l'appareil ou en la glissant-déposant dans la zone de téléchargement.
- **Prévisualisation de l'image** : Une fois l'image téléchargée, elle est affichée pour prévisualisation avant la détection.
- **Détection d'objets** : En cliquant sur le bouton de détection, l'image est envoyée au serveur où YOLO est utilisé pour détecter les objets.
- **Affichage des résultats** : Les résultats de la détection sont renvoyés au client sous forme d'une image annotée montrant les objets détectés avec des boîtes de délimitation et des labels.

## Technologies Utilisées

- **Flask** : Framework web léger utilisé pour construire le serveur backend.
- **OpenCV** : Utilisé pour le traitement d'images et l'intégration du modèle YOLO.
- **YOLO** : Modèle de détection d'objets pré-entraîné utilisé pour identifier et localiser des objets dans les images.
- **jQuery** : Bibliothèque JavaScript utilisée pour faciliter la manipulation de l'interface utilisateur et les appels AJAX.
- **HTML/CSS** : Utilisés pour la structure et le style de la page web.

2. **Installer les dépendances** :
    ```bash
    pip install -r requirements.txt
    ```

3. **Lancer l'application** :
    ```bash
    python app.py
    ```

4. **Accéder à l'application** :
    - Ouvrez votre navigateur web et accédez à `http://localhost:3000/`.

## Structure du Projet

- **app.py** : Fichier principal contenant le serveur Flask et les routes API.
- **static/** : Contient les fichiers JavaScript et CSS.
    - **script.js** : Contient les fonctions JavaScript pour gérer le téléchargement d'images et les appels AJAX.
    - **style.css** : Contient les styles CSS pour l'interface utilisateur.
- **templates/** : Contient les fichiers HTML.
    - **index.html** : Page principale de l'application.

## Utilisation

1. **Télécharger une image** : Cliquez sur le bouton "Importer l'image" ou glissez-déposez une image dans la zone de téléchargement.
2. **Prévisualiser l'image** : Vérifiez l'image affichée pour s'assurer que c'est la bonne.
3. **Détecter les objets** : Cliquez sur le bouton "Détecter les objets" pour envoyer l'image au serveur et recevoir les résultats de la détection.
4. **Afficher les résultats** : L'image avec les objets détectés et annotés sera affichée sous la zone de téléchargement.