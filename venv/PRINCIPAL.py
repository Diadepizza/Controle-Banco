from db import conectar
import tkinter as tk

janela = tk.Tk()
janela.title("CONTROLE PRODUÇÃO")
janela.geometry("1115x900")
janela.configure(bg="#361C29")
janela.grid_rowconfigure(0, weight=0)
janela.grid_columnconfigure(0, weight=0)
conexao = conectar()
cursor = conexao.cursor()

tela_menu = tk.Frame(janela, bg="#361C29")
tela_entredatas = tk.Frame(janela, bg="#361C29")
tela_porperiodo = tk.Frame(janela, bg="#361C29")

tela_porperiodo_ano = tk.Frame(janela, bg="#361C29")
tela_porperiodo_mes = tk.Frame(janela, bg="#361C29")
tela_porperiodo_dia = tk.Frame(janela, bg="#361C29")
tela_porperiodo_hora = tk.Frame(janela, bg="#361C29")

year = ""
month = ""
day = ""
hour = ""

def showFrame(frame):
    for f in (tela_menu, tela_entredatas, tela_porperiodo, tela_porperiodo_ano, tela_porperiodo_mes, tela_porperiodo_dia, tela_porperiodo_hora):
        f.grid_forget()
    frame.grid(row=0, column=0, sticky="nsew")
def mysql_scrollabel(frame,sizex,sizey,dados,labelname,textname,scrollname):
    labelname = tk.Frame(frame, bg="black")
    labelname.pack(fill="both", expand=False, padx=sizex, pady=sizey)

    
    scrollname = tk.Scrollbar(labelname)
    scrollname.pack(side="right", fill="y")

    textname = tk.Text(labelname,bg="black",fg="white",yscrollcommand=scrollname.set)
    textname.pack(side="left", fill="both", expand=True)

    scrollname.config(command=textname.yview)

    textname.config(state="normal")
    textname.delete("1.0", "end")
    for linha in dados:
        textname.insert("end", f"ID: {linha[0]} | Nome: {linha[1]}\n")
    textname.config(state="disabled")


