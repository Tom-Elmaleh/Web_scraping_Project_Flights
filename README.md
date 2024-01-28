# Web_scraping_Project_Flights

Ce repository GitHub contient l'ensemble des fichiers nécessaires à la réalisation du projet de Web Scraping, réalisé en 5e annéee. Le but de notre projet est de comparer les voyages en train et en avion au sein même de l'Italie pour les mêmes destinations.

Le repository est séparé en plusieurs dossiers qui font chacun référence à une étape de notre projet.

### Trenitalia_Scraping 

Ce dossier contient l'ensemble des fichiers associés au scraping du site Trenitalia (trains) : 

* Scraping_Trenitalia_VF.ipynb : Ce notebook contient le code utilisé pour scraper le site Trenitalia avec Selenium et Beautiful soup.
* trenitalia_data.csv : Ce fichier contient l'ensemble des données qui ont été scrapées sur le site Trenitalia à travers l'exécution du code de scraping.

### Ryanair_Scraping

Ce dossier contient l'ensemble des fichiers associés au scraping du site Ryanair (avions). Les fichiers les plus importants contenus dans ce dossier sont : 

* Webscrapping_rendu_v2.py : Ce fichier contient le code utilisé pour scraper le site Ryanair avec Selenium.
* Ryanair_Italy_Flight_Data_full.csv : Ce fichier contient l'ensemble des données qui ont été scrapées sur le site Ryanair à travers l'exécution du code de scraping.

### Data_Merge

Ce dossier contient l'ensemble des fichiers dédiées à l'étape de fusion des données scapées afin de réunir les données récupérées sur Ryanair et Trenitalia sur le même fichier csv. Les fichiers les plus importants contenus dans ce dossier sont : 

* Data_merge.ipynb : Ce notebook contient le code utilisé pour fusionner les données de Ryanair et Trenitalia.
* common_travels_data.csv : Ce fichier contient l'ensemble des données fusionnées (issues de Ryanair et de Trenitalia).

### Data_Analysis

Ce dossier contient l'ensemble des fichiers dédiées à l'étape d'analyse des données fusionnées. Le notebook Data_merge.ipynb est le plus important dans ce dossier. Il contient du code générant des visualisations à partir des données. 

Enfin, une application web a été développée pour ce projet à l'aide de la librairie streamlit.

L'application est accessible sur le lien suivant : https://web-scraping-project-flights-app-pmwout.streamlit.app/

Les fichiers principaux associés à cette application sont : 

* app.py : Ce fichier permet de constituer l'application streamlit dans son intégralité.
* requirements.txt : Ce fichier permet de définir les différentes versions des librairies utilisées sur le streamlit afin d'éviter des erreurs de dépendance et d'assurer la stabilité de l'application.
