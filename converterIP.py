enderecoIP = input("Digite o endereço ip: ")

octetos = enderecoIP.split('.')

IPbinario = []

for partes in octetos:

    parte_int = int(partes)
    binarizador = bin(parte_int)
    purificador = binarizador[2:]
    complemento = purificador.zfill(8)

    IPbinario.append(complemento)

print(IPbinario)
    