from django.shortcuts import render
from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key, Attr
import time
from datetime import datetime, timedelta
from django.conf import settings
from django.conf.urls.static import static

dynamodb = boto3.resource('dynamodb', region_name='us-east-1', aws_access_key_id='ASIAWB3I5CXJ5VHXGTC2', aws_secret_access_key= 'FqIjdC/AXzJOHVO0+YKNZW63iCviAGLwlZhPjMd9', aws_session_token='FwoGZXIvYXdzEJj//////////wEaDDp95WfdUYezEhnOhiLJAUP/GuCY7z2hZbFPpFtZtxml9NbkL5ypaHrZHmHZcyS5LVV7KD+rzj2h+wVN4wpZi00/sfYkLdFcq207PrR8eCV5/WtEZqbXE7ojzfLK2N4SE+S/NYNgt94ljQ/xB0lg0YhU/rY9mGQSafAihOvCkiF3ZmvBimXaKqQauvx0KuooX9XWDdO0GMJV4Z8kJFUXoXlopF8prXpVS9vjSd0KHpfnnU/13BYsqyf8jd7u5du/IhDzc3qSKjYAge3Lv7y/A1inP8O0dC85MSix1u3+BTItBRbjIwoe9SvNZjKLFtdzD7VYNTek4FWCjQxc/1pr6ZkFdf7DJBRofZS8bQGU')
table = dynamodb.Table('airquality_estacion_monitoreo')

numeros = ['2', '3', '4', '5', '6']

aqi_quintero = 0
r1_quintero = 0
r2_quintero = 0
color_quintero = ""

aqi_vina = 0
r1_vina = 0
r2_vina = 0
color_vina = ""

aqi_valdivia = 0
r1_valdivia = 0
r2_valdivia = 0
color_valdivia = ""

aqi_temuco = 0
r1_temuco = 0
r2_temuco = 0
color_temuco = ""

aqi_lascondes = 0
r1_lascondes = 0
r2_lascondes = 0
color_lascondes = ""

now = datetime.utcnow()
now_str = now.strftime('%Y-%m-%dT%H:%M:%SZ')

#now_menos_16min = now - timedelta(minutes=16)
now_menos_16min = now - timedelta(seconds=16)
now_menos_16min_str = now_menos_16min.strftime('%Y-%m-%dT%H:%M:%SZ')

#para guardar valores de las variables
for x in numeros:
    scan_kwargs = {
        'FilterExpression': Key('sensor_id').eq(x) & Key('timestamp').between(now_menos_16min_str, now_str),
        'ProjectionExpression': "informacion.payload.#dt.#crt.pollution.aqius",
        'ExpressionAttributeNames': {"#dt": "data", "#crt": "current"}
    }

    response = table.scan(**scan_kwargs)

    if x == '2' : #quintero
        texto = "La ciudad de Quintero tiene un Indice de Calidad de Aire (AQI) de "
        aqi_quintero = response['Items'][0]['informacion']['payload']['data']['current']['pollution']['aqius']
        r1_quintero = aqi_quintero * 2
        r2_quintero = aqi_quintero * 5
    if x == '3' : #viña del mar
        texto = "La ciudad de Viña del Mar tiene un Indice de Calidad de Aire (AQI) de "
        aqi_vina = response['Items'][0]['informacion']['payload']['data']['current']['pollution']['aqius']
        r1_vina = aqi_vina * 2
        r2_vina = aqi_vina * 5
    if x == '4' : #valdivia
        texto = "La ciudad de Valdivia tiene un Indice de Calidad de Aire (AQI) de "
        aqi_valdivia = response['Items'][0]['informacion']['payload']['data']['current']['pollution']['aqius']
        r1_valdivia = aqi_valdivia * 2
        r2_valdivia = aqi_valdivia * 5
    if x == '5' : #temuco
        texto = "La ciudad de Temuco tiene un Indice de Calidad de Aire (AQI) de "
        aqi_temuco = response['Items'][0]['informacion']['payload']['data']['current']['pollution']['aqius']
        r1_temuco = aqi_temuco * 2
        r2_temuco = aqi_temuco * 5
    if x == '6' : #las condes
        texto = "La comuna de Las Condes tiene un Indice de Calidad de Aire (AQI) de "
        aqi_lascondes = response['Items'][0]['informacion']['payload']['data']['current']['pollution']['aqius']
        r1_lascondes = aqi_lascondes * 2
        r2_lascondes = aqi_lascondes * 5

