from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
from django.template.loader import get_template
from django.shortcuts import render


# Request: Para realizar peticiones
# HttpResponse: Para enviar la respuesta usando el protocolo HTTP

#Esto es una vista:
def bienvenida(request): #Pasamos un objeto de tipo request como primer agumento
    return HttpResponse("Bienvenidos al Himalaya")

def bienvenidaRojo(request): #Pasamos un objeto de tipo request como primer agumento
    return HttpResponse("<p style='color: red;'> Bienvenidos al Himalaya</p>")

def categoriaEdad(request, edad):
    if edad >= 18:
        if edad >= 60:
            categoria = "Tercera edad"
        else:
            categoria = "Adultez"
    else:
        if edad <10:
            categoria = "Infancia"
        else: 
            categoria = "Adolescencia"

    resultado = "<h1> Categoría de la edad: %s </h1>" %categoria
    return HttpResponse(resultado)

def obtenerMomentoActual(request):
    respuesta = "<h1>Momento actual: {0}</h1>".format(datetime.datetime.now().strftime("%A %d/%m/%Y %H:%M:%S"))
    return HttpResponse(respuesta)

def contenidoHTML(request, nombre, edad):
    contenido = """ 
    <html>
    <body>
    <p>Nombre: %s / Edad: %s</p>
    </body>
    </html>
    """ %(nombre, edad)
    return HttpResponse(contenido)

def miPrimeraPlantilla(request):
    #Abrimos el documento que contiene a la plantilla
    plantillaExterna = open("C:/Users/laraa/Documents/Proyecto-Django/MiProyecto/MiProyecto/plantillas/miPrimeraPlantilla.html")
    template = Template(plantillaExterna.read())
    #Cerrar el documento externo que hemos abierto
    plantillaExterna.close()
    #Crear un contexto
    contexto = Context()
    documento = template.render(contexto)
    return  HttpResponse(documento)

def plantillaParametros(request):
    nombre = "Jeslar"
    fechaActual = datetime.datetime.now()
    lenguajes = ["Python", "Ruby", "JavaScript", "Java", "C#", "Kotlin"]
    #Abrimos el documento que contiene a la plantilla
    plantillaExterna = open("C:/Users/laraa/Documents/Proyecto-Django/MiProyecto/MiProyecto/plantillas/plantillaParametros.html")
    template = Template(plantillaExterna.read())
    #Cerrar el documento externo que hemos abierto
    plantillaExterna.close()
    #Crear un contexto
    contexto = Context({"Nombre": nombre, "fechaActual": fechaActual, "lenguajes": lenguajes})
    documento = template.render(contexto)
    return  HttpResponse(documento)

def plantillaCargador(request):
    nombre = "Jeslar"
    fechaActual = datetime.datetime.now()
    lenguajes = ["Python", "Ruby", "JavaScript", "PHP", "Java", "C#", "Kotlin"]
    #Estamos especificando la carpeta donde se encuantran las plantillas y creammos una variable que las almacena
    plantillaExterna = get_template("plantillaParametros.html")
    #Renderizar el documento que vamos a mandar.
    documento = plantillaExterna.render({"Nombre": nombre, "fechaActual": fechaActual, "lenguajes": lenguajes})
    return HttpResponse(documento)

def plantillaShortcut(request):
    nombre = "Jeslar"
    fechaActual = datetime.datetime.now()
    lenguajes = ["Python", "Ruby", "JavaScript","C++", "PHP", "Java", "C#", "Kotlin"]

    return render(request, "plantillaParametros.html", {"Nombre": nombre, "fechaActual": fechaActual, "lenguajes": lenguajes})

def plantillaHija1(request):
    return render(request, "plantillaHija_1.html", {})

def plantillaHija2(request):
    return render(request, "plantillaHija_2.html", {})