#############################################################################
# Filename    : Manager_software.py
# Description : programma che mi aiuta a gestire le ore che il mio team deve spendere per design
# Author      : Andrea Grosso
# Date        : 18.06.2020
# Revision    : R0
# note        : Il controllo delle ore non è corretto, da rivedere
#               Il controllo della data deve essere fatto correttamente
########################################################################
# Importo le librerie che mi interessano
from datetime import date
import datetime
import sqlite3
import time
from os.path import isfile


# Definisco le funzioni che mi servono
def data_corretta():
    data = datetime.date.today()                                                                                        # importa la data corrente
    data_corretta = str(data)                                                                                           # converte la data in formato string
    anno = (data_corretta[0:4])                                                                                         # definisce la variabile anno
    mese = (data_corretta[5:7])                                                                                         # definisce la variabile mese
    giorno = (data_corretta[8:10])                                                                                      # definisce la variabile giorno
    corretto_ordine=(giorno, '-', mese, '-', anno)                                                                      # stampa la data e l'ora
    data_corretta= ''.join(corretto_ordine)                                                                             # convertere il tulpe in stringa
    return(data_corretta)


def Interfaccia(ID):                                                                                                    # funzione che mi completa la tebella con le funzioni che ho bisogno
    week = date.today().isocalendar()[1]                                                                                # genera la settimana in base al calendario
    designer = input('Introduci il nome del designer \n')
    project = input('Introduci il nome del progetto \n')
    phaseoftheproject = input ("Il progetto a che punto è? (Handover, Site visit, Design) \n")
    if phaseoftheproject.capitalize() != 'Handover' \
            and phaseoftheproject.capitalize() != 'Site visit' \
            and phaseoftheproject.capitalize() != 'Design':                                                             #gestisce l'errore nel caso non introduco il corretto valore
        print('Non hai insirito la corretta risposta alla domanda, leggi la domanda con maggior attenzione')
        phaseoftheproject = input("Il progetto a che punto è? (Handover, Site visit, Design) \n")
    kindofproject = input('Definisci la natura del disegno che hai bisogno (New, Asbuilt, Amendment) \n')
    if kindofproject.capitalize() != 'New' \
            and kindofproject.capitalize() != 'Asbuilt' \
            and kindofproject.capitalize() != 'Amendment':                                                              #gestisce l'errore nel caso non introduco il corretto valore
        print('Non hai inserito la corretta risposta alla domanda, leggi la domanda con maggior attenzione')
        kindofproject = input('Definisci la natura del disegno che hai bisogno (New, Asbuilt, Amendment)\n')
    drawing = input('Introduci il tipo di drawing che deve produrre(GW,PLR,PID,ELE,CSD) \n')
    if drawing.upper() != 'GW' and drawing.upper() != 'PLR' and drawing.upper() != 'PID' and drawing.upper() != 'ELE' \
            and drawing.upper() != 'CSD':                                                                               #gestisce l'errore nel caso non introduco il corretto valore
        print('Non hai insirito la corretta risposta alla domanda, leggi la domanda con maggior attenzione')
        drawing = input('Introduci il tipo di drawing che deve produrre(GW,PLR,PID,ELE,CSD) \n')
    settimana = input('Il disegno deve essere fatto in questa settimana o nelle prossime?(Y/N) \n')
    if settimana.upper() == 'N':
        nuova_settimana = input('Introduci la settimana che vuoi il disegno \n')
        week = nuova_settimana
        ID = controllo_ID_WEEK(week)
    timetodesign = input('Specifica quanto tempo serve per realizzare il disegno \n')
    #if timetodesign.ischar() == True:                                                                                   #gestisce l'errore nel caso non introduco il corretto valore
        #print("Il valore che hai introdotto non e' corretto")
        #timetodesign = input('Specifica quanto tempo serve per realizzare il disegno \n')
    deadline = input("Per quando e' il progetto?(Introduci la data nel seguente formato GG-MM-ANNO) \n")
    if len(deadline) != 10:
        print('La data che hai introdotto non è corretta')
        deadline = input("Per quando e' il progetto?(Introduci la data nel seguente formato GG-MM-ANNO) \n")
    state = input ('definisci lo stato del progetto (In progress, Ready to review, Amendments, Close, On hold) \n')
    if state.capitalize() != 'In progress' and state.capitalize() != 'Ready to review' and \
            state.capitalize() != 'Amendments' and state.capitalize() != 'Close' and state.capitalize() != 'On hold':   #gestisce l'errore nel caso non introduco il corretto valore
        print('Non hai insirito la corretta risposta alla domanda, leggi la domanda con maggior attenzione')
        state = input('definisci lo stato del progetto (In progress, Ready to review, Amendments, Close, On hold) \n')
    date_login = data_corretta()
    Lista = [ID, week, designer.capitalize(), project.capitalize(), phaseoftheproject.capitalize(),
             kindofproject.capitalize(), drawing.upper(), float(timetodesign), deadline, state.capitalize(), date_login]# genero la lista da passare al database
    #print(Lista)
    return(Lista)


