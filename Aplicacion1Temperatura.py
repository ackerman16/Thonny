#Estado del agua
= int(input("Temperatura:"))
if temperatura > 100:
    print("El estado del agua será gaseoso")
elif temperatura < 0:
    print("El estado del agua será solido")
else:
    print("El estado del agua será líquido")