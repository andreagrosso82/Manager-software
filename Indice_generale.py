#############################################################################
# Filename    : Indice_generale.py
# Description : Interfaccia che mi porta nelle varie sottosezione del programma
# Author      : Andrea Grosso
# Date        : 18-07-2020
# Revision    : R2
# note        : Iniziate alcune modifiche per l'interfaccia
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

# Definisco le funzioni che mi servono
def data_corretta():
    data = datetime.date.today()                                                        # importa la data corrente
    data_corretta = str(data)                                                           # converte la data in formato string
    anno = (data_corretta[0:4])                                                         # definisce la variabile anno
    mese = (data_corretta[5:7])                                                         # definisce la variabile mese
    giorno = (data_corretta[8:10])                                                      # definisce la variabile giorno
    corretto_ordine=(giorno, '-', mese, '-', anno)                                      # stampa la data e l'ora
    data_corretta= ''.join(corretto_ordine)                                             # convertere il tulpe in stringa
    return(data_corretta)


def Ora():
    ora_aggiornata = strftime ('%H:%M')
    return(ora_aggiornata)


def ore_settimanali():
    giorno = datetime.datetime.today().weekday()
    if giorno == 0:
        ore_settimanali = 40
    if giorno == 1:
        ore_settimanali = 32
    if giorno == 2:
        ore_settimanali = 24
    if giorno == 3:
        ore_settimanali = 16
    if giorno == 4:
        ore_settimanali = 8
    return(ore_settimanali)


# Main proram
if __name__ == "__main__":
    print("Oggi e' il giorno ", data_corretta())
    print("Ciao Andrea \nti sei loggato alle ", Ora())
    cosa_fare = input("Cosa vuoi fare: \n"
                      "1) Vedere un progetto Esistente(E)\n"
                      "2) Inserire un Nuovo progetto (N)\n"
                      "3) Modificare un progetto esistente (M)\n"
                      "4) Vedere se ci sono progetti da rivedere (R)\n")
    ore_settimanali = float(ore_settimanali())
    if cosa_fare.upper() == 'E':
        print("Apro il databse dei progetti esistenti")
        settimana_corrente = date.today().isocalendar()[1]
        file_name = str(Manager_software.genera_nome()) + ".db"
        while True:
            print('La settimana corrente è ' + str(settimana_corrente) + '\n')
            scegli_week = input("Vuoi vedere l'elenco delle settimane (Y/N) \n")
            if scegli_week.capitalize() == 'Y':
                Settimane.elenco_settimane()
                week = input('Introduci la settimana \n')
            if scegli_week.capitalize() =='N':
                week = input('Introduci la settimana \n')
            if scegli_week.capitalize() != 'Y' and scegli_week.capitalize() !='N':
                print("La risposta che hai introdotto non e' corretta")
            if week != settimana_corrente:
                ore_settimanali = 40
            designer = input('Inserisci il nome del designer di cui vuoi vedere le informazioni \n')
            dati_da_leggere = [week, designer.capitalize(), ore_settimanali]
            cosa_vedere = input('che cosa vuoi vedere, la lista dei Progetti o le Ore?\n')
            if cosa_vedere.capitalize() == 'Ore':
                Lettura_DB.controllo_Ore(file_name, dati_da_leggere)
            if cosa_vedere.capitalize() == 'Progetti':
                print('LISTA PROGETTI IN CORSO \n')
                Lettura_DB.controllo_Progetti(file_name, dati_da_leggere)
                print('LISTA PROGETTI DA REVISIONARE \n')
                Lettura_DB.progetti_to_review(file_name,dati_da_leggere)
                print("LISTA PROGETTI GIA' REVISIONATI MA CON MODIFICHE DA FARE \n")
                print('LISTA PROGETTI INTERNI \n')
            Continuo = input('Finito o no?(Y/N)\n')
            if Continuo.upper() == 'Y':
                break
    if cosa_fare.upper() == 'N':
        print('Inizializzo il database per un nuovo progetto')
        file_name = str(Manager_software.genera_nome()) + ".db"
        settimana_corrente = date.today().isocalendar()[1]
        if not isfile(file_name):                                                                                       # controlla se il file esiste gia' o deve essere creato
            ID = 1
        else:
            ID = Manager_software.controllo_ID(settimana_corrente)
        while True:
            print('La settimana corrente è ' + str(settimana_corrente) + '\n')
            scegli_week = input("Vuoi vedere l'elenco delle settimane (Y/N) \n")
            if scegli_week.capitalize() == 'Y':
                Settimane.elenco_settimane()
                week = input('Introduci la settimana \n')
            if scegli_week.capitalize() == 'N':
                week = input('Introduci la settimana \n')
                settimana_corrente = week
                print(settimana_corrente)
                ID = Manager_software.controllo_ID(settimana_corrente)
            if scegli_week.capitalize() != 'Y' and scegli_week.capitalize() != 'N':
                print("La risposta che hai introdotto non e' corretta")
            Lista = Manager_software.Interfaccia(ID)
            print(Lista)
            Manager_software.controllo_database(file_name, Lista)
            Manager_software.genera_database(file_name, Lista)
            Manager_software.controllo_ore(file_name, Lista)
            ID = ID + 1
            Continuo = input('Finito o no?(Y/N)\n')
            if Continuo.upper() != 'N' and Continuo.upper() !='Y':
                print("Il risposta che hai introdotto non e' corretta")
                Continuo = input('Finito o no?(Y/N)\n')
            if Continuo.upper() == 'Y':
                break
    if cosa_fare.upper() == 'M':
        print("Modifichiamo progetto esistente")
        settimana_corrente = date.today().isocalendar()[1]
        file_name = str(Manager_software.genera_nome()) + ".db"
        while True:
            print('La settimana corrente è ' + str(settimana_corrente) + '\n')
            scegli_week = input("Vuoi vedere l'elenco delle settimane (Y/N) \n")
            if scegli_week.capitalize() == 'Y':
                Settimane.elenco_settimane()
                week = input('Introduci la settimana \n')
            if scegli_week.capitalize() == 'N':
                week = input('Introduci la settimana \n')
            if scegli_week.capitalize() != 'Y' and scegli_week.capitalize() != 'N':
                print("La risposta che hai introdotto non e' corretta")
            progetto = input('Inserisci il nome del progetto di cui vuoi modificare le informazioni \n')
            drawing = input('Introduci il tipo di drawing che deve modificare(GW,PLR,PID,ELE,CSD) \n')
            state = input('definisci lo stato del progetto (In progress, Ready to review, Amendments, Close, On hold) \n')
            dati_da_modificare = [progetto.capitalize(), drawing.upper(), state.capitalize()]

    if cosa_fare.upper() != 'N' and cosa_fare.upper() != 'E':
        print('La funzione che hai scelto non esiste')