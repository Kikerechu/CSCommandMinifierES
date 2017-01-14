import codecs # Paquete con el que podremos crear (y abrir) un archivo en codificación UTF-8. Necesario para escribir las tildes. No está incluido en la versión inglesa por razones obvias :).

def borrarContenido(archivo): # Función utilizada para borrar el contenido de un archivo.
    archivo.seek(0)
    archivo.truncate()

def numberList(nums, limit): # Función maestra de todo el programa. Encuentra las sumas de las longitudes de los comandos sin pasarse del límite impuesto de 255.
    prefix = []
    suma = 0
    if sum(nums) < limit:
        return prefix
    for num in nums:
        suma += num
        prefix.append(num)
        if suma >= limit:
            prefix.pop()
            return prefix

def borrarenLista(lista, number): #Función para borar i veces el primer elemento de una lista. Útil para quitar los comandos que ya han sido procesadosy quedarnos con lo útil.
    for i in range(number):
        lista.pop(0)

def printheader(): # Imprimir las líneas de información y créditos.
    archivo_escribir.write("-------------------------------------------------\n")
    archivo_escribir.write("| Creado por Enrique Carpintero - EnriqueCG.es |\n")
    archivo_escribir.write("-------------------------------------------------\n\n\n")
    archivo_escribir.write("Se ha convertido tu archivo correctamente\n")
    archivo_escribir.write("Debido a una restricción en la consola de CS:GO solo se pueden introducir 255 caracteres como máximo por comando.\n")
    archivo_escribir.write("Se han separado en varias líneas de máximo 255 caracteres, por la razón antes mencionada\n")
    archivo_escribir.write("Debes de introducir los comandos en la consola en el orden indicado. Si no es así pueden ocurrir errores.\n")
    archivo_escribir.write("Gracias por utilizar CSCommandMinifier. Visita mi perfil en GitHub para proyectos similares: https://github.com/Kikerechu/\n\n\n\n")
    archivo_escribir.write("COMANDOS\n\n\n\n")
    archivo_escribir.write("-------------------------------------- \n")

## Pedimos al usuario que introduzca el nombre del archivo, para una mayor comodidad.
print("Introduce el nombre del archivo que contiene la información autoexec, con extensión por favor :) ")
print("Por ejemplo 'autoexec.cfg' o 'miconfiguracion.txt'")
nombreArchivo = input("Nombre del archivo: ")

nombreArchivo = nombreArchivo.strip()

while not nombreArchivo: # Si el usuario no ha introducido nada (ergo, la variable NombreArchivo esta vacía), pedimos que la vuelva a introducir. Esto se repite hasta que se introduce algún dato.
    print("Debes introducir el nombre del archivo al que quieres realizar la conversión")
    nombreArchivo = input("Nombre del archivo: ")

while True: # Aquí es donde nos aseguramos de que la extensión es correcta.
    if '.' not in nombreArchivo: # Si no hay un .
        print("¡ERROR!, debes incluir la extension. De momento solo acepto extensiones de texto plano .txt y .cfg :( ")
        nombreArchivo = input("Nombre del archivo: ")
    if 'txt' not in nombreArchivo: # Si no hay txt en la cadena de texto.
        if 'cfg' not in nombreArchivo: # Si no hay cfg en la cadena de texto.
            print("¡ERROR!, por el momento solo acepto extensiones de texto plano .txt y .cfg :( ")
            nombreArchivo = input("Nombre del archivo: ")
        else: # Si las condiciones anteriores se cumplen, salir del bucle.
            break
    else: # Lo mismo pero adaptado al bloque indentado.
        break

longitud = [] # Definimos la lista que contedrá las longitudes de cada línea.
comandos = [] # Definimos la lista que contedrá los comandos una vez procesados, sin comentarios y sin espacios, etc.
numtiras = 0
## print(nombreArchivo) # DEBUG, DEJAR COMENTADO.
comentario = "//" # Creamos una variable que contenga la separación del comentario en el autoexec. En este caso es una barra doble.

abrir_archivo = open(nombreArchivo, "r") # Abrimos el archivo del autoexec normal.
#archivo_escribir = codecs.open("autoexec_convertido.txt", "w", "utf-8") # Creamos el archivo donde escribiremos el resultado.
archivo_escribir = open("autoexec_convertido.txt", "w") # Creamos el archivo donde escribiremos el resultado.

lineas = abrir_archivo.readlines() # Leemos las líneas del archivo y las metemos en una lista. Cada elemento de la lista será una línea.
# print(lines) ## DEBUG

printheader() # Imprimimos nuestro header.

# print(lineas) ## DEBUG

