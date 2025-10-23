class ipv4_adress:

    def __init__(self,endereco_ip,endereco_mask):
    # redefine todas as variáveis

        self.endereco_ip = endereco_ip
        self.endereco_mask = endereco_mask

        self.ip_convertido = self.binarizator(endereco_ip)
        self.mask_invertida = self.binarizator(endereco_mask)

        self.rede = self.calcular_rede()
        self.broadcast = self.calcular_broadcast()

    def binarizator(self, enderecoIPV4):

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

    def araksam (self,mask):

    # Inverter a mascara
    mask_invertida = []
    fator_de_inversao = 0b11111111

    for j in range(4):

        xor  = fator_de_inversao ^ mask[j]
        mask_invertida.append(xor)

    return mask_invertida
    # retorna máscara em com o complemento binário em inteiro
    # exemplo [0.0.0.255]

    def calcular_rede(self):

    enderecoREDE = []
    # variável que terá o endereço de rede

    # realiza AND BITWISE 
    for i in range(4):
        enderecoREDE.append(self.converter_ip[i] & converter_maskara[i])

    return enderecoREDE

    def calcular_broadcast(self):
    inverter_mascara = araksam(self.converter_maskara)

    # realizando OR BITWISE

    enderecoBROAD = []
    # ENDEREÇO BROADCAST
    for l in range(4):
        fazendo_or = converter_ip[l] | inverter_mascara[l]
        enderecoBROAD.append(fazendo_or)

    return enderecoBROAD

    def formatador(self):

    rede_str = []
    broad_str =[]

    for m in range(4):

    alterador_rede = str(self.enderecoREDE[m])
    alterador_broad = str(self.enderecoBROAD[m])

    rede_str.append(alterador_rede)
    broad_str.append(alterador_broad)

    rede_formatada = '.'.join(rede_str)
    broad_formatado = '.'.join(broad_str)

    return rede_formatada, broad_formatado

    def cidr(self):

    conta_um = 0
     # cdri

    for n in self.converter_maskara: ####### OBSERVAR#########
    conta_um += bin(n).count('1')

    return conta_um
   
    
    def apresentar(self):
    
    rede_formatada,broad_formatado = self.formatador()
    cidr_valor = self.cidr()
    pertence = sel.pertence_a_rede()

    print(f"Endereço IPv4 CIDR: {self.enderecoIP}/{cidr_valor}")
    print(f"Seu enderede de REDE é: {rede_formatada}")
    print(f"Seu endereço BROADCAST é: {broad_formatado}")

    def pertence_a_rede(self, rede,ip,broadcast):
    
    if self.rede <= self.ip <= self.broadcast:
        validade = True
    else:
        validade = False

    return validade
    # verifica se o ip está entre a rede e o broadcast