import model
import controller

print("\n Seja Bem-vindo ao teatro. \n")
print(f"As datas dos espetáculos são: {model.Datas}\n")
print("\n Escolha um lugar vago. \n")



print(model.numero_lugaresK)
print(model.numero_lugaresJ)
print(model.numero_lugaresI)
print(model.numero_lugaresH)
print(model.numero_lugaresG)
print(model.numero_lugaresF)
print(model.numero_lugaresE)
print(model.numero_lugaresD)
print(model.numero_lugaresC)
print(model.numero_lugaresB)
print(model.numero_lugaresA)
print(model.Palco)

print("\nInsira os comandos RL(para reservar lugar), ER(para eliminar reserva), AR(alterar reserva) e CVB(para consultar o valor da bilheteira).\n")
def main ():
    while True:
        try:
            comandos = input().split(" ")
        except EOFError:
            return
    
        
        if comandos [0] == "RL": #RL -> reservar lugar na sala   
            letra = input("Digite a letra da fila desejada: ")
            numero = input("Digite o numero do lugar desejado: ")
            data = input("Insira a data do espetáculo desejada(dd/mm/aaaa): ")

            while controller.valido_letra(letra) == False:
                print("Letra da fila inválida.")
                letra = input("Digite a letra da fila desejada novamente: ")

            while controller.valido_numero(letra, numero) == False:
                print("Número do lugar inválido.")
                numero = input("Digite o número do lugar desejado novamente: ")
            
            while controller.Validar_data(data) == False:
                print("Data inválida.")
                data = input("Insira a data do espetáculo desejada novamente(dd/mm/aaaa): ")
            
            if controller.verificar_lugares_reservados(letra, numero, data) == True:
                controller.reservar_lugares(letra, numero, data)
                print("\nLugar registado com sucesso.\n")
            else:
                print("\nLugar já se encontra reservado, insira o comando (RL) para reservar lugar novamente.\n")
                
                

        if comandos[0] == "ER": #ER -> Eliminar reserva
            print("\n Escolha um lugar ocupado. \n")
            letra = input("Digite a letra da fila desejada: ")
            numero = input("Digite o numero do lugar desejado: ")
            data = input("Insira a data do espetáculo desejada(dd/mm/aaaa): ")

            while controller.valido_letra(letra) == False:
                print("Letra da fila inválida.")
                letra = input("Digite a letra da fila desejada novamente: ")

            while controller.valido_numero(letra, numero) == False:
                print("Número do lugar inválido.")
                numero = input("Digite o número do lugar desejado novamente: ")

            while controller.Validar_data(data) == False:
                print("Data inválida.")
                data = input("Insira a data do espetáculo desejada novamente(dd/mm/aaaa): ")
            
                                                    
            if controller.verificar_lugares_reservados(letra, numero, data) == False:
                controller.eliminar_lugar_reservado(letra, numero, data)
                print("\nLugar eliminado com sucesso.\n")
            else:
                print("\nLugar não se encontra reservado.\n")
                print("Insira o comando (RL) para reservar um lugar.")


        if comandos[0] == "AR": #AR -> Alterar reserva
            print("\n Escolha um lugar a alterar. \n")
            letra = input("Digite a letra da fila que pretende alterar: ")
            numero = input("Digite o numero do lugar que pretende alterar: ")
            data = input("Insira a data do espetáculo que pretende alterar(dd/mm/aaaa): ")

            while controller.valido_letra(letra) == False:
                print("Letra da fila inválida.")
                letra = input("Digite a letra da fila desejada novamente: ")

            while controller.valido_numero(letra, numero) == False:
                print("Número do lugar inválido.")
                numero = input("Digite o número do lugar desejado novamente: ")

            while controller.Validar_data(data) == False:
                print("Data inválida.")
                data = input("Insira a data do espetáculo desejada novamente(dd/mm/aaaa): ")

            if controller.verificar_lugares_reservados(letra, numero, data) == False:
                controller.eliminar_lugar_reservado(letra, numero, data)
                print("\nLugar eliminado com sucesso.\n")
            else:
                print("\nLugar não se encontra reservado.\n")


            print("\n Escolha o seu novo lugar. \n")

            letrab = input("Digite a letra da fila desejada: ")
            numerob = input("Digite o numero do lugar desejado: ")
            datab = input("Insira a data do espetáculo desejada(dd/mm/aaaa): ")

            while controller.valido_letra(letrab) == False:
                print("Letra da fila inválida.")
                letrab = input("Digite a letra da fila desejada novamente: ")

            while controller.valido_numero(letrab, numerob) == False:
                print("Número do lugar inválido.")
                numerob = input("Digite o número do lugar desejado novamente: ")

            while controller.Validar_data(datab) == False:
                print("Data inválida.")
                datab = input("Insira a data do espetáculo desejada novamente(dd/mm/aaaa): ")
                                                    
            if controller.verificar_lugares_reservados(letrab, numerob, datab) == True:
                controller.reservar_lugares(letrab, numerob, datab)
                print("\nLugar alterado com sucesso.\n")
            else:
                print("\nLugar já se encontra reservado, insira o comando (RL) para reservar lugar novamente.\n")



        if comandos[0] == "CVB": #CVB -> Consultar valor da bilheteira
            print(f"As datas dos espetáculos são: {model.Datas}\n")
            dado = input("Digite o que quer consultar o valor(dia, mes , ano): ")
            if dado == "dia":   
                data = input(f"Que dia pretende consultar{model.Datas}?: ")    
                controller.contar_valor(data)
            elif dado == "mes":
                data = input(f"Que mes pretende consultar(07/22, 08/22, 09/22, 01/23, 02/23)?: ")   
                controller.contar_valor(data)
            elif dado == "ano":
                data = input(f"Que ano pretende consultar(2022, 2023)?: ")
                controller.contar_valor(data)

               
            
            
                


         ##############################################################################################################################

        if comandos[0] == "S": #S -> Sair
            print("\nObrigado por utilizar o nosso sistema de bilhetes.\n")
            break

        #   MTMT  ##