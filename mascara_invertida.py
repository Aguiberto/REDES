# receber e transformar a máscara para binário

mask = input("Digite a máscara de rede: ")

octetos = mask.split('.')

mask_bin = []

for parte in octetos:
    oct_int = int(parte)
    binarizador = bin(oct_int)
    recorte = binarizador[2:]
    complemento = recorte.zfill(8)

    mask_bin.append(complemento)
    # a máscara sai no formato STR

print(f"A máscara é: {mask_bin}")

# Converter a mascara para INT

mask_bin_int = []

for i in mask_bin:
    parte_int = int(i,2)
    mask_bin_int.append(parte_int)

print(f" Tipo de dado em Mask_bin_int é :{type(mask_bin_int[0])}")

# Inverter a mascara

mask_invertida = []
fator_de_inversao = 0b11111111

for j in range(4):

    xor  = fator_de_inversao ^ mask_bin_int[j]
    mask_invertida.append(bin(xor)[2:].zfill(8))
    # saída é do tipo STR

print(mask_invertida)
