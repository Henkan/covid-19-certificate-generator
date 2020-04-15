# covid-19-certificate-generator

## Introduction
Simple script permettant de générer une attestation de sortie en utilisant [le site du gouvernement](https://media.interieur.gouv.fr/deplacement-covid-19/). 

## Pré-requis
- Python 3
    - Pas testé sous Python 2
- Selenium
- Un driver Chrome - https://sites.google.com/a/chromium.org/chromedriver/downloads

## Installation
Cloner le répertoire
```
git clone https://github.com/Henkan/covid-19-certificate-generator.git
```

Installer Selenium
```
pip3 install -U selenium
```

## Utilisation
Il faut d'abord adapter le script pour remplir les informations suivantes:
- Le chemin du driver Chrome
- Le dossier de destination de l'attestation téléchargée
- Vos informations personnelles utilisées dans l'attestation

Toutes ces informations sont à remplir au début du fichier.
Une fois cela fait, il suffit de l'exécuter.
