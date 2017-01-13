import codecs

def borrarContenido(archivo): # Función utilizada para borrar el contenido de un archivo.
    archivo.seek(0)
    archivo.truncate()

def numberList(nums, limit):
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

def borrarenLista(lista, number):
    for i in range(number):
        lista.pop(0)

def printheader():
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

longitud = [] # Definimos la lista que contedrá las longitudes de cada línea.
comandos = []

comentario = "//" # Creamos una variable que contenga la separación del comentario en el autoexec. En este caso es una barra doble.
suma = 0

abrir_archivo = codecs.open("autoexec.txt", "r", "utf-8") # Abrimos el archivo del autoexec normal.
archivo_escribir = codecs.open("converted.txt", "w", "utf-8") # Creamos el archivo donde escribiremos el resultado.

lines = abrir_archivo.readlines() # Leemos las líneas del archivo y las metemos en una lista.
#print(lines)

printheader()

lineas = len(lines) + 1 # Hayamos el numero de líneas del archivo autoexec. Le sumamos 1 porque las listas asociativas empiezan desde 0.

#print(lineas)

for linea in lines:
    lineaactual = linea
    lineaactual = lineaactual.strip("\n")
    lineaactual = lineaactual.strip()
    if lineaactual.strip(): # Comprobamos que la línea en cuestión tiene contenido.
        if not lineaactual.startswith(comentario): # Comprobamos que la línea no empieza con un comentario "//".
            if comentario in lineaactual: # Comprobamos si la línea contiene ALGÚN comentario. En tal caso lo borramos y nos quedamos con la parte del comando.
                separarcomentario = lineaactual.split(comentario, 1) # Partimos el string del comentario en 2, justo por la doble barra.
                lineaactual = separarcomentario[0] # Nos quedamos con el primer elemento, que siempre será el comando.
                lineaactual = lineaactual.strip() # Borramos los espacios en blanco que queden a ambos lados, quedandonos el comando íntegro.
            lineaactual = lineaactual + ";"
            #print(lineaactual) ## BORRAR
            longitudcomando = len(lineaactual)
            #archivo_escribir.write(lineaactual + "\n") # DEJAR COMENTADO, DEBUG
            comandos.append(lineaactual) #Añadimos a nuestra lista comandos todos los elementos correspondientes.
            longitud.append(longitudcomando)

numcomandos = len(numberList(longitud, 255))

while numcomandos  <= len(longitud):
  numcomandos = len(numberList(longitud, 255))
  for i in range(0,numcomandos):
      comandoactual = comandos[i]
      archivo_escribir.write(comandoactual)
  print(numcomandos)
  borrarenLista(comandos, numcomandos)
  borrarenLista(longitud, numcomandos)
  archivo_escribir.write("\n -------------------------------------- \n")
  print(longitud)

if numcomandos > len(longitud):
    numcomandos = len(longitud)
    for i in range(0,numcomandos):
        comandoactual = comandos[i]
        archivo_escribir.write(comandoactual)
    borrarenLista(comandos, numcomandos)
    borrarenLista(longitud, numcomandos)
    archivo_escribir.write("\n -------------------------------------- \n")
    print(comandos)
    print(longitud)

print(comandos)
print (longitud)
print (len(longitud))
print (sum(longitud))



"""
total = 0
for line in lines:
    while total < 255:
        lineaactual = line
        #print(len(line))
        cuenta = len(lineaactual)
        print(str(cuenta) + ' esta es la cuenta')
        total = total + cuenta
        print(total)
        lineaactual += 1

"""

"""
while tira <= 255:
    cuenta = len(lines)
    print(cuenta)
    tira = tira + cuenta
    line+= 1
    print(tira)

for line in lines:
    print(len(line))
"""

archivo_escribir.close()
abrir_archivo.close()
