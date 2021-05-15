# Forocoches UP
Esto es un upeador de posts de [forocoches](https://forocoches.com)

## EN CONSTRUCCION
pues eso lo voy a dejar de lado una temporada

## Requirements
    - Selenium
    - Raspberry?

## Disclaimer:


No soy tu soporte tecnico, si no sabes donde te metes, no preguntes.


## How start

1- Teneis que abrir el archivo y editar la url de la carpeta de firefox para que se conecte automaticamente sin hacer login, coge las cookies y ya estas dentro.

2- Por defecto, el tiempo entre respuesta y respuesta es de 60segundos, lo puedes cambiar en `time.sleep(XX)`, obvio: min: 30

3- Cambiar cuantos mensajes quieres escribir, en el bucle ` for i in range(1,200)`, esta puesto 200 mensajes, puedes cambiarlo a lo que quieras.


Parametros: 

`{URL}` es la url del sitio, ejemplo: `https://www.forocoches.com/foro/showthread.php?p=402553270`


`python3 main.py {URL}`

osea que se quedaria asi:
`python3 main.py https://www.forocoches.com/foro/showthread.php?p=402553270`

## Why?
Porque puedo y porque no hay, si te gusta dale amor con estrellitas y conviame a un cafelillo.