#############################################################################
# Filename    : DB.py
# Description : programma che mi genera il DB
# Author      : Andrea Grosso
# Date        : 18.06.2020
# Revision    : R0
# note        :
########################################################################


# importo le librerie che mi servono
from sqlite3 import Connection
import sqlite3
import Data
import time
from os.path import isfile

# Definisco le funzioni che mi servono
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


def genera_tabella(file_name):                                                                                          # genera la tabella con la data corrente
    Data_Base = sqlite3.connect(file_name)                                                                              # apre il file il sqlite con il nome che gli ho dato
    c = Data_Base.cursor()
    Nome_Table = "'" + str(Data.data_corretta()) + "'"
    sql_cmd = '''CREATE TABLE IF NOT EXISTS {}
                    (Week INT PRIMARY KEY NOT NULL,
                     Designer TEXT NOT NULL, 
                     Project TEXT NOT NULL,
                     Drawings TEXT NOT NULL,
                     kindofproject TEXT NOT NULL,
                     Timetodesign FLOAT NOT NULL,
                     Deadline TEXT NOT NULL,
                     Date_login TEXT NOT NULL)'''.format(Nome_Table)
    c.execute(sql_cmd)
    Data_Base.commit()
    Data_Base.close()
    print('Tabella creata')
    return


def genera_database(file_name, Lista):
    Data_Base = sqlite3.connect (file_name)                                                                             # apre il file il sqlite con il nome che gli ho dato
    c = Data_Base.cursor()
    Nome_Table = "'" + Lista[0] + "'"
    c.execute("INSERT INTO " + Nome_Table + 'VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (Lista[0], Lista[1], Lista[2], Lista[3], Lista[4], Lista[5], Lista[6], Lista[7]))
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


#main program
if __name__ == "__main__":
        file_name = str(genera_nome()) + ".db"                                                                              # genera il nome del file che ho bisogno
        controllo_database(file_name)
        genera_database(file_name, Lista)
