lista=[]



while len(lista)<3:
     x=lista.append(int(input("ingrese su lista ")))

def promedio(x):
    suma=sum(x)/len(x)
    return suma

x=promedio(lista)
print(x)