time = list()
dados = dict()
partidas= list()


while True:
    dados.clear()
    dados['nome']= str(input('Nome do Jogador: '))
    tot=int(input(f'Quantas partidas {dados["nome"]} Jogou ? '))
    partidas.clear()
    for c in range(0,tot):
        partidas.append(int(input(f'      Quantos gols na partida {c} ? ')))
        dados['gols'] = partidas[:]
        dados['total'] = sum(partidas)
    time.append(dados.copy())
    while True:
        pergunta = str(input('Quer Coontinuar ?  [S/N] ')).upper() [0]
        if pergunta in 'SN':
            break
        print('ERRO! POR FAVOR , DIGITE APENAS S ou N')
    if pergunta == 'N':
        break # leitura de dados dos jogadores
print('--' * 30) # Analise de dados#
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('--' * 30)
for k , v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('--' * 30)
while True:
    busca = int(input('Mostrar os dados de qual jogador? (digite 999 para PARAR!) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não encontramos o jogador com o código {busca}')
    else:
        print(f'  --- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca] ['gols']):
            print(f'     No jogo {i+1} fez {g} gols.')
    print('--' * 30)
print('---VOLTE SEMPRE! ---')        