for linea in lineas: # Iteramos por cada elemento de la lista lineas.
    lineaactual = linea # Creamos una variable que lleve el contenido de la línea.
    lineaactual = lineaactual.strip("\n") # Quitamos la separación de líneas. Un /n al final de una línea indica el final de esta.
    lineaactual = lineaactual.strip() # Quitamos espacios en blanco a ambos lados.
    if lineaactual.strip(): # Comprobamos que la línea en cuestión tiene contenido.
        if not lineaactual.startswith(comentario): # Comprobamos que la línea no empieza con un comentario "//".
            if comentario in lineaactual: # Comprobamos si la línea contiene ALGÚN comentario. En tal caso lo borramos y nos quedamos con la parte del comando.
                separarcomentario = lineaactual.split(comentario, 1) # Partimos el string del comentario en 2, justo por la doble barra.
                lineaactual = separarcomentario[0] # Nos quedamos con el primer elemento, que siempre será el comando.
                lineaactual = lineaactual.strip() # Borramos los espacios en blanco que queden a ambos lados, quedandonos el comando íntegro.
            lineaactual = lineaactual + ";"
            print(lineaactual) ## Imprimos en la consola la línea independiente una vez procesada. Útil para ver si todo está correcto.
            longitudcomando = len(lineaactual)
            #archivo_escribir.write(lineaactual + "\n") # DEJAR COMENTADO, DEBUG
            comandos.append(lineaactual) #Añadimos a nuestra lista comandos todos los elementos correspondientes.
            longitud.append(longitudcomando) # Lo mismo ocurre con nuestras longitudes de comando.

numcomandos = len(numberList(longitud, 255)) # Número de comandos que puede incluir la primera "tira" de 255 carácteres como máximo.
print("\nHay " + str(len(longitud)) + " líneas con comandos.")

while numcomandos  <= len(longitud): # Mientras el numero de comando por línea sea igual o inferior a la longitud de la lista de las longitudes. (Lo sé, es rebuscado).
    if numcomandos == 0: # La función numberList tiene una flaqueza, y es que cuando el archivo autoexec contiene menos de 255 carácteres, devuelve un 0, haciendo el bucle while infinito, dado que 0 siempre será menor o igual que una longitud, que siempre se mide en numeros enteros positivos. Esto se arregla añadiendo la condición dentro del bucle if == 0, pues realiza la acción una sola vez.
        numcomandos = len(longitud) # Llamamos numcomandos a la longitud de la lista longitud.
        for i in range(0,numcomandos): # Iteramos a lo largo de la lista.
          comandoactual = comandos[i] # Igualamos la variable comandoactual al comando correspondiente en la iteración.
          archivo_escribir.write(comandoactual) # Escribimos el comando en el archivo.
        archivo_escribir.write("\n -------------------------------------- \n")
        numtiras += 1 # El numero de tiras será entonces 0 + 1 = 1. Dado que la única tira que hay es menor de 255 carácteres.
        print("Solo una tira que contiene '" + str(numcomandos) + "' comandos") # Imprimos información útil para el usuario.
        break # Una vez finalizado todos los pasos anteriores, rompemos el bucle while.
    # Si no se cumple que numcomandos  = 0, continuamos abajo.
    numcomandos = len(numberList(longitud, 255)) # El numero de comandos que necesitamos en la tira actual.
    for i in range(0,numcomandos): # Iteramos de nuevo a lo largo de la lista.
      comandoactual = comandos[i] # Igualamos la variable comandoactual al comando correspondiente en la iteración.
      archivo_escribir.write(comandoactual) # Escribimos el comando en el archivo.
    #print(numcomandos) # DEBUG, DEJAR COMENTADO
    borrarenLista(comandos, numcomandos) # Borramos en la lista comandos, el número de comandos de la tira actual. De esa forma la prixima vez que iteremos por aquí lo haremos con estos elementos ya procesados que han sido eliminados.
    borrarenLista(longitud, numcomandos) # Lo mismo pero con la lista que contiene las longitudes de los comandos.
    archivo_escribir.write("\n -------------------------------------- \n")
    #print(longitud) # DEBUG, DEJAR COMENTADO
    numtiras += 1 # Cada vez que iteremos por el bucle, se sumará 1 a la variable numtiras.
    print("La tira '" + str(numtiras) + "' contiene " + str(numcomandos) + " comandos") # Luego imprimimos numtiras conforme el bucle se cumple. Simplemente información útil al usuario.


if numcomandos > len(longitud): #Si el número de comandos es menor a la longitud de la lista longitud.
    numcomandos = len(longitud) # La variable numcomandos se iguala a longitud.
    for i in range(0,numcomandos):
        comandoactual = comandos[i]
        archivo_escribir.write(comandoactual)
    borrarenLista(comandos, numcomandos)
    borrarenLista(longitud, numcomandos)
    archivo_escribir.write("\n -------------------------------------- \n")
    numtiras += 1
    print("La tira '" + str(numtiras) + "' contiene " + str(numcomandos) + " comandos")
    #print(comandos) # DEBUG, DEJAR COMENTADO
    #print(longitud) # DEBUG, DEJAR COMENTADO

if numtiras == 1: # Pequeña tontería. Por si acaso la tira es solo 1, pues poner el nombre en singular.
    tirasplural = " tira"
else:
    tirasplural = " tiras"


print("\nSe ha dividido tu autoexec en " +str(numtiras)+ tirasplural + ". Debes de introducir cada tira en orden y asegurate de que copias la línea entera.")

# Terminamos cerrando ambos archivos para asegurar una lectura y una escritura sin pérdida de información.

archivo_escribir.close()
abrir_archivo.close()
