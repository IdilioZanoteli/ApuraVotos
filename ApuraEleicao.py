import json

listacandidatos = list(())

try:
    with open('eleicao.bin', 'rb') as file:
        for line in file:
            candidato = json.loads(line)
            listacandidatos.append(candidato['cod'])
except:
    pass

print("        Sistema Eleição       \n"
      "Bem vindo ao Sistema de Gerenciamento Eleitoral")

menu = {}
menu['1'] = "Adicionar Candidato"
menu['2'] = "Visualisar Resultado"
menu['3'] = "Sair"

while True:
    opcao = menu.keys()
    for entrada in opcao:
        print(entrada, menu[entrada])

    selecao = input("Selecione a Opção:")
    if selecao == '1':

        while True:
            totalVotos = 0
            print("Digite o Codigo do Candidato:")
            cand = input()
            if cand in listacandidatos:
                print("Candidato já cadastrado")
                break
            print("Digite o Nome do Candidato")
            nome = input()
            print("Digite o Cargo do Candidato")
            cargo = input()
            print("Digite a Quantidade de votos na Região Centro")
            votosCentro = int(input())
            print("Digite a Quantidade de votos na Região Sul")
            votosSul = int(input())
            print("Digite a Quantidade de Votos na Região Norte:")
            votosNorte = int(input())
            totalVotos = votosCentro+votosSul+votosNorte
            candidato = dict(cod=cand, nome=nome, cargo=cargo,
                             votosCentro=votosCentro, votosSul=votosSul, votosNorte=votosNorte, totalVotos=totalVotos)

            with open('eleicao.bin', 'ab') as file:
                x = json.dumps(candidato)
                file.write(bytearray(x, 'utf-8'))
                file.write(bytearray('\n', 'utf-8)'))
            print("Deseja Cadastrar Outro Candidato? Digite S ou N")
            if input() == 'N'or'n':
                break

    elif selecao == '2':
        menu2 = {}
        menu2['1'] = "Listar Candidatos "
        menu2['2'] = "Votos por Candidato"
        menu2['3'] = "Votos Totais por Candidato"
        menu2['4'] = "Votos por Região"
        menu2["5"] = "Voltar ao Menu Anterior"

        while True:
            opcao = menu2.keys()
            for entrada in opcao:
                print(entrada, menu2[entrada])

            selecao = input("Selecione a Opção:")
            if selecao == '1':
                print("Lista de Candidatos:")
                with open('eleicao.bin', 'rb') as file:
                    for line in file:
                        candidato = json.loads(line)
                        print('Codigo:'+candidato['cod']+'  Nome:' +
                              candidato['nome']+'  Cargo:'+candidato['cargo'])
                input('Pressione Enter para voltar para o Menu')

            elif selecao == '2':
                print('Votos por Candidato')
                with open('eleicao.bin', 'rb') as file:
                    for line in file:
                        candidato = (json.loads(line))
                        print('Codigo: '+candidato['cod']+'  Nome:  '+candidato['nome'] +
                              '  Cargo: '+candidato['cargo']+'  Votos Totais: '+str(candidato['totalVotos']))
                input('Pressione Enter para voltar para o Menu')

            elif selecao == '3':
                print('Votos Totais por Candidato')
                print('Digite o código do candidato a ser consultado:')
                cand = input()
                with open('eleicao.bin', 'rb') as file:
                    for line in file:
                        candidato = json.loads(line)
                        if candidato['cod'] == cand:
                            print(
                                'Codigo:'+candidato['cod']+'  Nome:'+candidato['nome']+'  Cargo:'+candidato['cargo'])
                            print("Votos Região Centro: "+str(candidato['votosCentro'])+'\n' +
                                  "Votos Região Norte: "+str(candidato['votosNorte'])+'\n' +
                                  "Votos Região Sul: "+str(candidato['votosSul']))
                input('Pressione Enter para voltar para o Menu')

            elif selecao == '4':
                votosCentro, votosNorte, votosSul = 0, 0, 0
                print('Votos por Região')
                with open('eleicao.bin', 'rb') as file:
                    for line in file:
                        candidato = json.loads(line)
                        votosCentro = votosCentro + \
                            int(candidato['votosCentro'])
                        votosNorte = votosNorte + int(candidato['votosNorte'])
                        votosSul = votosSul + int(candidato['votosSul'])

                print("Quantidade de votos na Região Centro: "+str(votosCentro))

                print("Quantidade de votos na Região Sul: "+str(votosSul))

                print("Quantidade de Votos na Região Norte: "+str(votosNorte))

                input('Pressione Enter para voltar para o Menu')

            elif selecao == '5':
                break

            else:
                print("Opção Inválida")
                input('Pressione Enter para voltar para o Menu')

    elif selecao == '3':
        break

    else:
        print("Opção Inválida")
        input('Pressione Enter para voltar para o Menu')
