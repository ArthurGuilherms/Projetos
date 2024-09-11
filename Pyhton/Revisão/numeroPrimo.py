def verificar(numero):
    verificador = False
    if numero % 1 == 0 & numero % numero == 0:
        verificador = True
        for x in range(2, numero):
            if numero % x == 0:
                verificador = False
    if numero == 1:
        verificador = False
        
    if verificador == True:
        return " é primo"
    if verificador == False:
        return " não é primo"
    
        

for x in range (1, 20):
    resultado = str(verificar(x))
    print("Número", x , resultado)