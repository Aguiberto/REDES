from IPAddress import ipv4_adress

if __name__ == "__main__":
    ip = input("Digite o IP: ")
    mascara = input("Informe a mascara: ")

calculo = ipv4_adress(ip,mascara)
