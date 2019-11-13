import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


GOOGLE_URL = 'https://www.google.cl/'


@given('La página de google está desplegada')
def step_impl(context):
    context.driver.get(GOOGLE_URL)


@when('Ingreso el texto a buscar "{phrase}"')
def step_impl(context, phrase):
    search_input = context.driver.find_element_by_xpath("//input[@title='Buscar']")
    search_input.send_keys(phrase + Keys.RETURN)


@then('Se muestran los resultados de "{phrase}"')
def step_impl(context, phrase):
    time.sleep(5)
    results_busqueda = context.driver.find_element_by_id("resultStats")
    print(results_busqueda.text)

