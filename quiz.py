import random


class Domanda:
    def __init__(self, domanda, livello, rispostaCorretta, elencoRisposte):
        self.domanda = domanda
        self.livello = livello
        self.rispostaCorretta = rispostaCorretta
        self.elencoRisposte = elencoRisposte

    def __str__(self):
        return f"Livello {self.livello}) {self.domanda} \n 1. {self.elencoRisposte[0]} \n 2. {self.elencoRisposte[1]} \n 3. {self.elencoRisposte[2]} \n 4. {self.elencoRisposte[3]}"


class Player:
    def __init__(self, nickname, punteggio):
        self.nickname = nickname
        self.punteggio = punteggio


f = open("domande.txt", "r")
riga = f.readline()
elementi_oggetto = []
dizionario_domande = {}
while riga != "":
    elementi_oggetto.clear()
    while riga != "\n":
        elementi_oggetto.append(riga)
        riga = f.readline()
    lista_risposte = [elementi_oggetto[2], elementi_oggetto[3], elementi_oggetto[4], elementi_oggetto[5]]
    d_temp = Domanda(elementi_oggetto[0], elementi_oggetto[1], elementi_oggetto[2], lista_risposte)
    dizionario_domande[elementi_oggetto[0]] = d_temp
    riga = f.readline()
f.close()

livello_massimo = 0
for domanda in dizionario_domande.values():
    if domanda.livello > livello_massimo:
        livello_massimo = domanda.livello

domande_per_livello = {}
for i in range(0, livello_massimo - 1):
    lista_domande_del_livello = []
    for domanda in dizionario_domande.values():
        if domanda.livello == i:
            lista_domande_del_livello.append(domanda)
    domande_per_livello[i] = lista_domande_del_livello


def gioco():
    ha_sbagliato = False
    livello_risposte = 0
    while not ha_sbagliato:
        lista_livello_corrente = domande_per_livello[livello_risposte]
        numero_casuale = random.randint(0, len(lista_livello_corrente) - 1)
        domanda_proposta = lista_livello_corrente[numero_casuale]
        print(domanda_proposta.__str__())
        random.shuffle(domanda_proposta.elencoRisposte)
        risposta = input("Inserisci la risposta: ")
        if risposta == 1:
            if domanda_proposta.rispostaCorretta == domanda_proposta.elencoRisposte[0]:
                print("Risposta corretta!")
            else:

                print(f"Risposta sbagliata! La risposta corretta era: {domanda_proposta.rispostaCorretta}")
                ha_sbagliato = True
        elif risposta == 2:
            if domanda_proposta.rispostaCorretta == domanda_proposta.elencoRisposte[0]:
                print("Risposta corretta!")
            else:
                print(f"Risposta sbaglita! La risposta corretta era: {domanda_proposta.rispostaCorretta}")
                ha_sbagliato = True
        elif risposta == 3:
            if domanda_proposta.rispostaCorretta == domanda_proposta.elencoRisposte[0]:
                print("Risposta corretta!")
            else:
                print(f"Risposta sbaglita! La risposta corretta era: {domanda_proposta.rispostaCorretta}")
                ha_sbagliato = True
        elif risposta == 4:
            if domanda_proposta.rispostaCorretta == domanda_proposta.elencoRisposte[0]:
                print("Risposta corretta!")
            else:
                print(f"Risposta sbaglita! La risposta corretta era: {domanda_proposta.rispostaCorretta}")
                ha_sbagliato = True
        else:
            print("Risposta non valida")


