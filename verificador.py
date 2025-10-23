def pertence_a_rede(rede,ip,broadcast):
    
    if rede <= ip <= broadcast:
        validade = True
    else:
        validade = False

    return validade
    # verifica se o ip está entre a rede e o broadcast