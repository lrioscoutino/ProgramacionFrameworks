import logging
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	numero = 5*2
	cadena = "Bienvenidos a mi primer"
	return HttpResponse("<h1>"+ cadena + "vista con python en Django "+ str(numero) +" veces </h1>")


def ViewTemplate(request):
	print(f"Aqui inicia la petición del navegador {request}")
	print(request.user, request.method)
	logging.info(request.user)
	
	name_student = "Alberto Perez"
	age_student = 44
	calificaciones= [5, 8, 7, 9, 10, 10, 5, 8]

	#Consultar una base de datos
	#asignar el resultado de la consulta a una variable

	contexto = {
	'name_student':name_student,
	'age_student':age_student,
	'control_number': "77777777",
	'calificaciones': calificaciones
	}
	
	if calificaciones:
		print("si tiene calificaciones")
	else:
		print("No tiene calificaciones")

	return render(request, "index.html", context=contexto)

def about(request):
	return render(request, "about.html")

def contact_us(request):
	return render(request, "contact_us.html")