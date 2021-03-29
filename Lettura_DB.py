#############################################################################
# Filename    : Lettura_DB.py
# Description : Questo file legge le informazioni nel database
# Author      : Andrea Grosso
# Date        : 27-06-2020
# Revision    : R0
# note        : programma per la lettura dei dati su database sqlite
#               aggiungere la gestione degli errori quando non si immettono i dati corretamente
########################################################################
# Importo le librerie che mi interessano
from datetime import date
import datetime
import sqlite3
import time
from os.path import isfile


# Definisco le costanti che mi servono


# Definisco le funzioni che mi servono
def controllo_Progetti(file_name,dati_da_leggere):                                                                      # funzione che mi controlla le ore per settimana
    Data_Base = sqlite3.connect(file_name)                                                                              # apre il file il sqlite con il nome che gli ho dato
    c = Data_Base.cursor()
    date = datetime.datetime.now()
    month = (date.strftime("%B"))
    Nome_Table = "'" + str(month) + "'"
    c.execute("SELECT * FROM" + Nome_Table)
    rows = c.fetchall()
    for row in rows:
        ID = row[0]
        Date = row[1]
        Designer = row[2]
        Project = row[3]
        Kindofproject = row[4]
        Phaseoftheproject = row[5]
        if Designer == dati_da_leggere and Phaseoftheproject == 'In_progress':
            print(Designer + " sta lavorando su: " + Project + " Tipo di progetto: " + Kindofproject)
        elif Designer == dati_da_leggere and Phaseoftheproject == 'Complete':
            print(Designer + " ha completato i seguenti progetti: " + Project)


