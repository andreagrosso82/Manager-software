#############################################################################
# Filename    : Indice_generale.py
# Description : Interfaccia che mi porta nelle varie sottosezione del programma
# Author      : Andrea Grosso
# Date        : 29-03-2021
# Revision    : R5
# note        : Semplifico il programma per usarlo solo come database
#             : Iniziato a testare il programma, la parte dell'inserire un nuovo progetto funziona
########################################################################
# Importo le librerie che mi interessano
import datetime
from datetime import date
from time import strftime
import Manager_software
import Lettura_DB
from os.path import isfile
from time import strftime

# Definisco le costanti che mi servono
file_name = str('Project_database.db')

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


def Ora():
    ora_aggiornata = strftime ('%H:%M')
    return(ora_aggiornata)


# Main proram
if __name__ == "__main__":
    print("Oggi e' il giorno ", data_corretta())
    print("Ciao Andrea \nti sei loggato alle ", Ora())
    cosa_fare = input("Cosa vuoi fare: \n"
                      "1) Inserire un Nuovo progetto (N)\n"
                      "2) Vedere lista progetti Assegnati (A)\n"
                      "3) Modificare un progetto esistente (M)\n")
#Parte riguardante i progetti esistenti
    if cosa_fare.upper() == 'A':
        print("Apro il database dei progetti esistenti")
        while True:
            designer = input('Inserisci il nome del designer di cui vuoi vedere le informazioni \n')
            dati_da_leggere = designer.capitalize()
            Lettura_DB.controllo_Progetti(file_name, dati_da_leggere)
            Continuo = input('Finito o no?(Y/N)\n')
            if Continuo.upper() == 'Y':
                break
# Parte riguardante i nuovi progetti
    if cosa_fare.upper() == 'N':
        print('Inizializzo il database per un nuovo progetto')
        settimana_corrente = date.today().isocalendar()[1]
        if not isfile(file_name):                                                                                       # controlla se il file esiste gia' o deve essere creato
            ID = 1
        else:
            ID = Manager_software.controllo_ID(file_name)
        while True:
            Lista = Manager_software.Interfaccia(ID)
            print(Lista)
            progetto = Manager_software.Database_Progetti(Lista['ID'], Lista['date'], Lista['designer'], Lista['project'], Lista['kindofproject'], Lista['phaseoftheproject'])
            progetto.genera_database(file_name)
            ID = ID + 1
            Continuo = input('Finito o no?(Y/N)\n')
            if Continuo.upper() != 'N' and Continuo.upper() !='Y':
                print("Il risposta che hai introdotto non e' corretta")
                Continuo = input('Finito o no?(Y/N)\n')
            if Continuo.upper() == 'Y':
                break
# Parte riguardante i progetti esistenti
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