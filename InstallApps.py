import os

def menu():
    
    print("\n-------------------")
    print("MENU DE INSTALAÇÕES")
    print("-------------------\n")
    print("1 - Instalar todos os aplicativos\n")
    print("2 - Instalar aplicativo especifíco\n")
    print("3 - Sair\n")
    
    op = int(input("Digite a opção desejada: "))

    os.system("cls")

    if op == 1:
        
        ins_todos()
        
    elif op == 2:
        
        ins_exp()
        
    elif op == 3:
        
        print("\nSaindo...\n")
        os.system("pause")
    
    else:
        
        print("\nOpção inválida!\n")
        os.system("pause")
        os.system("cls")
        menu()
    
def ins_todos():
    
    print("\nInstalando todos os aplicativos...\n")
    os.system("teste.exe")
    print("\n")
    os.system("pause")    
    os.system("cls")
    menu()
        
    
def ins_exp():
    
    os.system("cls")
    
    print("\n---------------------------")
    print("Aplicativos para instalação")
    print("---------------------------\n")
    print("1 - Teste 1\n")
    print("2 - Teste 2\n")
    print("3 - Teste 3\n")
    print("4 - Retornar\n")
    print("---------------------------\n")

    op_e = int(input("Digite a opção desejada: "))
    os.system("cls")
    
    if op_e == 1:
        
        print("\nInstalando Teste 1...\n")
        os.system("teste1.exe")
        print("\n")
        os.system("pause")
        os.system("cls")
        ins_exp()
        
    elif op_e == 2:
        
        print("\nInstalando Teste 2...\n")
        os.system("teste2.exe")
        print("\n")
        os.system("pause")
        os.system("cls")
        ins_exp()
    
    elif op_e == 3:
        
        print("\nInstalando Teste 3...\n")
        os.system("teste3.exe")
        print("\n")
        os.system("pause")
        os.system("cls")
        ins_exp()
        
    elif op_e == 4:
        
        os.system('cls')
        menu()
        
    else:
        
        print("\nOpção inválida!\n")
        os.system("pause")
        os.system("cls")
        ins_exp()
        
menu()