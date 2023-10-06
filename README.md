# AppSpector

# Générateur de captures d'écran web

Ce script Python permet de générer des captures d'écran (screenshots) pour un site web donné.

## Utilisation

1. Installer les prérequis :

- Python 3
- Selenium 
- Un navigateur web (Chrome, Firefox)
- Le driver Selenium correspondant au navigateur (chromedriver, geckodriver)

2. Mettre le driver dans le PATH ou indiquer son chemin dans le code.

3. Lancer un serveur web local (par exemple avec la commande `python -m http.server`).

4. Ouvrir la page web appSpector.html et entrer l'URL du site à screener.

5. Cliquer sur le bouton "Générer captures d'écran".

6. Le script Python va s'exécuter et générer les screenshots du site dans le dossier `vinted_screens`.

## Fonctionnement

- appSpector.html permet de saisir l'URL à screener
- En soumettant le formulaire, l'URL est passée au script Python
- Le script Selenium ouvre le site web et génère des captures d'écran
- Les screenshots sont enregistrés dans un dossier avec un nom unique

## Personnalisation

- Modifier les pages à capturer dans le script Python
- Ajouter des actions et vérifications avec Selenium
- Personnaliser les dossiers et noms de fichier

Ce générateur de captures d'écran web permet de facilement screener un site de manière automatisée.
