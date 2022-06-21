import model


def valido_letra (letra):
    if letra in model.filas:
        return True


def valido_numero(letra, numero):
    if int(numero) < 0:
        return False

    elif letra in model.filas_especiais and numero in model.numero_nao_lugarFA:
        return False

    elif numero in model.numero_lugar:

        return True

    else:
        if int(numero) > 14:
            return False 


def Validar_data(data):
    if data in model.Datas == True:
        return True


def verificar_lugares_reservados(letra, numero, data):
    lugares = letra + numero + data
    if lugares in model.Lugares_reservados27 or lugares in model.Lugares_reservados12 or lugares in model.Lugares_reservados29 or lugares in model.Lugares_reservados10 or lugares in model.Lugares_reservados13 or lugares in model.Lugares_VIP_Reservado27 or lugares in model.Lugares_VIP_Reservado12 or lugares in model.Lugares_VIP_Reservado29 or lugares in model.Lugares_VIP_Reservado10 or lugares in model.Lugares_VIP_Reservado13:
        return False
    else:
        return True


def reservar_lugares(letra, numero, data):
    lugares = letra + numero + data
    if data == "27/07/2022" and numero in model.numero_VIP and letra in model.filas_especiais and verificar_lugares_reservados(letra, numero, data) == True:  
        model.Lugares_VIP_Reservado27.append(lugares)

    elif data == "12/08/2022" and numero in model.numero_VIP and letra in model.filas_especiais and verificar_lugares_reservados(letra, numero, data) == True:
        model.Lugares_VIP_Reservado12.append(lugares)

    elif data == "29/09/2022" and numero in model.numero_VIP and letra in model.filas_especiais and verificar_lugares_reservados(letra, numero, data) == True: 
        model.Lugares_VIP_Reservado29.append(lugares)

    elif data == "10/01/2023" and numero in model.numero_VIP and letra in model.filas_especiais and verificar_lugares_reservados(letra, numero, data) == True: 
        model.Lugares_VIP_Reservado10.append(lugares)

    elif data == "13/02/2023" and numero in model.numero_VIP and letra in model.filas_especiais and verificar_lugares_reservados(letra, numero, data) == True:
        model.Lugares_VIP_Reservado13.append(lugares)

    elif data == "27/07/2022" and verificar_lugares_reservados(letra, numero, data) == True:
        model.Lugares_reservados27.append(lugares)

    elif data == "12/08/2022" and verificar_lugares_reservados(letra, numero, data) == True:
        model.Lugares_reservados12.append(lugares)
    
    elif data == "29/09/2022" and verificar_lugares_reservados(letra, numero, data) == True:
        model.Lugares_reservados29.append(lugares)
    
    elif data == "10/01/2023" and verificar_lugares_reservados(letra, numero, data) == True:
        model.Lugares_reservados10.append(lugares)

    elif data == "13/02/2023" and verificar_lugares_reservados(letra, numero, data) == True:
        model.Lugares_reservados13.append(lugares)
    

def eliminar_lugar_reservado(letra, numero, data):
    lugares = letra + numero + data
    if data == "27/07/2022" and numero in model.numero_VIP and letra in model.filas_especiais and verificar_lugares_reservados(letra, numero, data) == False:  
        model.Lugares_VIP_Reservado27.remove(lugares)

    elif data == "12/08/2022" and numero in model.numero_VIP and letra in model.filas_especiais and verificar_lugares_reservados(letra, numero, data) == False:
        model.Lugares_VIP_Reservado12.remove(lugares)

    elif data == "29/09/2022" and numero in model.numero_VIP and letra in model.filas_especiais and verificar_lugares_reservados(letra, numero, data) == False: 
        model.Lugares_VIP_Reservado29.remove(lugares)

    elif data == "10/01/2023" and numero in model.numero_VIP and letra in model.filas_especiais and verificar_lugares_reservados(letra, numero, data) == False: 
        model.Lugares_VIP_Reservado10.remove(lugares)

    elif data == "13/02/2023" and numero in model.numero_VIP and letra in model.filas_especiais and verificar_lugares_reservados(letra, numero, data) == False:
        model.Lugares_VIP_Reservado13.remove(lugares)

    elif data == "27/07/2022" and verificar_lugares_reservados(letra, numero, data) == False:
        model.Lugares_reservados27.remove(lugares)

    elif data == "12/08/2022" and verificar_lugares_reservados(letra, numero, data) == False:
        model.Lugares_reservados12.remove(lugares)
    
    elif data == "29/09/2022" and verificar_lugares_reservados(letra, numero, data) == False:
        model.Lugares_reservados29.remove(lugares)
    
    elif data == "10/01/2023" and verificar_lugares_reservados(letra, numero, data) == False:
        model.Lugares_reservados10.remove(lugares)

    elif data == "13/02/2023" and verificar_lugares_reservados(letra, numero, data) == False:
        model.Lugares_reservados13.remove(lugares)
        

