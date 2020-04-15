#!/usr/bin/env python3

__author__ = "Sylvain Roncoroni"

from selenium import webdriver
from datetime import datetime
from time import sleep

# Adapt to the path for the chrome driver
chromedriver_location = "./chromedriver.exe"
# Adapt to the folder the files should be downloaded
download_location = "D:/Downloads"
attestation_url = r"https://media.interieur.gouv.fr/deplacement-covid-19/"

# Change for your own values
# Adapt booleans for the reason of going out
values = {
    "firstname": "Jean",
    "lastname": "Dupont",
    "birthday": "01/01/1970",
    "birthplace": "Lyon",
    "address": "999 avenue de France",
    "city": "Paris",
    "zipcode": "75001",
    "work": False,      # Work purposes
    "grocery": True,    # To buy food
    "health": False,    # To see a doctor
    "family": False,    # To help family
    "sport": False,     # To make sport or just walk for an hour
    "judicial": False,  # For judicial reason
    "mission": False    # Required general interest missions
}


def main():
    today = datetime.now()
    options = webdriver.ChromeOptions()
    options.add_argument("download.default_directory={0}".format(download_location))
    driver = webdriver.Chrome(chromedriver_location, options=options)

    driver.get(attestation_url)
    sleep(2) # Wait for everything to load
    # Click on reload button if it exists
    try:
        driver.find_element_by_id("reload-btn").click()
    except(Exception):
        pass

    # Fill personal information
    driver.find_element_by_id("field-firstname").send_keys(values["firstname"])
    driver.find_element_by_id("field-lastname").send_keys(values["lastname"])
    driver.find_element_by_id("field-birthday").send_keys(values["birthday"])
    driver.find_element_by_id("field-lieunaissance").send_keys(values["birthplace"])
    driver.find_element_by_id("field-address").send_keys(values["address"])
    driver.find_element_by_id("field-town").send_keys(values["city"])
    driver.find_element_by_id("field-zipcode").send_keys(values["zipcode"])

    # Select reason
    if values["work"]:
        driver.find_element_by_id("checkbox-travail").click()
    if values["grocery"]:
        driver.find_element_by_id("checkbox-courses").click()
    if values["health"]:
        driver.find_element_by_id("checkbox-sante").click()
    if values["family"]:
        driver.find_element_by_id("checkbox-famille").click()
    if values["sport"]:
        driver.find_element_by_id("checkbox-sport").click()
    if values["judicial"]:
        driver.find_element_by_id("checkbox-judiciaire").click()
    if values["mission"]:
        driver.find_element_by_id("checkbox-missions").click()

    # Fill day and time
    driver.find_element_by_id("field-datesortie").send_keys(today.strftime("%d/%m/%Y"))
    driver.find_element_by_id("field-heuresortie").send_keys(today.strftime("%H:%M"))

    # Generate
    driver.find_element_by_id("generate-btn").click()
    sleep(1)
    driver.close()


if __name__ == "__main__":
    main()
