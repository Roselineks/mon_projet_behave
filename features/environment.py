from selenium import webdriver
from browser_actions import Cdiscount

def before_all(context):
    print("Initialisation du WebDriver")
    context.browser = Cdiscount()
    print("WebDriver initialisé avec succès")

def before_feature(context, feature):
    print(f"Préparation de l'environnement pour la fonctionnalité : {feature.name}")

def before_scenario(context, scenario):
    print(f"Préparation de l'environnement pour le scénario : {scenario.name}")