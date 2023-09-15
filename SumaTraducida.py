def traducir_a_espanol(numero):
    # Números en español
    numeros_espanol = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez"]
    return numeros_espanol[numero]

def traducir_a_ingles(numero):
    # Definir un diccionario (diccionario) con las traducciones
    numeros_traducidos = {
        "cero": "zero",
        "uno": "one",
        "dos": "two",
        "tres": "three",
        "cuatro": "four",
        "cinco": "five",
        "seis": "six",
        "siete": "seven",
        "ocho": "eight",
        "nueve": "nine",
        "diez": "ten"
    }
    numero_espanol = traducir_a_espanol(numero)
    return numeros_traducidos.get(numero_espanol)

def imprimir_suma_espanol(numero1, numero2, suma):
    numero1_str = traducir_a_espanol(numero1)
    numero2_str = traducir_a_espanol(numero2)
    suma_str = traducir_a_espanol(suma)
    print(f"La suma de {numero1_str} más {numero2_str} es igual a {suma_str}")

def imprimir_suma_ingles(numero1, numero2, suma):
    numero1_str = traducir_a_ingles(numero1)
    numero2_str = traducir_a_ingles(numero2)
    suma_str = traducir_a_ingles(suma)
    print(f"The sum of {numero1_str} plus {numero2_str} is equal to {suma_str}")

def sumar(numero1, numero2):
    suma = numero1 + numero2
    return suma

numero1 = 3
numero2 = 5

suma = sumar(numero1, numero2)
imprimir_suma_espanol(numero1, numero2, suma)
imprimir_suma_ingles(numero1, numero2, suma)
