#Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:

def calculadora (numero1, numero2, operacao):
    if (operacao == 1):
        return numero1 + numero2
    elif(operacao == 2):
        return numero1 - numero2
    elif(operacao == 3):
        return numero1 * numero2
    elif (operacao == 4):
        return numero1 / numero2
    
    else:
        return 0
    
resultado = calculadora(4, 7, 1)
print(resultado)    
