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

# Definisco le funzioni che mi servono
def controllo_Ore(file_name,dati_da_leggere):                                                                           # funzione che mi controlla i progetti per settimana
    Data_Base = sqlite3.connect(file_name)                                                                              # apre il file il sqlite con il nome che gli ho dato
    c = Data_Base.cursor()
    Nome_Table = "'Week " + str(dati_da_leggere[0]) + "'"
    c.execute("SELECT * FROM" + Nome_Table)
    rows = c.fetchall()
    totale_ore = 0
    for row in rows:
        #ID = row[0]
        week = row[1]
        designer = row[2]
        #project = row[3]
        #design = row[4]
        #site_visit = row[5]
        #kindofproject = row[6]
        #drawing = row[7]
        timetodesign = row[8]
        #deadline = row[9]
        #state = row[10]
        #date_login = row[11]
        if designer == dati_da_leggere[1]:
            totale_ore = totale_ore + timetodesign
    if totale_ore == 0:
        print("il designer " + dati_da_leggere[1] + " non ha ancora nessun progetto nella settimana del" + str(week))
    if totale_ore != 0:
        print("il designer " + dati_da_leggere[1] + " ha " + str(totale_ore) + " la settimana numero " + str(week))


def genera_nome():                                                                                                      # genera il nome del file
    mese = time.strftime("%B")                                                                                          # importa il mese
    anno = time.strftime("%Y")                                                                                          # importa l'anno
    nome_file = f"{mese} {anno}"                                                                                        # crea il nome del file
    return(nome_file)


def controllo_Progetti(file_name,dati_da_leggere):                                                                                     # funzione che mi controlla le ore per settimana
    Data_Base = sqlite3.connect(file_name)                                                                              # apre il file il sqlite con il nome che gli ho dato
    c = Data_Base.cursor()
    Nome_Table = "'Week " + str(dati_da_leggere[0]) + "'"
    c.execute("SELECT * FROM" + Nome_Table)
    rows = c.fetchall()
    totale_ore = 0
    for row in rows:
        ID = row[0]
        week = row[1]
        designer = row[2]
        project = row[3]
        design = row[4]
        site_visit = row[5]
        kindofproject = row[6]
        drawing = row[7]
        timetodesign = row[8]
        deadline = row[9]
        state = row[10]
        date_login = row[11]
        if designer == dati_da_leggere[1]:
            print(designer + " sta lavorando su: " + project + " e sul disegno: " + drawing
                  + " di cui ci vogliono:" + str(timetodesign))


# Main proram
if __name__ == "__main__":
    settimana_corrente = date.today().isocalendar()[1]
    file_name = str(genera_nome()) + ".db"
    week = input('Introduci la settimana che vuoi visualizzare, la settimana corrente è ' + str(settimana_corrente) + '\n')
    designer = input('Inserisci il nome del designer di cui vuoi vedere le ore \n')
    dati_da_leggere = [week, designer.capitalize()]
    cosa_vedere = input('che cosa vuoi vedere, la lista dei Progetti o le Ore?\n')
    if cosa_vedere.capitalize() == 'Ore':
        controllo_Ore(file_name, dati_da_leggere)
    if cosa_vedere.capitalize() == 'Progetti':
        controllo_Progetti(file_name, dati_da_leggere)