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


ip = input("Digite o endereço IP: ")

broadcast = input("Digite o endereço BROADCAST: ")

ipconvertido = binarizator(ip)
broadconvertido = binarizator(broadcast)

bitwise = []
for i in range(4):
    bitwise.append(ipconvertido[i] & broadconvertido[i])

print(bitwise)

    