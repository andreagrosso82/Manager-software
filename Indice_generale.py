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
from time import strftime
import Manager_software


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

# Main proram
if __name__ == "__main__":
    print("Oggi e' il giorno ", data_corretta())
    print("Buongiorno Andrea \nti sei loggato alle ", Ora())
    cosa_fare = input("Cosa vuoi fare? \nvedere un progetto Esistente o inserire un Nuovo progetto?\n")
    if cosa_fare.upper() == 'E':
        print("Apro il databse dei progetti esistenti")
    if cosa_fare.upper() == 'N':
        print('Inizializzo il database per un nuovo progetto')
        ID = 1
        ID = Manager_software.controllo_ID()
        while True:
            file_name = str(Manager_software.genera_nome()) + ".db"  # genera il nome del file che ho bisogno
            Lista = Manager_software.Interfaccia(ID)
            print(Lista)
            Manager_software.controllo_database(file_name, Lista)
            Manager_software.genera_database(file_name, Lista)
            Manager_software.controllo_ore(file_name, Lista)
            ID = ID + 1
            Continuo = input('Finito o no?(Y/N)')
            if Continuo.upper() == 'Y':
                break
    if cosa_fare.upper() != 'N' and cosa_fare.upper() != 'E':
        print('La funzione che hai scelto non esiste')