def contar_valor(data):
    if data == "27/07/2022":
        valorVIP = len(model.Lugares_VIP_Reservado27) * 12 
        valor = len(model.Lugares_reservados27) * 4
        print(f"\nValor da bilheteira é: {valor + valorVIP}€.\n")

    elif data == "12/08/2022":
        valorVIP = len(model.Lugares_VIP_Reservado12) * 12 
        valor = len(model.Lugares_reservados12) * 4
        print(f"\nValor da bilheteira é: {valor + valorVIP}€.\n")
    
    elif data == "29/09/2022":
        valorVIP = len(model.Lugares_VIP_Reservado29) * 12 
        valor = len(model.Lugares_reservados29) * 4
        print(f"\nValor da bilheteira é: {valor + valorVIP}€.\n")

    elif data == "10/01/2023":
        valorVIP = len(model.Lugares_VIP_Reservado10) * 12 
        valor = len(model.Lugares_reservados10) * 4
        print(f"\nValor da bilheteira é: {valor + valorVIP}€.\n")

    elif data == "13/02/2023":
        valorVIP = len(model.Lugares_VIP_Reservado13) * 12 
        valor = len(model.Lugares_reservados13) * 4
        print(f"\nValor da bilheteira é: {valor + valorVIP}€.\n")

    elif data == "07/22":
        valorVIP = len(model.Lugares_VIP_Reservado27) * 12 
        valor = len(model.Lugares_reservados27) * 4
        print(f"\nValor da bilheteira é: {valor + valorVIP}€.\n")

    elif data == "08/22":
        valorVIP = len(model.Lugares_VIP_Reservado12) * 12 
        valor = len(model.Lugares_reservados12) * 4
        print(f"\nValor da bilheteira é: {valor + valorVIP}€.\n")

    elif data == "09/22":
        valorVIP = len(model.Lugares_VIP_Reservado29) * 12 
        valor = len(model.Lugares_reservados29) * 4
        print(f"\nValor da bilheteira é: {valor + valorVIP}€.\n")

    elif data == "01":
        valorVIP = len(model.Lugares_VIP_Reservado10) * 12 
        valor = len(model.Lugares_reservados10) * 4
        print(f"\nValor da bilheteira é: {valor + valorVIP}€.\n")

    elif data == "02":
        valorVIP = len(model.Lugares_VIP_Reservado13) * 12 
        valor = len(model.Lugares_reservados13) * 4
        print(f"\nValor da bilheteira é: {valor + valorVIP}€.\n")

    elif data == "2022":
        valorvip27 = len(model.Lugares_VIP_Reservado27)
        valorvip12 = len(model.Lugares_VIP_Reservado12)
        valorvip29 = len(model.Lugares_VIP_Reservado29)

        valor27 = len(model.Lugares_reservados27)
        valor12 = len(model.Lugares_reservados12)
        valor29 = len(model.Lugares_reservados29)
        valor = ((valorvip27 + valorvip12 + valorvip29) * 12 + (valor27 + valor12 + valor29) * 4)
        print(f"\nValor da bilheteira é: {valor}€.\n")
    
    elif data == "2023":
        valorvip10 = len(model.Lugares_VIP_Reservado10)
        valorvip13 = len(model.Lugares_VIP_Reservado13)
       
        valor10 = len(model.Lugares_reservados10)
        valor13 = len(model.Lugares_reservados13)
       
        valor = ((valorvip10 + valorvip13) * 12 + (valor10 + valor13) * 4)
        print(f"\nValor da bilheteira é: {valor}€.\n")

    #   MTMT  ##
