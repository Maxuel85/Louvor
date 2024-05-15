import webbrowser

# Dicionário com nomes das músicas e seus respectivos links de cifra
musicas = {
    "Milhoes de anos - Theo Rubia": "https://www.cifraclub.com.br/musica1/",
    "Música 2": "https://www.cifraclub.com.br/musica2/",
    "Música 3": "https://www.cifraclub.com.br/musica3/",
    "Música 4": "https://www.cifraclub.com.br/musica4/"
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