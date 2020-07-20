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
def controllo_Ore(file_name, dati_da_leggere):                                                                           # funzione che mi controlla i progetti per settimana
    ore = float(dati_da_leggere[2])
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
        phaseoftheproject = row[4]
        kindofproject = row[5]
        drawing = row[6]
        timetodesign = row[7]
        deadline = row[8]
        state = row[9]
        date_login = row[10]
        if designer == dati_da_leggere[1] and state =='In progress':                                                    #mi fornisce esattamente su cui stanno lavorando e non quelle totali
            totale_ore = totale_ore + timetodesign
    if totale_ore == 0:
        print("il designer " + dati_da_leggere[1] + " non ha ancora nessun progetto nella settimana del" + str(week))
    if totale_ore != 0:
        print("il designer " + dati_da_leggere[1] + " ha " + str(totale_ore) + " la settimana numero " + str(week))
    ore_libere = ore - totale_ore
    print(dati_da_leggere[1] + ' ha ' + str(ore_libere) + ' ore libere')


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
    for row in rows:
        ID = row[0]
        week = row[1]
        designer = row[2]
        project = row[3]
        phaseoftheproject = row[4]
        kindofproject = row[5]
        drawing = row[6]
        timetodesign = row[7]
        deadline = row[8]
        state = row[9]
        date_login = row[10]
        if designer == dati_da_leggere[1]:
            if state == 'In progress':
                print(designer + " sta lavorando su: " + project + " e sul disegno: " + drawing
                  + " di cui ci vogliono: " + str(timetodesign) + " il disegno e' per il " + deadline)


def progetti_to_review(file_name,dati_da_leggere):                                                                      # funzione che mi controlla i project to review
    Data_Base = sqlite3.connect(file_name)                                                                              # apre il file il sqlite con il nome che gli ho dato
    c = Data_Base.cursor()
    Nome_Table = "'Week " + str(dati_da_leggere[0]) + "'"
    c.execute("SELECT * FROM" + Nome_Table)
    rows = c.fetchall()
    for row in rows:
        ID = row[0]
        week = row[1]
        designer = row[2]
        project = row[3]
        phaseoftheproject = row[4]
        kindofproject = row[5]
        drawing = row[6]
        timetodesign = row[7]
        deadline = row[8]
        state = row[9]
        date_login = row[10]
        if designer == dati_da_leggere[1]:
            if state == 'Ready to review':
                print('il ' + project + ' ' + drawing + ' ' + 'deve essere controllato')

# Main proram

