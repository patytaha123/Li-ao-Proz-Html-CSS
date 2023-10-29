#imprimir todos os numeros exeto 13(laço 13 for in ... range)
for i in range(1 , 21):
    if(i==13):
        continue
    else:
        print(i)
        
 #imprimir todos os numeros exeto 13(laço 13"while")
contador = 1
while (contador <=20):
    if(contador==13):
        contador = contador + 1
        continue
    else:
        print(contador)    
        contador = contador + 1   

               
 #imprimir todos os numeros exeto 13 em ordem descendente

for i in range(20, 0, -1):
    if(i==13):
        continue
    else:
        print(i)
        
