#############################################################################
# Filename    : Manager_software.py
# Description : programma che mi aiuta a gestire le ore che il mio team deve spendere per design
# Author      : Andrea Grosso
# Date        : 18.06.2020
# Revision    : R0
# note        :
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


def Interfaccia(ID):
    Week = date.today().isocalendar()[1]
    designer = input('Introduci il nome del designer \n')
    project = input('Introduci il nome del progetto \n')
    drawing = input('Introduci il tipo di drawing che deve produrre(GW,PLR,PID,ELE,CSD) \n')
    kindofproject = input('Definisci la natura del disegno che hai bisogno (New, Asbuilt, Amendment) \n')
    settimana = input('Il disegno deve essere fatto in questa settimana o nelle prossime?(Y/N) \n')
    if settimana.upper() == 'N':
        nuova_settimana = input('Introduci la settimana che vuoi il disegno \n')
        Week = nuova_settimana
    Timetodesign = input('Specifica quanto tempo serve per realizzare il disegno \n')
    Deadline = input("Per quando e' il progetto?(Introduci la data nel seguente formato GG-MM-ANNO) \n")
    Date_login = data_corretta()
    Lista = [ID, Week, designer.capitalize(), project.capitalize(), drawing.upper(), kindofproject.capitalize(), Timetodesign, Deadline, Date_login]
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
    Nome_Table = "'Week " + str(Lista[1]) + "'"
    sql_cmd = '''CREATE TABLE IF NOT EXISTS {}
                    (ID INT PRIMARY KEY NOT NULL,
                     Week TEXT KEY NOT NULL,
                     Designer TEXT NOT NULL, 
                     Project TEXT NOT NULL,
                     Drawings TEXT NOT NULL,
                     kind_of_project TEXT NOT NULL,
                     Time_to_design FLOAT NOT NULL,
                     Deadline TEXT NOT NULL,
                     Date_login TEXT NOT NULL)'''.format(Nome_Table)
    c.execute(sql_cmd)
    Data_Base.commit()
    Data_Base.close()
    print('Tabella creata')
    return


def genera_database(file_name, Lista):
    Data_Base = sqlite3.connect(file_name)                                                                             # apre il file il sqlite con il nome che gli ho dato
    c = Data_Base.cursor()
    Nome_Table = "'Week " + str(Lista[1]) + "'"
    print(Nome_Table)
    c.execute("INSERT INTO " + Nome_Table + 'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', (Lista[0], Lista[1], Lista[2], Lista[3], Lista[4], Lista[5], Lista[6], Lista[7], Lista[8]))
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


# Main program
if __name__ == "__main__":
    ID = 1
    while True:
        file_name = str(genera_nome()) + ".db"                                                                          # genera il nome del file che ho bisogno
        Lista = Interfaccia(ID)
        print(Lista)
        controllo_database(file_name, Lista)
        genera_database(file_name, Lista)
        ID = ID+1
        Continuo = input('Finito o no?(Y/N)')
        if Continuo.upper() == 'Y':
            break








#tot = 0
#while True:
    #a = input ('Introduci il valore di a /n')
    #tot = tot + int(a)
    #print(tot)
    #if tot >= 40:
        #avanzo = tot - 40
        #print (avanzo)
        #break