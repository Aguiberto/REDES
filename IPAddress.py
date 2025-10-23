class IPv4_adress:

    def __init__(self,endereco_ip,endereco_mask):
    # redefine todas as variáveis

        self.endereco_ip = endereco_ip
        self.endereco_mask = endereco_mask

        self.ip_convertido = self.binarizator(endereco_ip)
        self.converter_maskara = self.binarizator(endereco_mask)

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
            enderecoREDE.append(self.ip_convertido[i] & self.converter_maskara[i])

        return enderecoREDE

    def calcular_broadcast(self):

        inverter_mascara = self.araksam(self.converter_maskara)

        # realizando OR BITWISE

        enderecoBROAD = []
        # ENDEREÇO BROADCAST
        for l in range(4):
            fazendo_or = self.ip_convertido[l] | inverter_mascara[l]
            enderecoBROAD.append(fazendo_or)

        return enderecoBROAD

    def formatador(self):

        rede_str = []
        broad_str =[]

        for m in range(4):

            alterador_rede = str(self.rede[m])
            alterador_broad = str(self.broadcast[m])

            rede_str.append(alterador_rede)
            broad_str.append(alterador_broad)

        rede_formatada = '.'.join(rede_str)
        broad_formatado = '.'.join(broad_str)

        return rede_formatada, broad_formatado

    def cidr(self):

        conta_um = 0
        # cdri

        for n in self.converter_maskara: 
            conta_um += bin(n).count('1')

        return conta_um

    def pertence_a_rede(self):
        def ip_para_int(lista):
            valor = (lista[0] << 24) + (lista[1] << 16) + (lista[2] << 8) + lista[3]
            return valor

        rede_int = ip_para_int(self.rede)
        ip_int = ip_para_int(self.ip_convertido)
        broad_int = ip_para_int(self.broadcast)

        if rede_int <= ip_int <= broad_int:
            validade = True
        else:
            validade = False

        return validade
        # verifica se o ip está entre a rede e o broadcast

    def apresentar(self):
    
        rede_formatada,broad_formatado = self.formatador()
        cidr_valor = self.cidr()
        pertence = self.pertence_a_rede()

        print(f"Endereço IPv4 CIDR: {self.endereco_ip}/{cidr_valor}")
        print(f"Seu enderede de REDE é: {rede_formatada}")
        print(f"Seu endereço BROADCAST é: {broad_formatado}")
        print(f"Pertence à rede: {pertence}")
