#Importing the libraries
import numpy as np
import pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(ChromeDriverManager().install())

#Here is the features to scrap from ryanair website
df = pd.DataFrame(columns=['carrier','Flight_id','departure_airport','arrival_airport', 'date', 'take_off_time','landing_time','flight_time','price'])

#Initialization of the variables for the first flight to scrap
date_string = '2024-05-20'

#Attention: penser à installer la librarie 'openpyxl'.
airport_data=pd.read_excel('Airport_Data.xlsx')


# Créer une nouvelle instance du navigateur
#driver = webdriver.Chrome()

# Opening the webpage
driver.get("https://www.ryanair.com/fr/fr")

try:
    # Attendre que le bouton "Oui, j’accepte" soit chargé (cookies)
    button = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".cookie-popup-with-overlay__button-settings[data-ref='cookie.accept-all']"))
    )
    # Cliquer sur le bouton
    button.click()
except Exception as e:
    print(f"Une erreur s'est produite : {e}")


for i in range(airport_data.shape[0]):
        #nb_day=str(j)
        #date_string=f"2024-05-{nb_day}"
        #Here is the features to scrap from ryanair website
        #df = pd.DataFrame(columns=['carrier','Flight_id','departure_airport','arrival_airport', 'date', 'take_off_time','landing_time','flight_time','price'])
    df=pd.read_csv("Ryanair_Italy_Flight_Data.csv")

        #lancement du scrap pour chaque ligne

    airport_iata_departure=airport_data['Departure_IATA'][i]
    airport_arrival=airport_data['Destination_Airport'][i]

        #Pour ne pas faire planter le code si le scripte n'arrive pas à scrapper un vol en particulier
    try:
        try:
                # Aller sur le bouton "Aller simple"
            one_way_button = WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "ry-radio-button[data-ref='flight-search-trip-type__one-way-trip']"))
            )
                #Cliquer
            one_way_button.click()
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")
        try:
                #bouton aéroport de départ
            departure_input = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-button__departure"))
            )
            departure_input.click()
                # Cliquer sur l'élément "Italie"
            italy_element = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/ry-tooltip/div[2]/hp-app-controls-tooltips/fsw-controls-tooltips-container/fsw-controls-tooltips/fsw-origin-container/fsw-airports/fsw-countries/div[3]/div[8]/span"))
            )
            buttonIT=driver.find_element(By.XPATH, "/html/body/ry-tooltip/div[2]/hp-app-controls-tooltips/fsw-controls-tooltips-container/fsw-controls-tooltips/fsw-origin-container/fsw-airports/fsw-countries/div[3]/div[8]/span")
            buttonIT.click()
                # Cliquer sur l'élément "Rome (Tous les aéroports)"=>code IATA
            wait = WebDriverWait(driver, 5)
                #rome_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span[data-ref='airport-item__mac-name'][data-id='ROM']")))
            rome_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"span[data-ref='airport-item__mac-name'][data-id='{airport_iata_departure}']")))
                
                # Bouton Aéroport d'arrivée
            driver.execute_script("arguments[0].click();", rome_element)
            destination_input = WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-button__destination"))
            )
            import time
                #Netoyage de la cellule et on entre l'aéroport d'arrivée
                #destination_input.clear()
            destination_input.send_keys(airport_arrival)
            time.sleep(3)
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")
        try:
                # Aller sur le bouton recherche pour faire apparaitre les champs complementaires
            search_button = WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "button[data-ref='flight-search-widget__cta']"))
            )
            search_button.click()
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")

        try:
                # Aller sur le bouton date
            departure_date = WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "fsw-input-button[uniqueid='dates-from']"))
            )
                # Cliquer sur le bouton 
            departure_date.click()
                # selectionner moi de mais
            may_button = WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.m-toggle__month[data-id='mai']"))
            )
            may_button.click()
            WebDriverWait(driver, 10).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.toast__text"))
            )
                #slectionner le jour
                #Attention, Attendre s'il est ecrit erreur
            day_button = WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, f"div.calendar-body__cell[data-id='{date_string}']"))
            )
                
                # Faire défiler l'élément en vue
            ActionChains(driver).move_to_element(day_button).perform()

                # Cliquez sur le bouton
            day_button.click()
                #Selectionner le bouton valider le nombre de passager (pare defaut 1 passager)
            done_button = WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "button.passengers__confirm-button[aria-label='Fini']"))
            )
            done_button.click()
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")
        try:

                # Aller sur le bouton recherche
            search_button = WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "flight-search-widget__start-search-cta.ng-tns-c983940023-3.ry-button--gradient-yellow"))
            )
                # "#" A retirer pour lancer la recherche
            search_button.click()
        except Exception as e:
            print(Exception)
            print(f"Une erreur s'est produite : {e}")


        try:
                # Recupérer le tableau contenant tous les vols de la journée
            flight_list = WebDriverWait(driver, 2).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.flight-card__wrapper"))
            )

                # Parcourir la liste des éléments et récupérer l'ensemble des données de chaque élément

            for flight in flight_list:
                my_flight=[]
                    #recupérer les differentes donées du vol
                data = flight.text.split('\n')
                    #Mettre les données du vol dans une liste et le mettre en forme
                my_flight.append(data[0].replace('Opéré par ', ''))
                my_flight.append(data[3])
                my_flight.append(data[2])
                my_flight.append(data[6])
                my_flight.append(date_string)
                my_flight.append(data[1])
                my_flight.append(data[5])
                my_flight.append(data[4].replace(' h ', ':').replace(' m',''))
                my_flight.append(data[8].replace(' €', ''))
                    #print(my_flight)
                    #Ajouter la ligne au dataframe
                df.loc[len(df.index)] = my_flight
                    # A chaque scrappe on va exporter au fichier csv
                df.to_csv('Ryanair_Italy_Flight_Data.csv', index=False)
        except:
            print('Vol non enrregistré')
    except:
        print("Echec lors du scrap du vol "+airport_iata_departure+" - "+airport_arrival+" "+"date : "+date_string)

        #retour a la page principale
    try:
        button = driver.find_element(By.CLASS_NAME, 'ry-header__logo') 
        button.click()
    except:
        driver.get("https://www.ryanair.com/fr/fr")