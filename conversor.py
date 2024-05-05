import os, time

def mostrar_info():
    print("Seja bem-vindo!! Digite 'info' para ter as informações sobre o projeto.\n\n")
    print('*CONVERSOR DE NÚMEROS*\n')

def voltar_ao_menu():
    input("\nPressione qualquer tecla para voltar ao menu de conversão...")
    os.system('cls')  

while True:
    mostrar_info()

    escolha = input(' A.BINÁRIO\n B.HEXADECIMAL\n C.OCTADECIMAL\n Qual conversão deseja realizar (digite a palavra chave "F" para finalizar o sistema): ')
    escolha = escolha.upper()

    if escolha == 'A' or escolha == 'A.DECIMAL' or escolha == 'DECIMAL':
        def dec_bin_int():
            os.system('cls')
            numero = int(input('Digite um número decimal: '))
            num = []
            a = ''
            cont = 0
            while numero > 0:
                num.append(numero % 2)
                numero = numero // 2
                cont += 1
            num.reverse()
            for i in range(cont):
                a += str(num[i])
            print('Seu número em Binário é:', a)
            time.sleep(2)
            voltar_ao_menu()

        dec_bin_int()
    elif escolha == 'B' or escolha == 'B.HEXADECIMAL' or escolha == 'HEXADECIMAL':
        def dec_hex_int():
            os.system('cls')
            numero = int(input('Digite um número decimal: '))
            num = []
            a = ''
            cont = 0
            while numero > 0:
                num.append(numero % 16)
                numero = numero // 16
                cont += 1
            num.reverse()
            for i in range(cont):
                a += str(num[i])
            print('Seu número em Hexadecimal é:', a)
            time.sleep(2)
            voltar_ao_menu()

        dec_hex_int()

    elif escolha == 'C':
        os.system('cls')
        def dec_octa_int():
            numero = int(input('Digite um número decimal: '))
            num = []
            a = ''
            cont = 0
            while numero > 0:
                num.append(numero % 8)
                numero = numero // 8
                cont += 1
            num.reverse()
            for i in range(cont):
                a += str(num[i])
            print('Seu número em Octadecimal é:', a)
            voltar_ao_menu()

        dec_octa_int()
        
    elif escolha == 'INFO':
        os.system('cls')
        print("Curso: Análise e Desenvolvimento de Sistemas\n\nDiciplinas envolvidas: Progrmação de Computadores e Organização e Arquitetura de Computadores\n\n******\nMembros do grupo\n******\n\n31449638 - GUSTAVO HENRIQUE RODRIGUES\n32601000 - MARLON SANTOS DE SOUZA\n31704948 - NATHAN LIMA PORTERO\n31518494 - PEDRO LUCAS BASTOS DOS SANTOS \n31294260 - VICTOR CARÚS DE MELO\n\nVersion: 1.2.0")
        voltar_ao_menu()
    
    elif escolha == 'F':
        print('Obrigado por usar nosso sistema!!')
        break
    else:
        print("Opção inválida. Por favor, escolha A, B, C ou F.")
        voltar_ao_menu()
