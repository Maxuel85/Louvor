import webbrowser

# Dicionário com nomes das músicas e seus respectivos links de cifra
musicas = {
    "Até que o Senhor venha - Ministério Zoe": "https://www.cifraclub.com.br/ministerio-zoe/ate-que-o-senhor-venha/",
    "Milhão de anos - Theo Rubia": "https://www.cifraclub.com.br/theo-rubia/um-milhao-de-anos/",
    "Estamos de pé - Marcus Salles": "https://www.cifraclub.com.br/marcus-salles/estamos-de-pe/",
    "Tu és - FHOP": "https://www.cifraclub.com.br/florianopolis-house-of-prayer/tu-es-aguas-purificadoras/"
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
                link_musica = musicas.pop(nome_musica)
                webbrowser.open(link_musica)
                print(f"\nVocê escolheu: {nome_musica}. O link foi aberto no navegador.\n")
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