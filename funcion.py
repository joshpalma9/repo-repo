lista=[]

x=int(input("ingrese primer numero "))
lista.append(x)
y=int(input("ingrese segundo numero "))
lista.append(y)
z=int(input("ingrese tercer numero "))
lista.append(z)

# while len(lista)<3:
#     x=lista.append(int(input("ingrese su lista ")))

def promedio(lista):
    suma=sum(lista)/len(lista)
    return suma

x=promedio(lista)
print(x)