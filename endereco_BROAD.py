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

enderecoIP = input("Digite o IP: ")
enderecoMASK = input("Digite o endereço BROADCAST: ")

converter_ip = binarizator(enderecoIP)
converter_maskara = binarizator(enderecoMASK)

inverter_mascara = araksam(converter_maskara)

print(inverter_mascara)

# falta só fazer o OR ENTRE A MASCARA E O IP