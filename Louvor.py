import webbrowser

# Dicionário com nomes das músicas e seus respectivos links de cifra e YouTube
musicas = {
    "Até que o Senhor venha - Ministério Zoe": {
        "cifra": "https://www.cifraclub.com.br/ministerio-zoe/ate-que-o-senhor-venha/",
        "youtube": "https://www.youtube.com/watch?v=TdMS20oszR4"
    },
    "Milhão de anos - Theo Rubia": {
        "cifra": "https://www.cifraclub.com.br/theo-rubia/um-milhao-de-anos/",
        "youtube": "https://www.youtube.com/watch?v=5frMRXUeHPU"
    },
    "Estamos de pé - Marcus Salles": {
        "cifra": "https://www.cifraclub.com.br/marcus-salles/estamos-de-pe/",
        "youtube": "https://www.youtube.com/watch?v=4x-yrCz1D9g"
    },
    "Tu és - FHOP": {
        "cifra": "https://www.cifraclub.com.br/florianopolis-house-of-prayer/tu-es-aguas-purificadoras/",
        "youtube": "https://www.youtube.com/watch?v=YXnQ02HYB1w"
    }
}

def mostrar_menu(musicas):
    print("\nMenu de Músicas:")
    for i, musica in enumerate(musicas.keys(), start=1):
        print(f"{i}. {musica}")

def escolher_musica(musicas):
    while True:
        mostrar_menu(musicas)
        try:
            escolha = int(input("\nEscolha uma música pelo número: "))
            if 1 <= escolha <= len(musicas):
                nome_musica = list(musicas.keys())[escolha - 1]
                opcoes_link = musicas[nome_musica]
                while True:
                    print("\nEscolha o link para abrir:")
                    print("1. Cifra Club")
                    print("2. YouTube")
                    print("3. Voltar")
                    escolha_link = int(input("Digite o número da opção desejada: "))
                    if escolha_link == 1:
                        webbrowser.open(opcoes_link["cifra"])
                        print(f"\nVocê escolheu: {nome_musica} - Cifra Club. O link foi aberto no navegador.\n")
                    elif escolha_link == 2:
                        webbrowser.open(opcoes_link["youtube"])
                        print(f"\nVocê escolheu: {nome_musica} - YouTube. O link foi aberto no navegador.\n")
                    elif escolha_link == 3:
                        break
                    else:
                        print("Escolha inválida. Tente novamente.")
                break
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def menu_interativo():
    while musicas:
        escolher_musica(musicas)
    print("Todas as músicas foram escolhidas. Menu encerrado.")

if __name__ == "__main__":
    menu_interativo()