def porperiodo():
    def porperiodoAno(year):
        def porperiodoMes(year,month):
            def porperiodoDia(year,month,day):
                def porperiodoHora(year,month,day,hour):
                    
                    showFrame(tela_porperiodo_hora)
                    # H O R A
                    #*texto*
                    def voltar_hora():
                        porperiodoDia(year,month,day)
                    botaoVoltar_hora = tk.Button(tela_porperiodo_hora,text="←",font=("Comic Sans MS", 25),fg="white",bg="#361C29",command= voltar_hora)
                    botaoVoltar_hora.grid(row=0, column=0, sticky="nw")
                    print(year,month,day,hour)

                    #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   
                      #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   # 
                    #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #

                showFrame(tela_porperiodo_dia)
                # D I A
                hora = tk.Entry(tela_porperiodo_dia,font=("Comic Sans MS", 23),fg="gray",width=3)
                hora.grid(row=1, column=1, padx=(0,0), pady=0)
                hora.insert(0, "hh")
                def digitarH(event):
                    if hora.get() == "hh":
                        hora.delete(0, tk.END)
                        hora.config(fg="#363636")
                def sairH(event):
                    if hora.get() == "":
                        hora.insert(0, "hh")
                        hora.config(fg="gray")
                hora.bind("<FocusIn>", digitarH)
                hora.bind("<FocusOut>", sairH)

                hora_text = tk.Label(tela_porperiodo_dia,text="Hora :",font=("Comic Sans MS", 23),fg="white",bg="#361C29")
                hora_text.grid(row=1, column=0, padx=(387,10), pady=0)

                def hourSearch():
                    hour = hora.get()
                    porperiodoHora(year,month,day,hour)
                    #cursor.execute(f"SELECT * FROM producao WHERE DATE(dataEhorario) = '{day}-{month}-{year}';")
                pesquisaHora = tk.Button(tela_porperiodo_dia,text="Pesquisar",font=("Comic Sans MS", 16),fg="white",bg="#170C22",command= hourSearch)
                pesquisaHora.grid(row=1, column=2, padx=(10,40), pady=0)

                def voltar_dia():
                    porperiodoMes(year,month)
                botaoVoltar_dia = tk.Button(tela_porperiodo_dia,text="←",font=("Comic Sans MS", 25),fg="white",bg="#361C29",command= voltar_dia)
                botaoVoltar_dia.grid(row=0, column=0, sticky="nw")

                #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   
                  #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   # 
                #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #

            showFrame(tela_porperiodo_mes)
            # M E S
            dia = tk.Entry(tela_porperiodo_mes,font=("Comic Sans MS", 23),fg="gray",width=3)
            dia.grid(row=1, column=1, padx=(0,0), pady=0)
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

            dia_text = tk.Label(tela_porperiodo_mes,text="Dia :",font=("Comic Sans MS", 23),fg="white",bg="#361C29")
            dia_text.grid(row=1, column=0, padx=(387,10), pady=0)

            def daySearch():
                day = dia.get()
                porperiodoDia(year,month,day)
                #cursor.execute(f"SELECT * FROM producao WHERE DATE(dataEhorario) = '{day}-{month}-{year}';")
            pesquisaDia = tk.Button(tela_porperiodo_mes,text="Pesquisar",font=("Comic Sans MS", 16),fg="white",bg="#170C22",command= daySearch)
            pesquisaDia.grid(row=1, column=2, padx=(10,40), pady=0)

            def voltar_mes():
                porperiodoAno(year)
            botaoVoltar_mes = tk.Button(tela_porperiodo_mes,text="←",font=("Comic Sans MS", 25),fg="white",bg="#361C29",command= voltar_mes)
            botaoVoltar_mes.grid(row=0, column=0, sticky="nw")

            #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   
              #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   # 
            #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #

        showFrame(tela_porperiodo_ano)
        # A N O
        mes = tk.Entry(tela_porperiodo_ano,font=("Comic Sans MS", 23),fg="gray",width=4)
        mes.grid(row=1, column=1, padx=(0,0), pady=0)
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

        mes_text = tk.Label(tela_porperiodo_ano,text="Mês :",font=("Comic Sans MS", 23),fg="white",bg="#361C29")
        mes_text.grid(row=1, column=0, padx=(387,10), pady=0)

        def monthSearch():
            month = mes.get()
            porperiodoMes(year,month)
            #cursor.execute(f"SELECT * FROM producao WHERE DATE(dataEhorario) = '{day}-{month}-{year}';")
        pesquisaMes = tk.Button(tela_porperiodo_ano,text="Pesquisar",font=("Comic Sans MS", 16),fg="white",bg="#170C22",command= monthSearch)
        pesquisaMes.grid(row=1, column=2, padx=(10,40), pady=0)

        def voltar_ano():
            porperiodo()
        botaoVoltar_ano = tk.Button(tela_porperiodo_ano,text="←",font=("Comic Sans MS", 25),fg="white",bg="#361C29",command= voltar_ano)
        botaoVoltar_ano.grid(row=0, column=0, sticky="nw")

        #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   
          #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   # 
        #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #

    showFrame(tela_porperiodo)
    # MAIN  P O R  P E R Í O D O
    ano = tk.Entry(tela_porperiodo,font=("Comic Sans MS", 34),fg="gray",width=5)
    ano.grid(row=5, column=1, padx=(35,0), pady=(450,0))
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

    ano_text = tk.Label(tela_porperiodo,text="Ano :",font=("Comic Sans MS", 34),fg="white",bg="#361C29")
    ano_text.grid(row=5, column=0, padx=(330,0), pady=(450,0))

    def yearSearch():
        year = ano.get()
        porperiodoAno(year)
        #cursor.execute(f"SELECT * FROM producao WHERE DATE(dataEhorario) = '{day}-{month}-{year}';")
    pesquisaAno = tk.Button(tela_porperiodo,text="Pesquisar",font=("Comic Sans MS", 20),fg="white",bg="#170C22",command= yearSearch)
    pesquisaAno.grid(row=5, column=2, padx=(35,0), pady=(450,0))

    def voltar_menu():
        main_menu()
    botaoVoltar_menu = tk.Button(tela_porperiodo,text="←",font=("Comic Sans MS", 25),fg="white",bg="#361C29",command= voltar_menu)
    botaoVoltar_menu.grid(row=0, column=0, sticky="nw")

    #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   
      #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   # 
    #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #    

def entredatas():

    print("Working too!")
    showFrame(tela_entredatas)
    def daySearch():
        print("daySearch Working")

def main_menu():
    showFrame(tela_menu)
    botao1 = tk.Button(tela_menu,text="Produção por Período",font=("Comic Sans MS", 24),bg="#170C22",fg="white",width=28,command=porperiodo)
    botao1.grid(row=5, column=0, padx=256, pady=(450,0))
    botao2 = tk.Button(tela_menu,text="Produção por Dia",font=("Comic Sans MS", 24),bg="#170C22",fg="white",width=28,command=entredatas)
    botao2.grid(row=6, column=0, padx=256, pady=(50,0))

main_menu()


#cursor.execute("SELECT COUNT(*) FROM usuarios")



janela.mainloop()
#cursor.close()
#conexao.close()