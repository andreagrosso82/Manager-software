#R0:
# programma per testare internet con la funzione di ping
# aggiunto la funzione di data log e inoltra una email con il report
#R1
# gestisco la mail nel caso non c'e' internet
# aggiungo i dati che voglio passare alla funzione in modo da poterla riutilizzare

# definisco le librerie che mi servono
import smtplib
import Data
import Ora


def manda_email(ora, data):                                                                                          # definisce la funzione per mandare la mail
    importa_dati = open('proprieta.txt', 'r')
    riga = (importa_dati.readlines()[0])
    proprieta = (riga[20:])
    oggetto = "Subject: " + proprieta + "\n\n"                                                              # definisce l'oggetto della email
    frase_1 = "messaggio di test mandato 1 volta al giorno \n"
    frase_2 = ("alle " + str(ora) + " del giorno " + str(data))
    frase_3 = open("Internet_report.txt", "r").read()
    contenuto = frase_1 + frase_2 + frase_3                                                                 # definisce il messaggio della email
    messaggio = oggetto + contenuto                                                                         # la mail
    try:
        email = smtplib.SMTP("smtp.gmail.com", 587)                                                         # specifica il server SMTP
        email.ehlo()                                                                                        # connesso al server
        email.starttls()                                                                                    # apre la crittografia per mandare la password
        email.login("agraspberry2019@gmail.com", "Giovanni2019@")                                           # username e password della email che intendiamo usare
        email.sendmail("agraspberry2019@gmail.com", "andrea.grosso@iso.co.uk", messaggio)                   # funzione che manda la mail
        email.quit()                                                                                        # chiude la comunicazione con il server
    except:
        print("non posso inviare la mail perche' non c'e' internet")

