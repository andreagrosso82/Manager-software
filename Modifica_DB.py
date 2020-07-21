#############################################################################
# Filename    : Modifica_DB.py
# Description : Modifico il database
# Author      : Andrea Grosso
# Date        : 21-07-2020
# Revision    : R2
# note        : Inizio la stesura del programma per la modifica del database
#               testato la modifica del database e funziona
#               Iniziato la stesura della modifica dei parametri
########################################################################
# Importo le librerie che mi interessano
import datetime
from datetime import date
from time import strftime
import Manager_software
import Lettura_DB
from os.path import isfile
from time import strftime
import Settimane
import sqlite3


# Definisco le funzioni che mi servono
def modifica_progetto(dati_da_modificare):                                                                       # funzione che mi controlla i progetti per settimana
    print(dati_da_modificare[3])
    Data_Base = sqlite3.connect(dati_da_modificare[0])                                                                              # apre il file il sqlite con il nome che gli ho dato
    c = Data_Base.cursor()
    Nome_Table = "'Week " + dati_da_modificare[1] + "'"
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
        if designer == dati_da_modificare[2] and project == dati_da_modificare[3]:
            print(row[6]+row[9])


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


def modifica_progetto(dati_da_modificare):                                                                                     # funzione che mi controlla le ore per settimana
    Data_Base = sqlite3.connect(dati_da_modificare[0])                                                                              # apre il file il sqlite con il nome che gli ho dato
    c = Data_Base.cursor()
    Nome_Table = "'Week " + str(dati_da_modificare[1]) + "'"
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
        if project == dati_da_modificare[2]:
            informazioni={"ID":row[0],
                          "week": row[1],
                          "designer": row[2],
                          "project": row[3],
                          "phaseoftheproject": row[4],
                          "kindofproject": row[5],
                          "drawing": row[6],
                          "timetodesign": row[7],
                          "deadline": row[8],
                          "state": row[9],
                          "date_login":row[10]}
            print(informazioni)
            while True:
                cosa_modificare = input("Scegli cosa vuoi modificare:\n"
                                        "- Week (1)\n"
                                        "- Designer (2)\n"
                                        "- Phase of the project (3)\n"
                                        "- Kind of project (4)\n"
                                        "- Time to the design (5)\n"
                                        "- Deadline (6)\n"
                                        "- State of the design (7)\n")
                if cosa_modificare == 1:
                    nuova_settimana = input('Introduci la settimana \n')
                    informazioni["week"] = nuova_settimana
                if cosa_modificare == 2:
                    nuovo_designer = input('Inserisci il nome del designer \n')
                    informazioni["designer"] = nuovo_designer.capitalize()
                if cosa_modificare == 3:
                    nuova_fase = input('Il progetto a che punto è? (Sale support, Handover, Site visit, Design) \n')
                    informazioni["phaseoftheproject"] = nuova_fase.capitalize()
                if cosa_modificare == 4:
                    nuovo_tipo = input('Definisci la natura del disegno che hai bisogno (New, Asbuilt, Amendment) \n')
                    informazioni["kindofproject"] = nuovo_tipo.capitalize()
                if cosa_modificare == 5:
                    nuova_ora = input('Specifica quanto tempo serve per realizzare il disegno \n')
                    informazioni["timetodesign"] = float(nuova_ora)
                if cosa_modificare == 6:
                    nuova_deadline = input("Per quando e' il progetto?(Introduci la data nel seguente formato GG-MM-ANNO) \n")
                    informazioni["deadline"] = nuova_deadline
                if cosa_modificare == 7:
                    nuovo_stato = input("Definisci lo stato del progetto (In progress, Ready to review, Amendments, Sign-off, On hold) \n")
                    informazioni["state"] = nuovo_stato
                #if cosa_modificare != 1 and cosa_modificare != 2 and cosa_modificare != 3 and cosa_modificare != 4 and cosa_modificare != 5 and cosa_modificare != 6 and cosa_modificare != 7:
                    #print('Non hai insirito la corretta risposta alla domanda, leggi la domanda con maggior attenzione')
                Continuo = input('Finito o no?(Y/N)\n')
                if Continuo.upper() != 'N' and Continuo.upper() != 'Y':
                    print("Il risposta che hai introdotto non e' corretta")
                    Continuo = input('Finito o no?(Y/N)\n')
                if Continuo.upper() == 'Y':
                    break

            #new_state=input('definisci lo stato del progetto (In progress, Ready to review, Amendments, Close, On hold) \n')
            #informazioni["state"]=new_state
            print(informazioni)
            #modifica_dati(file_name, informazioni)


def modifica_dati(file_name, informazioni):
    Data_Base = sqlite3.connect(file_name)                                                                              # apre il file il sqlite con il nome che gli ho dato
    c = Data_Base.cursor()
    Nome_Table = "'Week " + str(informazioni['week']) + "'"
    print(Nome_Table)
    nome1 = informazioni['state']
    nome2 = 'In progress'
    c.execute("UPDATE " + Nome_Table + 'SET State_Design = ? WHERE State_Design = ?', (nome1, nome2))
    Data_Base.commit()
    Data_Base.close()




# Main proram
if __name__ == "__main__":
    print("Modifichiamo progetto esistente")
    settimana_corrente = date.today().isocalendar()[1]
    file_name = str(Manager_software.genera_nome()) + ".db"
    print('La settimana corrente è ' + str(settimana_corrente) + '\n')
    scegli_week = input("Vuoi vedere l'elenco delle settimane (Y/N) \n")
    if scegli_week.capitalize() == 'Y':
        Settimane.elenco_settimane()
        week = input('Introduci la settimana \n')
    if scegli_week.capitalize() == 'N':
        pass
    if scegli_week.capitalize() != 'Y' and scegli_week.capitalize() != 'N':
        print("La risposta che hai introdotto non e' corretta")
    progetto = input('Inserisci il nome del progetto di cui vuoi modificare le informazioni \n')
    #drawing = input('Introduci il tipo di drawing che deve modificare(GW,PLR,PID,ELE,CSD) \n')
    #state = input('definisci lo stato del progetto (In progress, Ready to review, Amendments, Close, On hold) \n')
    week = input('Inserisci la settimana dove si trova il progetto che vuoi modificare \n')
    dati_da_modificare = [file_name, week, progetto.capitalize()]
    modifica_progetto(dati_da_modificare)
