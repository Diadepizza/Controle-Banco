from db import conectar
import tkinter as tk

janela = tk.Tk()
janela.title("CONTROLE PRODUÇÃO")
janela.geometry("1115x900")
janela.configure(bg="#361C29")
conexao = conectar()
cursor = conexao.cursor()

tela_menu = tk.Frame(janela, bg="#361C29")
tela_porhora = tk.Frame(janela, bg="#361C29")
tela_pordia = tk.Frame(janela, bg="#361C29")
def showFrame(frame):
    for f in (tela_menu, tela_pordia, tela_porhora):
        f.pack_forget()
    frame.pack()

def hourSearch(d,m,y):
    day = d.get()
    month = m.get()
    year = y.get()
    print(day)
def daySearch():
    print("daySearch Working")

def porhora():

    print("Working")
    showFrame(tela_porhora)
    dia = tk.Entry(tela_porhora)
    dia.grid(row=2, column=2, padx=(45,20), pady=80)
    mes = tk.Entry(tela_porhora)
    mes.grid(row=2, column=3, padx=(20,20), pady=80)
    ano = tk.Entry(tela_porhora)
    ano.grid(row=2, column=4, padx=(20,20), pady=80)
    pesquisa = tk.Button(tela_porhora, text="=>", command= hourSearch(dia,mes,ano)).grid(row=2, column=5, padx=(20,20), pady=80)


def pordia():

    print("Working too!")
    showFrame(tela_pordia)

showFrame(tela_menu)
botao1 = tk.Button(tela_menu,text="Produção por Hora",font=("Comic Sans MS", 24),bg="#170C22",fg="white",width=28,command=porhora)
botao1.grid(row=5, column=0, padx=256, pady=(450,0))
botao2 = tk.Button(tela_menu,text="Produção por Dia",font=("Comic Sans MS", 24),bg="#170C22",fg="white",width=28,command=pordia)
botao2.grid(row=6, column=0, padx=256, pady=(50,0))



#cursor.execute("SELECT COUNT(*) FROM usuarios")



janela.mainloop()
#cursor.close()
#conexao.close()