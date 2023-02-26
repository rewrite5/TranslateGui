import flet as ft
import requests
from dotenv import load_dotenv
import os

load_dotenv()
AUTHORIZATION = os.getenv('AUTHORIZATION')

def main(page):
    languages = {'Spanish': 'es_ES', 'English': 'en_US','Esperanto' : 'eo_WORLD', 'German' : 'de_DE', 'Italian' : 'it_IT', 'latin' : 'la_VAT', 'Russian' :'ru_RU'}


    def button_Translate(event):
        url = "https://api-b2b.backenster.com/b1/api/v3/translate"

        payload = {
            "translateMode": "html",
            "platform": "api",
            "from": languages[combo_box1.value],
            "to": languages[combo_box2.value],
            "data": text_field1.value
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": AUTHORIZATION
        }

        response = requests.post(url, json=payload, headers=headers, timeout=30)

        translations = response.json()
        text_field2.value = translations['result']
        page.update()
    def button_Clear(event):
        combo_box1.value = ''
        combo_box2.value = ''
        text_field1.value = ''
        text_field2.value = ''
        combo_box1.focus()

        page.update()

    combo_box1 = ft.Dropdown(label='Language',
                             width=200,
                             options=[
                                 ft.dropdown.Option('Spanish'),
                                 ft.dropdown.Option('English'),
                                 ft.dropdown.Option('Esperanto'),
                                 ft.dropdown.Option('German'),
                                 ft.dropdown.Option('Italian'),
                                 ft.dropdown.Option('Latin'),
                                 ft.dropdown.Option('Russian'),
                             ]
    )

    combo_box2 = ft.Dropdown(label='Language',
                             width=200,
                             options=[
                                 ft.dropdown.Option('Spanish'),
                                 ft.dropdown.Option('English'),
                                 ft.dropdown.Option('Esperanto'),
                                 ft.dropdown.Option('German'),
                                 ft.dropdown.Option('Italian'),
                                 ft.dropdown.Option('Latin'),
                                 ft.dropdown.Option('Russian'),
                             ]
    )
    texto = ft.Text(value='Translate',color='BLUE')
    texto2 = ft.Text(value='<--->', color='RED')
    text_field1 = ft.TextField(label='From',width=230)
    text_field2 = ft.TextField(label='To', width=230)

    translate = ft.ElevatedButton(text='translate', on_click=button_Translate)
    clear = ft.ElevatedButton(text='Clear', on_click=button_Clear)

    filas = ft.Row(controls=[
        combo_box1,texto2,combo_box2
    ])
    filas_botons = ft.Row(controls=[
        translate, clear
    ])

    filas_text_fields = ft.Row(controls=[
        text_field1, text_field2
    ])

    page.add(texto,filas,filas_text_fields,filas_botons)

ft.app(target=main)
