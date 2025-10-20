enderecoBROAD = input("Informe endereço BROADCAST: ")

octetos = enderecoBROAD.split('.')

BROADbinario = []

for parte in octetos:

    oct_int = int(parte)
    binarizador = bin(oct_int)
    purificador = binarizador[2:]
    complemento = purificador.zfill(8)


    BROADbinario.append(complemento)

print (BROADbinario)
