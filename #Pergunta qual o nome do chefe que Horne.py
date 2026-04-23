#Pergunta qual o nome do chefe que Hornet batalhará
nome_chefe = input()
if nome_chefe == "Tessela":
    print("Tessela: Ha Ha Ha! Parece que a aranha retornou.")
elif nome_chefe == "Grande Mãe Seda":
    print("Hornet: Monarca, seu reino de tirania acaba aqui!")
elif nome_chefe == "A Última Juíza":
    print("Hornet: Não posso recuar agora, a cidadela está logo ali.")
else:
    print(f"Hornet: {nome_chefe}, levante sua lâmina!")
print()

qtd_mascaras_restantes = 5
qtd_inicial_mascaras = 5
qtd_mascaras_recuperadas = 0
qtd_seda_restante = 0
qtd_seda_gerada = 0
qtd_seda_utilizada = 0
seda_desperdicada = 0
vida_do_chefe = 140

#Função da ação de Hornet
def ação_hornet(x, qtd_mascaras_restantes , qtd_inicial_mascaras, qtd_mascaras_recuperadas, qtd_seda_restante, qtd_seda_gerada, qtd_seda_utilizada, seda_desperdicada, vida_do_chefe):
    #Se for ferrão, tira-se dez pontos de vida do chefe e se a quantidade de seda no carretel for
    #menor do que 8 adicionamos 2 unidades nesse carretel.
    if x == "Ferrão":
        vida_do_chefe += -10
        if qtd_seda_restante + 2 < 8:
            qtd_seda_restante += 2
            qtd_seda_gerada += 2
    #Se a ação for ataque de seda, ela só vai acontecer se a quantidade de seda for maior ou igual a trẽs
    elif x == "Ataque de Seda" and qtd_seda_restante >= 3:
        vida_do_chefe += -20
        qtd_seda_restante += -3
        qtd_seda_utilizada += 3

    #Se a ação for vincular, serão gastas 8 unidades de seda no carretel 
    elif x == "Vincular" and qtd_seda_restante == 8:
        #-8 sedas no carretel
        qtd_seda_restante += -8  
        qtd_seda_utilizada += 8

        #Contando quantas máscaras haviam antes da recuperação de até 3 máscaras
        qtd_inicial_mascaras = qtd_mascaras_restantes 
        #Se a adição das três máscaras não der um número maior do que 5, então adicione as três máscaras
        if qtd_mascaras_restantes + 3 <= 5:
            qtd_mascaras_restantes += 3
        else:
        #Se der um número maior do que 5, então não adicione, e sim iguale a quantidade de máscaras a 5,
        #pois se fosse somado o 3 o limite de máscaras seria ultrapassado.
            qtd_mascaras_restantes = 5

        #Agora, a quantidade de máscaras recuperadas será igual a ela mesma + a diferença entre a 
        # quantidade de máscaras final e a quantidade inicial de máscaras. 
        # EX: qtd inicial sendo 4, a final 5, então recuperou-se apenas uma.
        qtd_mascaras_recuperadas += qtd_mascaras_restantes - qtd_inicial_mascaras
    #Durante o código, a cada seda gerada, adicionei valores à variável seda gerada e, a cada seda gasta, 
    # também contabilizei da mesma forma.
    seda_desperdicada = qtd_seda_gerada - qtd_seda_utilizada
    return qtd_mascaras_restantes, vida_do_chefe
        


def ação_chefe (y, qtd_mascaras_restantes):
    if y == "Acerto":
        qtd_mascaras_restantes += -1
    elif y == "Acerto Duplo":
        qtd_mascaras_restantes += -2
    #Em qualquer outro caso, o chefe errou, 
    # então a quantidade de máscaras não se altera.


def sistema_de_batalha ():
    x = input()
    qtd_mascaras_restantes, vida_do_chefe = ação_hornet(x, qtd_mascaras_restantes , qtd_inicial_mascaras, qtd_mascaras_recuperadas, qtd_seda_restante, qtd_seda_gerada, qtd_seda_utilizada, seda_desperdicada, vida_do_chefe)
    y = input()
    ação_chefe(y, qtd_mascaras_restantes)
    

while qtd_mascaras_restantes > 0 and vida_do_chefe > 0:
    sistema_de_batalha()
    

print("cabosse")

   