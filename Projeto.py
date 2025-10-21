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

def araksam (mask):

    # Inverter a mascara
    mask_invertida = []
    fator_de_inversao = 0b11111111

    for j in range(4):

        xor  = fator_de_inversao ^ mask[j]
        mask_invertida.append(xor)

    return mask_invertida

# ----------------------- RECEBENDO AS ENTRADAS ---------------------------------
enderecoIP = input("Digite o endereço IP: ")
enderecoMASK = input("Digite o endereço BROADCAST: ")

converter_ip = binarizator(enderecoIP)
converter_maskara = binarizator(enderecoMASK)

# ----------------------- CALCULO DA REDE ---------------------------------------

enderecoREDE = []
#variável que recebe o endereço de rede

# realiza AND BITWISE 
for i in range(4):
    enderecoREDE.append(converter_ip[i] & converter_maskara[i])

print(f"O endereço de REDE É: {enderecoREDE}")
# ENDEREÇO DE REDE

# --------------------------- ENDEREÇO BROADCAST --------------------------------

inverter_mascara = araksam(converter_maskara)

# realizando OR BITWISE

enderecoBROAD = []
# ENDEREÇO BROADCAST
for l in range(4):
    fazendo_or = converter_ip[l] | inverter_mascara[l]
    enderecoBROAD.append(fazendo_or)

print(f"Seu endereço BROADCAST é: {enderecoBROAD}")

# ---------------------------- VEFIRICAÇÃO DE VALIDADE DE REDE -----------------------

# comparar se o endeço ip está entre o endereço de rede eo endereço BROADCAST
# verficar octeto por octeto

validade = False

for m in range (4):
    if (enderecoIP[m] <= enderecoREDE[m]) or (enderecoIP[m] >= enderecoBROAD[m]):
        validade = True

print(f"Validade do IP: {validade}")