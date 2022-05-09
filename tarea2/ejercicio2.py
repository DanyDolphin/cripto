import hashlib



def lee(archivo):
    usuarios = []
    with open(archivo) as file:
        for linea in file:
            fila = linea.split("$")
            print(fila[2].strip())
            
            usuario = (bytes.fromhex(fila[1]) , bytes.fromhex(fila[2].strip("\n")))
            usuarios.append(usuario)
    return usuarios

def getLote(tamanio):
    lote = []
    contador = 0
    with open("realhuman_phill.txt", "rb") as file:
        for linea in file:
            lote.append(linea[:-1])
            contador += 1
            if contador == tamanio:
                contador = 0
                yield lote
                lote = []
        if contador < tamanio:
            yield lote
def encuentraContra(sal, hashContra, contrasenias):
    for i in contrasenias:
        s = hashlib.sha256(sal+i).digest()
        s1 = hashlib.sha256(i+sal).digest()

        if s == hashContra or s1 == hashContra:
            return i


def decode(idUsuario):
    g = getLote(1000)
    for lote in g:
        contra = encuentraContra(usuarios[idUsuario][0], usuarios[idUsuario][1],  lote)
        if contra != None:
            return contra
    print("NO")

def decodeContra():
    with open("res.txt", "w") as file:
        for contrasenia in range(1):
            file.write("usario {} {}\n".format(contrasenia, decode(contrasenia)) )
    return "chidos"

if __name__ == "__main__":
    archivo = "./BD_jaqueada.txt"
    usuarios = lee(archivo)
    
    print(decodeContra())

