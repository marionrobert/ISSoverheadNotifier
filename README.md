# Suivi de la Station Spatiale Internationale (ISS)

## Présentation
Ce projet vise à suivre la Station Spatiale Internationale (ISS) et à envoyer une notification lorsqu'elle passe au-dessus d'une localisation géographique spécifique. Il utilise les données de l'API Open Notify et de l'API Sunrise-Sunset pour déterminer la position de l'ISS et s'il fait nuit à l'endroit spécifié.

## Fonctionnement
1. Suivi de la Position de l'ISS : Le script récupère périodiquement la position actuelle de l'ISS en utilisant l'API Open Notify. Il compare la latitude et la longitude de l'ISS avec des coordonnées prédéfinies pour déterminer si elle est au-dessus de la tête.

2. Vérification de la Nuit : Il récupère également les heures de lever et de coucher du soleil pour l'emplacement spécifié à l'aide de l'API Sunrise-Sunset. En comparant l'heure actuelle avec les heures de lever et de coucher du soleil, le script détermine s'il fait nuit à l'emplacement.

3. Notification : Si l'ISS est au-dessus de la tête et qu'il fait nuit, le script envoie une notification par courriel pour alerter l'utilisateur.


## Exécution du Script
- Exécutez le script iss_tracker.py.
- Le script s'exécute en continu (toutes les 60 secondes), vérifiant la position de l'ISS et les conditions nocturnes.
Si l'ISS est au-dessus de la tête et qu'il fait nuit, une notification par courriel sera envoyée.

## Installation et Configuration
- Python : Version 3.9.6
- Bibliothèques Python : requests, datetime, smtplib, time
- Coordonnées : Remplacez MY_LAT et MY_LONG par la latitude et la longitude de votre emplacement.
- Paramètres de Courriel : Fournissez votre adresse courriel Gmail (MY_EMAIL) et votre mot de passe (MY_PASSWORD) pour activer les notifications par courriel.

## Remarques
Ce projet a été réalisé dans le cadre du cours [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/) de Angela Yu sur la plateforme Udemy.
