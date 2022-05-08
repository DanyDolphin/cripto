from sys import argv,version_info
import os
assert version_info[0] == 3, 'USA PYTHON 3'
print('Recuperando archivos :p')

# función que cambia los bytes de un archivo
# como el inverso de XOR es XOR, usamos la misma función
def xx(x, k):
    # z = archivo destino sin '.enc'
    with open(x[:-4],'wb') as z:
        cambia_bytes = lambda x: bytes(
            # x = la lista de bytes
            # se guarda x[i] ^ k[i % 6]
            # k = 16 random bytes
            [x[i] ^ k[i%16] for i in range(len(x))]
        )
        z.write(
            # x = nombre del archivo
            cambia_bytes(open(x,'rb').read())
        )

# función que elimina un archivo dado un nombre
def delete_enc(x):
    # elimina archivo
    os.remove(x)

# x = lista de nombres de archivos en el directorio ./
_,_,x = next(os.walk('./'))
# eliminamos el script de la lista
# y juego.py
x.remove(argv[0])
x.remove('juego.py')
x.remove('.xyz')

# recuperamos los valores de c, d y k
z = open('.xyz', 'rb')
keys = z.read()
# c = primer byte
c = bytes([keys[0]])
# d = siguientes 32 bytes
d = bytes(keys[1:33])
# k = ultimos 42 bytes
k = bytes(keys[33:])
# convertimos a numeros
c = c[0]
d,k=map(lambda x:int.from_bytes(x,'big'),[d,k])
# d = k0 | 1
# por lo que k0 = d ó k0 = d - 1
for k0 in [d, d-1]:
    # regresamos a bytes
    kbytes = k0.to_bytes(16,'big')
    # recuperamos los archivos
    list(map(lambda x: xx(x,kbytes),x))
    # preguntamos si los archivos estan recuperados
    # para saber si intentar con d-1 o no
    res = input('Los archivos ya estan bien? [Y,n]')
    if not res or res.lower() == 'y':
        # eliminamos los archivos encriptados
        list(map(delete_enc, x))
        break

print('Archivos recuperados :D')
