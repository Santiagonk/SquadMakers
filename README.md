# SquadMakers

## Requerimientos

La prueba consiste en crear un API Rest en el framework Flask con los siguientes endpoints:
*	Endpoint de chistes. 
o	GET: Se devolverá un chiste aleatorio si no se pasa ningún path param. Si se envía el path param habrá que comprobar si tiene el valor “Chuck” o el valor “Dad”. Si tiene el valor “Chuck” se conseguirá el chiste de este API https://api.chucknorris.io. Si tiene el valor “Dad” se conseguirá del API https://icanhazdadjoke.com/api. En caso de que el valor no sea ninguno de esos dos se devolverá el error correspondiente.
*	Endpoint matemático:
o	GET: Endpoint al que se le pasará un query param llamado “numbers” con una lista de números enteros. La respuesta de este endpoint debe ser el mínimo común múltiplo de ellos.
o	Get: Endpoint al que se le pasará un query param llamado “number” con un número entero. La respuesta será ese número + 1.


## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

1. Clonar el repositorio:
`git clone`

2. Crear entorno virtual:
  * Windows:
  Ejecutar en terminal
   * `py -m venv venv`
  * Linux:
   * `python3 -m venv venv`
  * Mac OS:
   * `python3 -m venv venv`
  
3. Iniciar el entorno virtual:
  * Windows:
   * `.\venv\Scripts\activate.bat`
  * Linux:
   * `source ./venv/bin/activate`
  * Mac OS:
   * `source ./venv/bin/activate`
  
4. Instalar librerias:
  * `pip install -r requirements.txt`
  
5. Iniciar el servidor:
  * `flask run`

## Pre-requisitos 📋

* Python 3

## Despliegue 📦

_Agrega notas adicionales sobre como hacer deploy_

### Link de despliegue:

* [Link despliegue Heroku](https://warm-beyond-31783.herokuapp.com/)

### Documentacion API

* [Documentación en Postman](https://web.postman.co/workspace/My-Workspace~21065134-1b3f-4786-81bd-471da866a0e7/documentation/15367532-0a0a1b82-bb24-4132-8e9f-477d1bc54d29)

### Construido con 🛠️

* [Flask](https://flask.palletsprojects.com/en/2.0.x/) - framework para API's basado en [Flask](https://flask.palletsprojects.com/en/2.0.x/)


### Versionado 📌

Usamos la siguiente [convención](https://www.notion.so/Commit-conventions-0ab0b6cde23b49e5a9c0bbeb73970072).

### Autor ✒️

* **Santiago Salgado** - [GitHub](https://github.com/Santiagonk)
