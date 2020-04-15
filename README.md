# covid-19-certificate-generator

## Introduction
Simple script permettant de générer une attestation de sortie en utilisant [le site du gouvernement](https://media.interieur.gouv.fr/deplacement-covid-19/). 

## Pré-requis
- Python 3.6
    - Les autres versions n'ont pas été testées
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
Il faut d'abord adapter le script avec vos informations (au début du fichier). \
Une fois cela fait, il suffit de l'exécuter.