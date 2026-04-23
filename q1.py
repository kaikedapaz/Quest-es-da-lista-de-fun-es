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
qtd_mascaras_recuperadas = 0
qtd_seda_restante = 0
qtd_seda_gerada = 0
qtd_seda_utilizada = 0
seda_desperdicada = 0
vida_do_chefe = 140

#Função da ação de Hornet
def hornet_function():
    x = input()
    if x == "Ferrão":
        vida_do_chefe += -10
        if qtd_seda_restante + 2 < 8:
            qtd_seda_restante += 2
            qtd_seda_gerada += 2
        return 1, vida_do_chefe, qtd_seda_restante, qtd_seda_gerada
    elif x == "Ataque de Seda" and qtd_seda_restante >= 3:
        vida_do_chefe += -20
        qtd_seda_restante += -3
        qtd_seda_utilizada += 3
        return 2, vida_do_chefe, qtd_seda_restante, qtd_seda_utilizada

    elif x == "Vincular" and qtd_seda_restante == 8:
        qtd_seda_restante += -8  
        qtd_seda_utilizada += 8
        qtd_inicial_mascaras = qtd_mascaras_restantes 
        if qtd_mascaras_restantes + 3 <= 5:
            qtd_mascaras_restantes += 3
        else:
            qtd_mascaras_restantes = 5
        return 3, qtd_seda_restante, qtd_seda_utilizada, qtd_mascaras_restantes


#Função da ação do chefão
def chefe_function():


#Função do sistema de batalha
def sistema_de_batalha():
    flag, _, _, _ = hornet_function()
    if flag == 1:
        _, vida_do_chefe, qtd_seda_restante, qtd_seda_gerada = hornet_function()
    elif flag == 2:
        _, vida_do_chefe, qtd_seda_restante, qtd_seda_utilizada = hornet_function()
    elif 

