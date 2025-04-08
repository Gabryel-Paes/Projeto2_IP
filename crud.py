import os  # o modulo "os" verifica se o arquivo livros.txt existe no sistema antes de executar

arquivo = "livros.txt"

livros = []  # list e basicamente um vetor so q melhor aceita todo tipo de variavel
id = 1


def pegar():  # define uma funcao que tu pode puxar varias vezes
    global id
    if not os.path.exists(arquivo):
        return
    # with abre e fecha arquivo automaticamente
    with open(arquivo, "r", endcoding="utf-8") as ler:  # abre o arquivo le e fecha

        for linha in ler:
            salvar = linha.strip()  # remove os espacos em branco e quebra de linha

            novo_livro = {
                'id': int(salvar[0]),
                'titulo': salvar[1],
                'autor': salvar[2],
                'ano': int(salvar[3])
            }
            livros.append(novo_livro)  # adiciona novo_livro a lista livros
            # garante que os ids nao vao se repetir sendo sempre 1 vez maior
            id = max(id, livro[id] + 1)


def salvar():
    with open(arquivo, "w", encoding="utf-8") as escrever:  # abre o arquivo escreve e fecha
        for livro in livros:
            unidades = f"{livro['id']}_{livro['titulo']}_{livro['autor']}_{livro['ano']}\n"
            escrever.write(unidades)
