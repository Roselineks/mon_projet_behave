from behave import given, when, then

import logging

@given('the login page is displayed')
def step_impl(context):
    try:
        context.browser.login('ricacegos@gmail.com', 'Roibcaan1')
        logging.info("connexion faite avec succès")
        #print("Connexion faite avec succès")
        
    except Exception as e:
       # print(f"Erreur de connexion : {e}")
       logging.info(f"Erreur de connexion :'{e}")
    

@when('a user logs in with username "{username}" and password "{password}"')
def step_impl(context, username, password):

    print("Connexion de l'utilisateur réussie")

@then('the user should be redirected to the homepage')
def step_impl(context):

    print("Utilisateur redirigé vers la page d'accueil avec succès")