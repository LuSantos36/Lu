def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Operação inválida: divisão por zero."
    return a / b

def  main ():
    while True:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operacao (+,-,*,/): ")

        if operacao == '+':
             print(f"Resultado: {soma(num1,num2)}")
        elif operacao == '-':
            print(f"Resultado: {subtracao(num1,num2)}") 
        elif operacao == '*':
            print(f"Resultado: {multiplicacao(num1,num2)}")
        elif operacao == '/':
            print(f"Resultado: {divisao(num1,num2)}")
            if(num2 !=0):
                return num1/num2
           
            else:
                print("Operação inválida")

        stop = input("Deseja parar o programa? (1 - Sim / 2 - Não): ")
        if stop == '1':
            print("Programa encerrado.")
            break
        elif stop != '2':
            print("Opção inválida. Continuando...")


if __name__ == "__main__":
     main()

            
