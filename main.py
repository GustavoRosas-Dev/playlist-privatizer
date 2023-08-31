# Autor: Gustavo Rosas
# GitHub: https://github.com/GustavoRosas-Dev/playlist-privatizer
# Data: 2023-08-29

#region BIBLIOTECAS

import pyautogui as pg
import time

#endregion

#region VARIÁVEIS

DELAY = 0.2
SPACE = -25
CONFIDENCE = 0.85
PATH = 'resources/images/'
VOLTAR = 'alt', 'left'

#endregion

#region FUNÇÕES

#region LOCALIZAR E CLICAR
def localizar_e_clicar(nome):

    while True:

        # Espera um pouco
        time.sleep(DELAY)

        try:
            print(f'DEBUG > {nome}')
            if nome == 'EDITAR':
                CONFIDENCE = 0.7
            else:
                CONFIDENCE = 0.85

            print(f'CONFIDENCE > {CONFIDENCE}')
            image_location = pg.locateOnScreen((PATH + f'{nome.lower()}.png'),
                                                      confidence=CONFIDENCE)

            if image_location is not None:
                print(f'Achei > {nome}')
                image_center = pg.center(
                    image_location)  # Obtém o centro da imagem encontrada
                print('DEBUG', image_center)
                pg.click(image_center)  # Clica no centro da imagem
                print(f'Cliquei > {nome}')

                break

        except Exception as e:
            print('Erro:', e)

#endregion

#region MAIN
def main():

    # region Uma automação chamada Pieton que vivia em busca de aventuras.
    while True:
        pg.scroll(SPACE)  # Rola a página para baixo

        try:
            # Localiza uma imagem pública e uma imagem privada na tela.
            image_PUBLICA_location = pg.locateOnScreen((PATH + 'publica.png'), confidence=CONFIDENCE)

            if image_PUBLICA_location is not None:

                # Obtém o centro da imagem encontrada.
                image_PUBLICA_center = pg.center(image_PUBLICA_location)
                pg.click(image_PUBLICA_center)  # Clica no centro da imagem

                # Aguarda um período de tempo.
                time.sleep(DELAY)

                # Navega por uma série de opções em uma interface.

                # Clica na opção 'EDITAR'.
                localizar_e_clicar('EDITAR')

                # Clica na opção 'VISIBILIDADE'.
                localizar_e_clicar('VISIBILIDADE')

                # Clica na opção 'PARTICULAR'.
                localizar_e_clicar('PARTICULAR')

                # Clica na opção 'SALVAR'.
                localizar_e_clicar('SALVAR')

                # Volta para a página anterior.
                pg.hotkey(VOLTAR)
                
                time.sleep(DELAY*5)

                # Clica na aba chamada 'ABA_PLAYLIST'.
                localizar_e_clicar('ABA_PLAYLIST')
                #endregion

            else:
                print('Não localizei nada')

            #endregion

        except Exception as e:
            print('Erro:', e)

    #endregion

#endregion

#endregion

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("A execução foi interrompida pelo usuário.")
    except Exception as e:
        print("Erro na execução:", e)