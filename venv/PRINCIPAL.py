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
                    if hour.isdigit():
                        hourInt = int(hour)
                        if hourInt < 24: porperiodoHora(year,month,day,hour)
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
                if day.isdigit():
                    dayInt = int(day)
                    apocalipse = ""
                    yearInt = int(year)
                    monthInt = int(month)
                    if ((yearInt % 4 == 0 and yearInt % 100 != 0) or (yearInt % 400 == 0)) and monthInt == 2: apocalipse = 29
                    elif monthInt == 2: apocalipse = 28
                    elif monthInt in [1,3,5,7,8,10,12]: apocalipse = 31
                    else: apocalipse = 30
                    if dayInt <= apocalipse and dayInt > 0: porperiodoDia(year,month,day)
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
            if month.isdigit():
                monthInt = int(month)
                if monthInt < 13 and monthInt > 0: porperiodoMes(year,month)
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
        if year.isdigit():
            porperiodoAno(year)
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
    showFrame(tela_entredatas)

    def voltar_menu():
        main_menu()
    botaoVoltar_menu = tk.Button(tela_entredatas,text="←",font=("Comic Sans MS", 25),fg="white",bg="#361C29",command= voltar_menu)
    botaoVoltar_menu.grid(row=0, column=0, sticky="nw")
    
    entre_text = tk.Label(tela_entredatas,text="ENTRE",font=("Comic Sans MS", 28),fg="white",bg="#361C29")
    entre_text.grid(row=0, column=4, padx=0, pady=0)

    hora_text = tk.Label(tela_entredatas,text="hora",font=("Comic Sans MS", 16),fg="white",bg="#361C29")
    hora_text.grid(row=1, column=5, padx=0, pady=0)

    seg_text = tk.Label(tela_entredatas,text="seg.",font=("Comic Sans MS", 16),fg="white",bg="#361C29")
    seg_text.grid(row=1, column=9, padx=0, pady=0)
    
    ano = tk.Entry(tela_entredatas,font=("Comic Sans MS", 23),fg="gray",width=5)
    ano.grid(row=2, column=0, padx=(240,0), pady=0)
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

    mes = tk.Entry(tela_entredatas,font=("Comic Sans MS", 23),fg="gray",width=4)
    mes.grid(row=2, column=1, padx=0, pady=0)
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

    dia = tk.Entry(tela_entredatas,font=("Comic Sans MS", 23),fg="gray",width=3)
    dia.grid(row=2, column=2, padx=0, pady=0)
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

    as_text = tk.Label(tela_entredatas,text="às",font=("Comic Sans MS", 28),fg="white",bg="#361C29")
    as_text.grid(row=2, column=4, padx=0, pady=0)

    hh = tk.Entry(tela_entredatas,font=("Comic Sans MS", 23),fg="gray",width=3)
    hh.grid(row=2, column=5, padx=0, pady=0)
    hh.insert(0, "00")
    def digitarhh(event):
        if hh.get() == "00":
            hh.delete(0, tk.END)
            hh.config(fg="#363636")
    def sairhh(event):
        if hh.get() == "":
            hh.insert(0, "00")
            hh.config(fg="gray")
    hh.bind("<FocusIn>", digitarhh)
    hh.bind("<FocusOut>", sairhh)

    doispontos_text = tk.Label(tela_entredatas,text=":",font=("Comic Sans MS", 24),fg="white",bg="#361C29")
    doispontos_text.grid(row=2, column=6, padx=0, pady=0)

    min = tk.Entry(tela_entredatas,font=("Comic Sans MS", 23),fg="gray",width=3)
    min.grid(row=2, column=7, padx=0, pady=0)
    min.insert(0, "00")
    def digitarmin(event):
        if min.get() == "00":
            min.delete(0, tk.END)
            min.config(fg="#363636")
    def sairmin(event):
        if min.get() == "":
            min.insert(0, "00")
            min.config(fg="gray")
    min.bind("<FocusIn>", digitarmin)
    min.bind("<FocusOut>", sairmin)

    doispontos2_text = tk.Label(tela_entredatas,text=":",font=("Comic Sans MS", 24),fg="white",bg="#361C29")
    doispontos2_text.grid(row=2, column=8, padx=0, pady=0)

    seg = tk.Entry(tela_entredatas,font=("Comic Sans MS", 23),fg="gray",width=3)
    seg.grid(row=2, column=9, padx=0, pady=0)
    seg.insert(0, "00")
    def digitarseg(event):
        if seg.get() == "00":
            seg.delete(0, tk.END)
            seg.config(fg="#363636")
    def sairseg(event):
        if seg.get() == "":
            seg.insert(0, "00")
            seg.config(fg="gray")
    seg.bind("<FocusIn>", digitarseg)
    seg.bind("<FocusOut>", sairseg)

    min_text = tk.Label(tela_entredatas,text="min.",font=("Comic Sans MS", 16),fg="white",bg="#361C29")
    min_text.grid(row=3, column=7, padx=0, pady=0)


    E_text = tk.Label(tela_entredatas,text="&",font=("Comic Sans MS", 20),fg="white",bg="#361C29")
    E_text.grid(row=4, column=4, padx=0, pady=0)


    hora2_text = tk.Label(tela_entredatas,text="hora",font=("Comic Sans MS", 16),fg="white",bg="#361C29")
    hora2_text.grid(row=5, column=5, padx=0, pady=0)

    seg2_text = tk.Label(tela_entredatas,text="seg.",font=("Comic Sans MS", 16),fg="white",bg="#361C29")
    seg2_text.grid(row=5, column=9, padx=0, pady=0)
    
    ano2 = tk.Entry(tela_entredatas,font=("Comic Sans MS", 23),fg="gray",width=5)
    ano2.grid(row=6, column=0, padx=(240,0), pady=0)
    ano2.insert(0, "YYYY")
    def digitarYYYY2(event):
        if ano2.get() == "YYYY":
            ano2.delete(0, tk.END)
            ano2.config(fg="#363636")
    def sairYYYY2(event):
        if ano2.get() == "":
            ano2.insert(0, "YYYY")
            ano2.config(fg="gray")
    ano2.bind("<FocusIn>", digitarYYYY2)
    ano2.bind("<FocusOut>", sairYYYY2)

    mes2 = tk.Entry(tela_entredatas,font=("Comic Sans MS", 23),fg="gray",width=4)
    mes2.grid(row=6, column=1, padx=0, pady=0)
    mes2.insert(0, "MM")
    def digitarMM2(event):
        if mes2.get() == "MM":
            mes2.delete(0, tk.END)
            mes2.config(fg="#363636")
    def sairMM2(event):
        if mes2.get() == "":
            mes2.insert(0, "MM")
            mes2.config(fg="gray")
    mes2.bind("<FocusIn>", digitarMM2)
    mes2.bind("<FocusOut>", sairMM2)

    dia2 = tk.Entry(tela_entredatas,font=("Comic Sans MS", 23),fg="gray",width=3)
    dia2.grid(row=6, column=2, padx=0, pady=0)
    dia2.insert(0, "DD")
    def digitarDD2(event):
        if dia2.get() == "DD":
            dia2.delete(0, tk.END)
            dia2.config(fg="#363636")
    def sairDD2(event):
        if dia2.get() == "":
            dia2.insert(0, "DD")
            dia2.config(fg="gray")
    dia2.bind("<FocusIn>", digitarDD2)
    dia2.bind("<FocusOut>", sairDD2)

    as2_text = tk.Label(tela_entredatas,text="às",font=("Comic Sans MS", 28),fg="white",bg="#361C29")
    as2_text.grid(row=6, column=4, padx=0, pady=0)

    hh2 = tk.Entry(tela_entredatas,font=("Comic Sans MS", 23),fg="gray",width=3)
    hh2.grid(row=6, column=5, padx=0, pady=0)
    hh2.insert(0, "00")
    def digitarhh2(event):
        if hh2.get() == "00":
            hh2.delete(0, tk.END)
            hh2.config(fg="#363636")
    def sairhh2(event):
        if hh2.get() == "":
            hh2.insert(0, "00")
            hh2.config(fg="gray")
    hh2.bind("<FocusIn>", digitarhh2)
    hh2.bind("<FocusOut>", sairhh2)

    doispontos3_text = tk.Label(tela_entredatas,text=":",font=("Comic Sans MS", 24),fg="white",bg="#361C29")
    doispontos3_text.grid(row=6, column=6, padx=0, pady=0)

    min2 = tk.Entry(tela_entredatas,font=("Comic Sans MS", 23),fg="gray",width=3)
    min2.grid(row=6, column=7, padx=0, pady=0)
    min2.insert(0, "00")
    def digitarmin2(event):
        if min2.get() == "00":
            min2.delete(0, tk.END)
            min2.config(fg="#363636")
    def sairmin2(event):
        if min2.get() == "":
            min2.insert(0, "00")
            min2.config(fg="gray")
    min2.bind("<FocusIn>", digitarmin2)
    min2.bind("<FocusOut>", sairmin2)

    doispontos4_text = tk.Label(tela_entredatas,text=":",font=("Comic Sans MS", 24),fg="white",bg="#361C29")
    doispontos4_text.grid(row=6, column=8, padx=0, pady=0)

    seg2 = tk.Entry(tela_entredatas,font=("Comic Sans MS", 23),fg="gray",width=3)
    seg2.grid(row=6, column=9, padx=0, pady=0)
    seg2.insert(0, "00")
    def digitarseg2(event):
        if seg2.get() == "00":
            seg2.delete(0, tk.END)
            seg2.config(fg="#363636")
    def sairseg2(event):
        if seg2.get() == "":
            seg2.insert(0, "00")
            seg2.config(fg="gray")
    seg2.bind("<FocusIn>", digitarseg2)
    seg2.bind("<FocusOut>", sairseg2)

    min2_text = tk.Label(tela_entredatas,text="min.",font=("Comic Sans MS", 16),fg="white",bg="#361C29")
    min2_text.grid(row=7, column=7, padx=0, pady=0)



    def entreperiodos_result():
        year = ano.get()
        month = mes.get()
        day = dia.get()
        hour = hh.get()
        minute = min.get()
        second = seg.get()

        year2 = ano2.get()
        month2 = mes2.get()
        day2 = dia2.get()
        hour2 = hh2.get()
        minute2 = min2.get()
        second2 = seg2.get()

        cursor.execute(f"SELECT COUNT(*) FROM producao WHERE dataEhorario BETWEEN '{int(year):04d}-{int(month):02d}-{int(day):02d} {int(hour or 0):02d}:{int(minute or 0):02d}:{int(second or 0):02d}' AND '{int(year2):04d}-{int(month2):02d}-{int(day2):02d} {int(hour2 or 0):02d}:{int(minute2 or 0):02d}:{int(second2 or 0):02d}';")
        total = cursor.fetchone()[0]

        labelname = tk.Frame(tela_entredatas, bg="black")
        labelname.grid(row=9, column=0, columnspan=1000, padx=0, pady=(90,0))
        labelname.grid_configure(padx=(220, 220))
    
        scrollname = tk.Scrollbar(labelname)
        scrollname.grid(row=0, column=1, sticky="ns")

        textname = tk.Text(labelname,bg="black",fg="white",yscrollcommand=scrollname.set,width=60,height=8)
        textname.grid(row=0, column=0)

        scrollname.config(command=textname.yview)

        textname.config(state="normal")
        textname.delete("1.0", "end")
        textname.insert("end", f"\n T O T A L  :  {total}  R E G I S T R O S")
        textname.config(state="disabled")
    
    pesquisa = tk.Button(tela_entredatas,text="Pesquisar",font=("Comic Sans MS", 20),fg="white",bg="#170C22",command= entreperiodos_result)
    pesquisa.grid(row=8, column=4, padx=0, pady=0)

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