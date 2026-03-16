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

def porhora():

    print("Working")
    showFrame(tela_porhora)
    dia = tk.Entry(tela_porhora,font=("Comic Sans MS", 20),fg="gray",width=3)
    dia.grid(row=2, column=2, padx=(45,20), pady=80)
    mes = tk.Entry(tela_porhora,font=("Comic Sans MS", 20),fg="gray",width=3)
    mes.grid(row=2, column=3, padx=(20,20), pady=80)
    ano = tk.Entry(tela_porhora,font=("Comic Sans MS", 20),fg="gray",width=5)
    ano.grid(row=2, column=4, padx=(20,20), pady=80)
    def hourSearch():
        day = dia.get()
        month = mes.get()
        year = ano.get()
        print(f"{day}/{month}/{year}")
        #cursor.execute(f"SELECT * FROM producao WHERE DATE(dataEhorario) = '{day}-{month}-{year}';")
    pesquisa = tk.Button(tela_porhora, text="=>", command= hourSearch)
    pesquisa.grid(row=2, column=5, padx=(20,20), pady=80)
    
    dia.insert(0, "DD")
    def digitarDD(event):
        if dia.get() == "DD":
            dia.delete(0, tk.END)
            dia.config(fg="#363636")
    def sairDD(event):
        if dia.get() == "":
            dia.insert(0, "DD")
            dia.config(fg="gray")
    dia.bind("<FocusIn>", digitarDD)
    dia.bind("<FocusOut>", sairDD)
    mes.insert(0, "MM")
    def digitarMM(event):
        if mes.get() == "MM":
            mes.delete(0, tk.END)
            mes.config(fg="#363636")
    def sairMM(event):
        if mes.get() == "":
            mes.insert(0, "MM")
            mes.config(fg="gray")
    mes.bind("<FocusIn>", digitarMM)
    mes.bind("<FocusOut>", sairMM)
    ano.insert(0, "YYYY")
    def digitarYYYY(event):
        if ano.get() == "YYYY":
            ano.delete(0, tk.END)
            ano.config(fg="#363636")
    def sairYYYY(event):
        if ano.get() == "":
            ano.insert(0, "YYYY")
            ano.config(fg="gray")
    ano.bind("<FocusIn>", digitarYYYY)
    ano.bind("<FocusOut>", sairYYYY)

    resPorhora = tk.Label(tela_porhora,text="",font=("Comic Sans MS", 20),fg="gray")


def pordia():

    print("Working too!")
    showFrame(tela_pordia)
    def daySearch():
        print("daySearch Working")


showFrame(tela_menu)
botao1 = tk.Button(tela_menu,text="Produção por Hora",font=("Comic Sans MS", 24),bg="#170C22",fg="white",width=28,command=porhora)
botao1.grid(row=5, column=0, padx=256, pady=(450,0))
botao2 = tk.Button(tela_menu,text="Produção por Dia",font=("Comic Sans MS", 24),bg="#170C22",fg="white",width=28,command=pordia)
botao2.grid(row=6, column=0, padx=256, pady=(50,0))



#cursor.execute("SELECT COUNT(*) FROM usuarios")



janela.mainloop()
#cursor.close()
#conexao.close()