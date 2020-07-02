#############################################################################
# Filename    : Settimane.py
# Description : Crea il database delle settimane
# Author      : Andrea Grosso
# Date        : 01-07-2020
# Revision    : R0
# note        : Completa il data
########################################################################
# Importo le librerie che mi interessano
import sqlite3
import time
from os.path import isfile


# Definisco le funzioni che mi servono
def genera_file(file_name):                                                                                             # genera il file
    Data_Base = sqlite3.connect(file_name)                                                                              # apre il file il sqlite con il nome che gli ho dato
    Data_Base.commit()
    Data_Base.close()
    print('File creato')
    return


def genera_tabella(file_name):                                                                                   # genera la tabella con la data corrente
    Data_Base = sqlite3.connect(file_name)                                                                              # apre il file il sqlite con il nome che gli ho dato
    c = Data_Base.cursor()
    Nome_Table = "'Settimane 2020'"
    sql_cmd = '''CREATE TABLE IF NOT EXISTS {}
                    (ID INT PRIMARY KEY NOT NULL,
                     Week TEXT KEY NOT NULL,
                     Dal TEXT NOT NULL, 
                     Al TEXT NOT NULL)'''.format(Nome_Table)
    c.execute(sql_cmd)
    Data_Base.commit()
    Data_Base.close()
    print('Tabella creata')
    return


def genera_database(file_name, Lista):
    Data_Base = sqlite3.connect(file_name)                                                                              # apre il file il sqlite con il nome che gli ho dato
    c = Data_Base.cursor()
    Nome_Table = "'Settimane 2020'"
    c.execute("INSERT INTO " + Nome_Table + 'VALUES (?, ?, ?, ?)', (Lista[0], Lista[1], Lista[2], Lista[3]))
    Data_Base.commit()
    Data_Base.close()
    print('Data base creato')


def controllo_database(file_name):
    if not isfile (file_name):                                                                                          # controlla se il file esiste gia' o deve essere creato
        genera_file(file_name)
        genera_tabella(file_name)
    else:
        print("Il file esiste gia'")
        genera_tabella(file_name)


def controllo_ID(file_name):
    Data_Base = sqlite3.connect(file_name)                                                                              # apre il file il sqlite con il nome che gli ho dato
    c = Data_Base.cursor()
    Nome_Table = "'Settimane 2020'"
    c.execute("SELECT * FROM" + Nome_Table)
    rows = c.fetchall()
    for row in rows:
        ID = row[0] + 1
    return(ID)




# Main proram
if __name__ == "__main__":
    ID = 1
    file_name = "Settimane.db"
    while True:
        ID = controllo_ID(file_name)
        controllo_database(file_name)
        week = input('Introduci la settimana \n')
        dal = input('Quando inizia la settimana \n')
        al = input('Quando finisce la settimana \n')
        Lista = [ID, week, dal, al]
        genera_database(file_name, Lista)
        Continuo = input('Finito o no?(Y/N)\n')
        if Continuo.upper() != 'N' and Continuo.upper() != 'Y':
            print("Il risposta che hai introdotto non e' corretta")
            Continuo = input('Finito o no?(Y/N)\n')
        if Continuo.upper() == 'Y':
            break