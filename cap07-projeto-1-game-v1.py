# import
import random 
from os import system, name

# função para limpar a tela
def limpa_tela():
    # windows
    if name == 'nt':
        _ = system('cls')
    
    # mac ou linux
    else:
        _ = system('clear')

def game():
    limpa_tela()

    print('Jogo da Forca\n')

    palavras = ['python', 'programacao', 'computador', 'desenvolvimento', 'software', 'algoritmo', 'jogo', 'tecnologia', 'maracuja']

    palavra = random.choice(palavras)

    letras_descobertas = ['_' for letra in palavra]

    chances = 6

    letras_erradas = []

    while chances > 0:
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))

        tentativa = input("\nDigite uma letra: ").lower()

        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)
        
        if "_" not in letras_descobertas:
            print("\nParabéns! Você adivinhou a palavra:", palavra)
            break
    
    if "_" in letras_descobertas:
        print("\nVocê perdeu! A palavra era:", palavra)
    print("\nFim do jogo!")

if __name__ == "__main__":
    game()
