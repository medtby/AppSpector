from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from flask import request
import time
import os

site_url = request.args.get('site_url')

# Options headless du navigateur
options = webdriver.ChromeOptions()
options.add_argument("headless")

# Initialiser le driver Chrome
driver = webdriver.Chrome(options=options)

# Pages à capturer
pages = [site_url]

# Dossier pour les captures d'écran
screenshot_folder = "vinted_screens"
if not os.path.exists(screenshot_folder):
    os.makedirs(screenshot_folder)

# Boucle de capture des pages 
for url in pages:

    # Ouvrir l'URL
    driver.get(url)
    
    # Attendre la page chargée
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    
    # Nom de fichier unique
    file_name = f"{screenshot_folder}/{url.split('/')[-1]}-{time.strftime('%Y%m%d-%H%M%S')}.png"
    
    # Capture d'écran
    driver.save_screenshot(file_name)

    # Afficher le nom du fichier 
    print(f"Capture '{url}' sauvegardée dans {file_name}")
    
# Fermeture
driver.quit()