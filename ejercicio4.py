def manipular_cadena(cadena, letra_a_remplazar, nueva_letra):
 
  cadena_minuscula = cadena.lower()

  cadena_modificada = cadena_minuscula.replace(letra_a_remplazar, nueva_letra)

  lista_palabras = cadena_modificada.split()

  print("Cadena modificada:", cadena_modificada)
  print("Lista de palabras:", lista_palabras)

cadena_original = "Hola, cómo estás? El día está genial."
letra_a_cambiar = "a"
nueva_letra = "e"

manipular_cadena(cadena_original, letra_a_cambiar, nueva_letra)
