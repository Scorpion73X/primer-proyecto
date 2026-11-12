respuestas_ia = [
    {"usuario": "Diego", "calificacion": 5},
    {"usuario": "Camila", "calificacion": 2},
    {"usuario": "Gonzalo", "calificacion": 4},
    {"usuario": "Valentina", "calificacion": 1}
]
print("Evaluacion de satisfaccion")



for item in respuestas_ia:
    usuario = item["usuario"]
    calificacion = item["calificacion"]


    if calificacion >= 3:
        print(f"{usuario} esta satisfecho con la IA")
    else:
        print(f"{usuario} no esta satisfecho con la IA")