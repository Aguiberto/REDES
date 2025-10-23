def binarizator(enderecoIPV4):

    octetos = enderecoIPV4.split('.')

    IPV4binario = []
    int_IPV4binario = []

    for partes in octetos:

        parte_int = int(partes)
        binarizador = bin(parte_int)
        purificador = binarizador[2:]
        complemento = purificador.zfill(8)

        IPV4binario.append(complemento)
    
    for binarios in IPV4binario:

        interizador = int(binarios,2)

        int_IPV4binario.append(interizador)

    return (int_IPV4binario)
    # retorna uma lista de int

def araksam (mask):

    # Inverter a mascara
    mask_invertida = []
    fator_de_inversao = 0b11111111

    for j in range(4):

        xor  = fator_de_inversao ^ mask[j]
        mask_invertida.append(xor)

    return mask_invertida
    # retorna máscara em com o complemento binário em inteiro
    # exemplo [0.0.0.255]

def pertence_a_rede(rede,ip,broadcast):
    
    if rede <= ip <= broadcast:
        validade = True
    else:
        validade = False

    return validade
    # verifica se o ip está entre a rede e o broadcast


# ----------------------- RECEBENDO AS ENTRADAS ---------------------------------
enderecoIP = input("Digite o endereço IP: ")
enderecoMASK = input("Digite o endereço BROADCAST: ")

converter_ip = binarizator(enderecoIP)
converter_maskara = binarizator(enderecoMASK)

# ----------------------- CALCULO DA REDE ---------------------------------------

enderecoREDE = []
# variável que terá o endereço de rede

# realiza AND BITWISE 
for i in range(4):
    enderecoREDE.append(converter_ip[i] & converter_maskara[i])


# --------------------------- ENDEREÇO BROADCAST --------------------------------

inverter_mascara = araksam(converter_maskara)

# realizando OR BITWISE

enderecoBROAD = []
# ENDEREÇO BROADCAST
for l in range(4):
    fazendo_or = converter_ip[l] | inverter_mascara[l]
    enderecoBROAD.append(fazendo_or)

#--------------------- MOSTRAND OS RESULTADOS ----------------------------------------
rede_str = []
broad_str =[]

for m in range(4):

    alterador_rede = str(enderecoREDE[m])
    alterador_broad = str(enderecoBROAD[m])

    rede_str.append(alterador_rede)
    broad_str.append(alterador_broad)


conta_um = 0
for n in converter_maskara:
    conta_um += bin(n).count('1')
# cdri

rede_formatada = '.'.join(rede_str)
broad_formatado = '.'.join(broad_str)

print(f"Endereço IPv4 CIDR: {enderecoIP}/{conta_um}")
print(f"Seu enderede de REDE é: {rede_formatada}")
print(f"Seu endereço BROADCAST é: {broad_formatado}")

# ---------------------- VALIDAÇÃO IP --------------------------------------------

validacao = pertence_a_rede(enderecoREDE,converter_ip,enderecoBROAD)

print(f"Validade : {validacao}")