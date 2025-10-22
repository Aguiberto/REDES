enderecoBROAD = input("Informe a MASCARA de REDE: ")

octetos = enderecoBROAD.split('.')

mask_binario = []

for parte in octetos:

    oct_int = int(parte)
    binarizador = bin(oct_int)
    purificador = binarizador[2:]
    complemento = purificador.zfill(8)


    mask_binario.append(complemento)

print (mask_binario)
print(type(mask_binario))
print(type(mask_binario[0]))