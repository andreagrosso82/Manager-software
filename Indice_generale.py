#############################################################################
# Filename    : Indice_generale.py
# Description : Interfaccia che mi porta nelle varie sottosezione del programma
# Author      : Andrea Grosso
# Date        : 24-06-2020
# Revision    : R0
# note        : Inizio a codificare, ma senza aggiungere nessuna interfaccia grafice
########################################################################
# Importo le librerie che mi interessano
import datetime
from datetime import date
from time import strftime
import Manager_software
import Lettura_DB
from os.path import isfile
from time import strftime


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
    cosa_fare = input("Cosa vuoi fare? \nvedere un progetto Esistente o inserire un Nuovo progetto?\n")
    ore_settimanali = float(ore_settimanali())
    if cosa_fare.upper() == 'E':
        print("Apro il databse dei progetti esistenti")
        settimana_corrente = date.today().isocalendar()[1]
        file_name = str(Manager_software.genera_nome()) + ".db"
        while True:
            week = input('Introduci la settimana che vuoi visualizzare, la settimana corrente è ' + str(settimana_corrente) + '\n')
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
            Continuo = input('Finito o no?(Y/N)\n')
            if Continuo.upper() == 'Y':
                break
    if cosa_fare.upper() == 'N':
        print('Inizializzo il database per un nuovo progetto')
        file_name = str(Manager_software.genera_nome()) + ".db"
        if not isfile(file_name):                                                                                       # controlla se il file esiste gia' o deve essere creato
            ID = 1
        else:
            ID = Manager_software.controllo_ID()
        while True:
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
    if cosa_fare.upper() != 'N' and cosa_fare.upper() != 'E':
        print('La funzione che hai scelto non esiste')
