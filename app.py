# imports
from flask import Flask, request, render_template, flash
from selenium import webdriver
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

app = Flask(__name__)

# Options Chrome headless
options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument("no-sandbox") 

# Dossier captures
screenshot_folder = "captures"
os.makedirs(screenshot_folder, exist_ok=True)

# Fonction de capture 
def take_screenshot(url):

  print(f"Prendre capture d'écran de {url}")

  driver = webdriver.Chrome(options=options)
  driver.get(url)

  # Attendre chargement 
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

  # Nom de fichier 
  file_name = f"{screenshot_folder}/{url.split('/')[-1]}-{time.strftime('%Y%m%d-%H%M%S')}.png"

  print(f"Enregistrement dans {file_name}")
  driver.save_screenshot(file_name)

  driver.quit()

  return file_name

@app.route('/', methods=['GET','POST'])
def index():

  if request.method == 'POST':

    url = request.form['url']
    if url:
      try:
        file = take_screenshot(url) 
        flash(f"Capture enregistrée dans {file}")
      except:
        flash("Échec de la capture d'écran")

  return render_template('index.html')

if __name__ == "__main__":
    app.secret_key = 'ma_clé_secrete_haha'
    app.run(debug=True)