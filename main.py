from IPAddress import IPv4_adress

if __name__ == "__main__":
    ip = input("Digite o IP: ")
    mascara = input("Informe a mascara: ")

calculo = IPv4_adress(ip,mascara)
calculo.apresentar()