#para guardar el color correcto
for x in numeros:
    if x == '2' : #quintero
        if r1_quintero >= 0 and r1_quintero <= 50:
            color_quintero = "green"
        if r1_quintero >= 51 and r1_quintero <= 100:
            color_quintero = "yellow"
        if r1_quintero >= 101 and r1_quintero <= 150:
            color_quintero = "orange"
        if r1_quintero >= 151 and r1_quintero <= 200:
            color_quintero = "red"
        if r1_quintero >= 201 and r1_quintero <= 300:
            color_quintero = "purple"

    if x == '3' : #viña del mar
        if r1_vina >= 0 and r1_vina <= 50:
            color_vina = "green"
        if r1_vina >= 51 and r1_vina <= 100:
            color_vina = "yellow"
        if r1_vina >= 101 and r1_vina <= 150:
            color_vina = "orange"
        if r1_vina >= 151 and r1_vina <= 200:
            color_vina = "red"
        if r1_vina >= 201 and r1_vina <= 300:
            color_vina = "purple"
        
    if x == '4' : #valdivia
        if r1_valdivia >= 0 and r1_valdivia <= 50:
            color_valdivia = "green"
        if r1_valdivia >= 51 and r1_valdivia <= 100:
            color_valdivia = "yellow"
        if r1_valdivia >= 101 and r1_valdivia <= 150:
            color_valdivia = "orange"
        if r1_valdivia >= 151 and r1_valdivia <= 200:
            color_valdivia = "red"
        if r1_valdivia >= 201 and r1_valdivia <= 300:
            color_valdivia = "purple"

    if x == '5' : #temuco
        if r1_temuco >= 0 and r1_temuco <= 50:
            color_temuco = "green"
        if r1_temuco >= 51 and r1_temuco <= 100:
            color_temuco = "yellow"
        if r1_temuco >= 101 and r1_temuco <= 150:
            color_temuco = "orange"
        if r1_temuco >= 151 and r1_temuco <= 200:
            color_temuco = "red"
        if r1_temuco >= 201 and r1_temuco <= 300:
            color_temuco = "purple"

    if x == '6' : #las condes
        if r1_lascondes >= 0 and r1_lascondes <= 50:
            color_lascondes = "green"
        if r1_lascondes >= 51 and r1_lascondes <= 100:
            color_lascondes = "yellow"
        if r1_lascondes >= 101 and r1_lascondes <= 150:
            color_lascondes = "orange"
        if r1_lascondes >= 151 and r1_lascondes <= 200:
            color_lascondes = "red"
        if r1_lascondes >= 201 and r1_lascondes <= 300:
            color_lascondes = "purple"



# Create your views here.
def index(request):
    return render(request,'pages/index.html', {"quintero": aqi_quintero, "r1_q": r1_quintero, "r2_q": r2_quintero, "vina": aqi_vina, "r1_v": r1_vina, "r2_v": r2_vina, "valdivia": aqi_valdivia, "r1_va": r1_valdivia, "r2_va": r2_valdivia,"temuco": aqi_temuco, "r1_t": r1_temuco, "r2_t": r2_temuco, "lascondes": aqi_lascondes,"r1_lc": r1_lascondes,"r2_lc": r2_lascondes, "color_q": color_quintero, "color_vi": color_vina, "color_va": color_valdivia, "color_t": color_temuco, "color_lc": color_lascondes })

def error(request):
    return render(request,'pages/404.html')





