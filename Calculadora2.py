def calculadora(n1, n2, operador):
    n1 = float(n1)
    n2 = float(n2)
    cod = int(operador)
    if cod == 1:
        res = n1 + n2

    elif cod == 2:
        res = n1 - n2

    elif cod == 3:
        res = n1 * n2

    elif cod == 4:
        res = n1 / n2
    else:
        res = 0

    return res

while True:
    print("""Digite o operador: 
  1. Soma
  2. Subtração
  3. Multiplicação
  4. Divisão
  0. Sair""")

    codigo = int(input("Digite o operador: "))
    if codigo == 0:
        break
    if codigo > 4 or codigo < 0:
        print("Essa opção não existe")
        continue
    nota_1 = input("Digite o primeiro número: ")
    nota_2 = input("Digite o segundo número: ")

    resultado = calculadora(nota_1, nota_2, codigo)
    print(f"O resultado é : {resultado}")

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
operador = int(input('Digite o numero do operador == 1.soma; 2.subtração; 3.multiplicação; 4.divisão: '))

resultado = calculadora(num1, num2, operador)
print(resultado)
