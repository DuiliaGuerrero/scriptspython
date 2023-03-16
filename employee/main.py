import random
import names
from random import randrange
from datetime import timedelta, datetime


limite_nacimiento_inicial = datetime.strptime('1/1/1965 1:30 PM', '%m/%d/%Y %I:%M %p')
limite_nacimiento_final = datetime.strptime('1/1/2003 4:50 AM', '%m/%d/%Y %I:%M %p')

fecha_inicio_trabajo = datetime.strptime('1/1/1998 1:30 PM', '%m/%d/%Y %I:%M %p')
ultimo_ingreso_trabajo = datetime.strptime('1/1/2023 1:30 PM', '%m/%d/%Y %I:%M %p')

def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

cargos = ["Desarrollador Full Stack",
          "Desarrollador Back-End",
          "Desarrollador Front-End",
          "Profesional de Ciberseguridad",
          "Desarrollador móvil",
          "Analista DevOps",
          "Científico de datos o Ingeniero de datos",
          "Arquitecto de Big Data",
          "Secretarix",
          "Contadxr"]

generos = ["Femenino", "Masculino"]

departamentos = ["Departamento de marketing",
                 "Departamento comercial",
                 "Departamento administrativo",
                 "Recursos humanos",
                 "Departamento de finanzas",
                 "IT"]

for i in range(20):
    genero = random.choice(generos)
    gender = "male"
    if genero == "Femenino":
        gender = "female"
    empleado = {
        "id": random.randint(1, 984653),
        "nombre": names.get_full_name(gender=gender),
        "genero": genero,
        "cargo": random.choice(cargos),
        "fecha_nacimiento": random_date(limite_nacimiento_inicial, limite_nacimiento_final).isoformat(),
        "departamento": {
            "nombre": random.choice(departamentos)
        },
        "fecha_ingreso" : random_date(fecha_inicio_trabajo, limite_nacimiento_final).isoformat(),
        "salario": random.randint(1000000, 5000000),
        "comision": random.randint(100000, 500000)
    }

    print(empleado, end=",\n")