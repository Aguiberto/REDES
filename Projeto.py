def binarizator(enderecoIPV4):

    octetos = enderecoIPV4.split('.')

    IPV4binario = []

    for partes in octetos:

        parte_int = int(partes)
        binarizador = bin(parte_int)
        purificador = binarizador[2:]
        complemento = purificador.zfill(8)

        IPV4binario.append(complemento)

    return (IPV4binario)


ip = input("Digite o endereço IP: ")

broadcast = input("Digite o endereço BROADCAST: ")

ipconvertido = binarizator(ip)
broadconvertido = binarizator(broadcast)

print(ipconvertido)
print(broadconvertido)

    