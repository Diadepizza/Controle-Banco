from db import conectar
import tkinter as tk

janela = tk.Tk()
janela.title("CONTROLE PRODUÇÃO")
janela.geometry("1115x900")
janela.configure(bg="#361C29")
janela.grid_rowconfigure(0, weight=0)
janela.grid_columnconfigure(0, weight=0)
janela.resizable(False, False)
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

def porperiodo():
    def porperiodoAno(year):
        def porperiodoMes(year,month):
            def porperiodoDia(year,month,day):
                def porperiodoHora(year,month,day,hour):
                    
                    showFrame(tela_porperiodo_hora)
                    # H O R A
                    def hour_result(frame,sizex,sizey):
                        labelname = tk.Frame(frame, bg="black")
                        labelname.grid(row=2, column=0, columnspan=3, padx=sizex, pady=sizey)
                        labelname.grid_configure(padx=(220, 220))

    
                        scrollname = tk.Scrollbar(labelname)
                        scrollname.grid(row=0, column=1, sticky="ns")

                        textname = tk.Text(labelname,bg="black",fg="white",yscrollcommand=scrollname.set)
                        textname.grid(row=0, column=0)

                        scrollname.config(command=textname.yview)

                        textname.config(state="normal")
                        textname.delete("1.0", "end")
                        cursor.execute(f"SELECT dataEhorario, id, intervalo FROM producao WHERE dataEhorario BETWEEN '{int(year):04d}-{int(month):02d}-{int(day):02d} {int(hour):02d}:00:00' AND '{int(year):04d}-{int(month):02d}-{int(day):02d} {int(hour):02d}:59:59'")
                        dados = cursor.fetchall()
                        for linha in dados:
                            textname.insert("end", f"INSTANTE: {linha[0]} | ID: {linha[1]} | DELAY: {linha[2]}\n")
                        cursor.execute(f"SELECT COUNT(*) FROM producao WHERE dataEhorario BETWEEN '{int(year):04d}-{int(month):02d}-{int(day):02d} {int(hour):02d}:00:00' AND '{int(year):04d}-{int(month):02d}-{int(day):02d} {int(hour):02d}:59:59'")
                        total = cursor.fetchone()[0]
                        textname.insert("end", f"\n T O T A L  H O R A  :  {total}")
                        textname.config(state="disabled")
                    hour_result(tela_porperiodo_hora,130,160)
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
                pesquisaHora.grid(row=1, column=2, padx=(10,320), pady=0)

                def day_result(frame,sizex,sizey):
                    labelname = tk.Frame(frame, bg="black")
                    labelname.grid(row=2, column=0, columnspan=3, padx=sizex, pady=sizey)
                    labelname.grid_configure(padx=(220, 220))
    
                    scrollname = tk.Scrollbar(labelname)
                    scrollname.grid(row=0, column=1, sticky="ns")

                    textname = tk.Text(labelname,bg="black",fg="white",yscrollcommand=scrollname.set)
                    textname.grid(row=0, column=0)
                    scrollname.config(command=textname.yview)

                    textname.config(state="normal")
                    textname.delete("1.0", "end")
                    #TOTAL DIÁRIO
                    cursor.execute(f"SELECT COUNT(*) FROM producao WHERE dataEhorario BETWEEN '{int(year):04d}-{int(month):02d}-{int(day):02d} 00:00:00' AND '{int(year):04d}-{int(month):02d}-{int(day):02d} 23:59:59'")
                    total = cursor.fetchone()[0]

                    #TABELA ( & TOTAL POR HORA)
                    for hh in range(0,24):
                        cursor.execute(f"SELECT COUNT(*) FROM producao WHERE dataEhorario BETWEEN '{int(year):04d}-{int(month):02d}-{int(day):02d} {hh:02d}:00:00' AND '{int(year):04d}-{int(month):02d}-{int(day):02d} {hh:02d}:59:59'")
                        total_hora = cursor.fetchone()[0]
                        textname.insert("end", f"Hora: {hh:02d} | Produção: {total_hora}\n")
                    textname.insert("end", f"\n T O T A L  D I Á R I O  :  {total}")
                    textname.config(state="disabled")
                day_result(tela_porperiodo_dia,130,160)

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
            pesquisaDia.grid(row=1, column=2, padx=(10,320), pady=0)

            def month_result(frame,sizex,sizey):
                year_int = int(year)
                labelname = tk.Frame(frame, bg="black")
                labelname.grid(row=2, column=0, columnspan=3, padx=sizex, pady=sizey)
                labelname.grid_configure(padx=(220, 220))

    
                scrollname = tk.Scrollbar(labelname)
                scrollname.grid(row=0, column=1, sticky="ns")

                textname = tk.Text(labelname,bg="black",fg="white",yscrollcommand=scrollname.set)
                textname.grid(row=0, column=0)

                scrollname.config(command=textname.yview)

                textname.config(state="normal")
                textname.delete("1.0", "end")
                apocalipse = ""
                ap = 0
                if ((year_int % 4 == 0 and year_int % 100 != 0) or (year_int % 400 == 0)) and (month == "02" or month == "2"):
                    apocalipse = "29"
                    ap = 30
                elif month == "02" or month == "2":
                    apocalipse = "28"
                    ap = 29
                elif month in ["01","1","03","3","05","5","07","7","08","8","10","12"]:
                    apocalipse = "31"
                    ap = 32
                else:   
                    apocalipse = "30"
                    ap = 31

                #TOTAL MENSAL
                cursor.execute(f"SELECT COUNT(*) FROM producao WHERE dataEhorario BETWEEN '{int(year):04d}-{int(month):02d}-01 00:00:00' AND '{int(year):04d}-{int(month):02d}-{int(apocalipse)} 23:59:59'")
                total = cursor.fetchone()[0]

                #TABELA ( & TOTAL POR DIA)
                for dd in range(1,ap):
                    cursor.execute(f"SELECT COUNT(*) FROM producao WHERE dataEhorario BETWEEN '{int(year):04d}-{int(month):02d}-{dd:02d} 00:00:00' AND '{int(year):04d}-{int(month):02d}-{dd:02d} 23:59:59'")
                    total_dia = cursor.fetchone()[0]
                    textname.insert("end", f"Dia: {dd} | Produção: {total_dia}\n")
                textname.insert("end", f"\n T O T A L  M E N S A L  :  {total}")
                textname.config(state="disabled")
            month_result(tela_porperiodo_mes,130,160)

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
        pesquisaMes.grid(row=1, column=2, padx=(10,320), pady=0)

        def year_result(frame,sizex,sizey):
            year_int = int(year)
            labelname = tk.Frame(frame, bg="black")
            labelname.grid(row=2, column=0, columnspan=3, padx=sizex, pady=sizey)
            labelname.grid_configure(padx=(220, 220))

    
            scrollname = tk.Scrollbar(labelname)
            scrollname.grid(row=0, column=1, sticky="ns")

            textname = tk.Text(labelname,bg="black",fg="white",yscrollcommand=scrollname.set)
            textname.grid(row=0, column=0)

            scrollname.config(command=textname.yview)

            textname.config(state="normal")
            textname.delete("1.0", "end")

            #TOTAL ANUAL
            cursor.execute(f"SELECT COUNT(*) FROM producao WHERE dataEhorario BETWEEN '{year_int}-01-01 00:00:00' AND '{year_int}-12-31 23:59:59'")
            total = cursor.fetchone()[0]

            #TABELA ( & TOTAL POR MÊS)
            for mm in range(1,13):
                match mm:
                    case 1:
                        mesemquestao = "jan."
                    case 2:
                        mesemquestao = "fev."
                    case 3:
                        mesemquestao = "mar."
                    case 4:
                        mesemquestao = "abr."
                    case 5:
                        mesemquestao = "mai."
                    case 6:
                        mesemquestao = "jun."
                    case 7:
                        mesemquestao = "jul."
                    case 8:
                        mesemquestao = "ago."
                    case 9:
                        mesemquestao = "set."
                    case 10:
                        mesemquestao = "out."
                    case 11:
                        mesemquestao = "nov."
                    case 12:
                        mesemquestao = "dez."
                apocalipse = ""
                if ((year_int % 4 == 0 and year_int % 100 != 0) or (year_int % 400 == 0)) and mm == 2: apocalipse = "29"
                elif mm == 2: apocalipse = "28"
                elif mm in [1,3,5,7,8,10,12]: apocalipse = "31"
                else: apocalipse = "30"
                cursor.execute(f"SELECT COUNT(*) FROM producao WHERE dataEhorario BETWEEN '{int(year):04d}-{mm:02d}-01 00:00:00' AND '{int(year):04d}-{mm:02d}-{int(apocalipse)} 23:59:59'")
                total_mes = cursor.fetchone()[0]
                textname.insert("end", f"{mesemquestao} | {total_mes}\n")
            textname.insert("end", f"\n T O T A L  A N U A L  :  {total}")
            textname.config(state="disabled")
        year_result(tela_porperiodo_ano,130,160)

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


janela.mainloop()
cursor.close()
conexao.close()