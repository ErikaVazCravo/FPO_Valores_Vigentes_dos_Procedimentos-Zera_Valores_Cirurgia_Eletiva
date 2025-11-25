
# Automação criada para zerar os valores de Cirurgia Eletiva na FPO
# Manutenção -> Valores Vigentes dos Procedimentos
# Encontre a primeira linha cinza - deixe ela posicionada na tela como sendo a primeira linha
# Execute o código e selecione o programa da FPO 
# OBS: Será necessário verificar todas as linhas cinzas já que o sistema acaba pulando algumas linhas

import pyautogui
import time
import keyboard

# Marca o início do processamento
inicio = time.time()

# Configurações
colunas_x = [839, 893, 950]        # Coordenadas X das colunas 12, 13 e 14
linha_inicial_y = 155              # Posição Y da primeira linha
distancia_entre_linhas = 20        # Espaçamento vertical entre linhas
linhas_visiveis_na_tela = 41       # Linhas visíveis na tela antes do scroll
total_linhas = 2950                # Total de linhas no sistema

# Função para preencher os valores da linha
def preencher_linha(y):
    for x in colunas_x:
        if keyboard.is_pressed('esc'):
            print("Automação cancelada pelo usuário.")
            exit()
        pyautogui.click(x, y)
        time.sleep(0.03)
        pyautogui.write('0,00')
        time.sleep(0.03)

# Espera para o usuário posicionar a tela
print("Posicione o sistema SIHD2. A automação começará em 5 segundos...")
time.sleep(5)

linha_atual = 1  # Começa da linha 1

while linha_atual <= total_linhas:
    if keyboard.is_pressed('esc'):
        print("Automação cancelada pelo usuário.")
        break

    if linha_atual < linhas_visiveis_na_tela:  # Preenche linhas 1 a 40 normalmente
        y = linha_inicial_y + (distancia_entre_linhas * (linha_atual - 1))
        preencher_linha(y)
        linha_atual += 1
    else:
        # Clica na linha 42 (posição da linha que faz o scroll)
        y_scroll = linha_inicial_y + (distancia_entre_linhas * (linhas_visiveis_na_tela))  # linha 42
        pyautogui.click(colunas_x[0], y_scroll)
        time.sleep(0.2)

        # Preenche a linha 41 (posição fixa após o scroll)
        y_fixa = linha_inicial_y + (distancia_entre_linhas * (linhas_visiveis_na_tela - 1))  # linha 41
        preencher_linha(y_fixa)

        linha_atual += 1

# Marca o fim do processamento
fim = time.time()

# Calcula o tempo total e exibe em minutos e segundos
tempo_total = fim - inicio
minutos = int(tempo_total // 60)
segundos = int(tempo_total % 60)

print(f"\nProcesso concluído em {minutos} minutos e {segundos} segundos!")

print("Automação finalizada com sucesso.")