def genera_nome():                                                                                                      # genera il nome del file
    mese = time.strftime("%B")                                                                                          # importa il mese
    anno = time.strftime("%Y")                                                                                          # importa l'anno
    nome_file = f"{mese} {anno}"                                                                                        # crea il nome del file
    return(nome_file)


def genera_file(file_name):                                                                                             # genera il file
    Data_Base = sqlite3.connect(file_name)                                                                              # apre il file il sqlite con il nome che gli ho dato
    Data_Base.commit()
    Data_Base.close()
    print('File creato')
    return


def genera_tabella(file_name, Lista):                                                                                   # genera la tabella con la data corrente
    Data_Base = sqlite3.connect(file_name)                                                                              # apre il file il sqlite con il nome che gli ho dato
    c = Data_Base.cursor()
    #Nome_Table = "'Week " + str(Lista) + "'"
    Nome_Table = "'Week " + str(Lista[1]) + "'"
    sql_cmd = '''CREATE TABLE IF NOT EXISTS {}
                    (ID INT PRIMARY KEY NOT NULL,
                     Week TEXT KEY NOT NULL,
                     Designer TEXT NOT NULL, 
                     Project TEXT NOT NULL,
                     Phase_of_the_project TEXT NOT NULL,
                     Kind_of_project TEXT NOT NULL,
                     Drawings TEXT NOT NULL,
                     Time_to_design FLOAT NOT NULL,
                     Deadline TEXT NOT NULL,
                     State_Design TEXT NOT NULL,
                     Date_login TEXT NOT NULL)'''.format(Nome_Table)
    c.execute(sql_cmd)
    Data_Base.commit()
    Data_Base.close()
    print('Tabella creata')
    return


def genera_database(file_name, Lista):
    Data_Base = sqlite3.connect(file_name)                                                                              # apre il file il sqlite con il nome che gli ho dato
    c = Data_Base.cursor()
    Nome_Table = "'Week " + str(Lista[1]) + "'"
    #print(Nome_Table)
    c.execute("INSERT INTO " + Nome_Table + 'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
              (Lista[0], Lista[1], Lista[2], Lista[3], Lista[4], Lista[5], Lista[6], Lista[7], Lista[8], Lista[9], Lista[10]))
    Data_Base.commit()
    Data_Base.close()
    print('Data base creato')


def controllo_database(file_name, Lista):
    if not isfile (file_name):                                                                                          # controlla se il file esiste gia' o deve essere creato
        genera_file(file_name)
        genera_tabella(file_name, Lista)
    else:
        print("Il file esiste gia'")
        genera_tabella(file_name, Lista)


def controllo_ore(file_name, Lista):                                                                                     # funzione che mi controlla le ore per settimana
    Data_Base = sqlite3.connect(file_name)                                                                              # apre il file il sqlite con il nome che gli ho dato
    c = Data_Base.cursor()
    Nome_Table = "'Week " + str(Lista[1]) + "'"
    c.execute("SELECT * FROM" + Nome_Table)
    rows = c.fetchall()
    totale_ore = 0
    for row in rows:
        ID = row[0]
        week = row[1]
        designer = row[2]
        project = row[3]
        phaseoftheproject = row[4]
        kindofproject = row[5]
        drawing = row[6]
        timetodesign = float(row[7])
        deadline = row[8]
        state = row[9]
        date_login = row[10]
        #print (ID, week, designer, project, design, site_visit, kindofproject, drawing, timetodesign, deadline, state, date_login)
        totale_ore = totale_ore + timetodesign
        if totale_ore >= 40:
            avanzo = totale_ore - 40
            print(avanzo)
    print("il designer "+ designer + " ha " + str(totale_ore) + " la settimana numero " + str(week))
    return()

def controllo_ID():
    file_name = str(genera_nome()) + ".db"
    Data_Base = sqlite3.connect(file_name)                                                                              # apre il file il sqlite con il nome che gli ho dato
    c = Data_Base.cursor()
    week = date.today().isocalendar()[1]
    Nome_Table = "'Week " + str(week) + "'"
    c.execute("SELECT * FROM" + Nome_Table)
    rows = c.fetchall()
    for row in rows:
        ID = row[0] + 1
    return(ID)


def controllo_ID_WEEK(week):
    file_name = str(genera_nome()) + ".db"
    Data_Base = sqlite3.connect(file_name)                                                                              # apre il file il sqlite con il nome che gli ho dato
    c = Data_Base.cursor()
    Nome_Table = "'Week " + str(week) + "'"
    c.execute("SELECT * FROM" + Nome_Table)
    rows = c.fetchall()
    for row in rows:
        ID = row[0] + 1
    return(ID)









#tot = 0
#while True:
    #a = input ('Introduci il valore di a /n')
    #tot = tot + int(a)
    #print(tot)
    #
        #break