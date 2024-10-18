# Ejemplo de "memoria dinámica"
def promedio_edades_dinamico():
    edades = []  # Simula memoria dinámica
    while True:
        entrada = input("Ingresa una edad (o 'q' para salir): ")
        if entrada == 'q':
            break
        try:
            edad = int(entrada)
            edades.append(edad)  # La lista crece dinámicamente
        except ValueError:
            print("Por favor, ingresa un número válido.")
    
    if len(edades) == 0:
        return "No se ingresaron edades."
    
    total = sum(edades)
    promedio = total / len(edades)
    return promedio

# Llamada a la función
print(f"Promedio de edades (memoria dinámica): {promedio_edades_dinamico()}")
