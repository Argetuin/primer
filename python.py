temperatura = float(input("Ingrese temperatura: "))
temp = input("Es Fahrenheit (F) o Celcius (C): ").lower()

if temp == "f":
        operaciones = ((temperatura-32)*(5/9))
        operaciones = round(operaciones, 2)
        print (operaciones)
    
    