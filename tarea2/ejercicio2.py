import hashlib

"""
Archivo para el ejercicio 2 de la tarea
"""



def pedazo(tamanio):
    """
    Método para regresar un pedszo de contraseñas del archivo de contraseñas para no estar
    revisando todas de jalon, ya que se puede acabar la memoria para ciertas conputadoras
    limitas en memoria
    """
    p = []
    contador = 0
    with open("realhuman_phill.txt", "rb") as file:
        for linea in file:
            p.append(linea[:-1])
            contador += 1
            if contador == tamanio:
                contador = 0
                # ocuapmos la funcion generadora para que guarde la lista conforme se va generando,
                # ya que si llenamos la lista con todo el archivo de 6 millones de contraseñas
                # se tiene que construir primero la lista de ese tamaño

                yield p
                p = []
        if contador < tamanio:
            #regresamos el generador 
            
            yield p


def juanito():
    """
    Método para encontrar la contraseña de juanito
    """

    sal = bytes.fromhex("d8201aae236713fefe9a5266dc1f8012")
    contraseniaHasheada = bytes.fromhex("5f495364792782144918397bdbb72bc04326a883138a11f3d0b61a3d2576ca00")
    contrasenias = pedazo(1000000)
    for i in contrasenias:         
        contrasenia = hashlib.scrypt(i, salt=sal,n=2*16, r=8, p=1, maxmem=2*30, dklen=32)
        if contrasenia == contraseniaHasheada:
            return i


if __name__ == "__main__":
    archivo = "./BD_jaqueada.txt"
    usuarios = []
    with open(archivo) as file:
        for linea in file:
            fila = linea.split("$")           
            usuario = (bytes.fromhex(fila[1]) , bytes.fromhex(fila[2].strip("\n")))
            usuarios.append(usuario)
    
    with open("res.txt", "w") as file:
       for contrasenia in range(500):
            g = pedazo(100000)
            for pe in g:

                for i in pe:
                    contrasenia1 = hashlib.sha256(usuarios[contrasenia][0]+i).digest()
                    contrasenia2 = hashlib.sha256(i+usuarios[contrasenia][0]).digest()

                    if contrasenia1 == usuarios[contrasenia][1] or contrasenia2 == usuarios[contrasenia][1]:
                        
                        if i != None:
                            file.write("{}{}\n".format(contrasenia, i))  

    

