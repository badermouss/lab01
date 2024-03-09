import random


class Domanda:
    def __init__(self, testo, livello, risposta_corretta, risposte):
        self.testo = testo
        self.livello = livello
        self.risposta_corretta = risposta_corretta
        self.risposte = risposte


class Player:
    def __init__(self, nickname, punteggio):
        self.nickname = nickname
        self.punteggio = punteggio

    def __str__(self):
        return f"{self.nickname} {self.punteggio}"


def game():
    domande_gioco = leggi_file("domande.txt")
    liv_max = livello_massimo(domande_gioco)
    domande_per_livello = dizionario_livelli(liv_max, domande_gioco)
    ha_sbagliato = False
    livello_corrente = 0
    while not ha_sbagliato and livello_corrente <= liv_max:
        domanda_proposta = definisci_domanda(domande_per_livello[livello_corrente])
        mostra_domanda(domanda_proposta)
        risposta_data = int(input("Inserisci la risposta: "))
        risposta_giusta = numero_risposta_corretta(domanda_proposta)
        if risposta_data == risposta_giusta:
            livello_corrente += 1
            print("\n")
        else:
            ha_sbagliato = True
            print(f"Risposta sbagliata! La risposta corretta era: {risposta_giusta}")
    if livello_corrente == liv_max + 1:
        print(f"Hai totalizzato il punteggio massimo di {livello_corrente} punti!")
    else:
        print(f"\nHai totalizzato {livello_corrente} punti!")
    nickname = input("Inserisci il tuo nickname: ")
    player_temp = Player(nickname, livello_corrente)
    aggiungi_punteggio("punti.txt", player_temp)
    ordina_punteggi("punti.txt")


def leggi_file(file):
    with open(file, "r") as f:
        lista_righe_file = f.readlines()
        counter_riga = 0
        domande = []
        while counter_riga < len(lista_righe_file):
            testo = lista_righe_file[counter_riga].strip()
            livello = int(lista_righe_file[counter_riga + 1])
            risposta_corretta = lista_righe_file[counter_riga + 2].strip()
            risposte = [lista_righe_file[counter_riga + 2].strip(), lista_righe_file[counter_riga + 3].strip(),
                        lista_righe_file[counter_riga + 4].strip(),
                        lista_righe_file[counter_riga + 5].strip()]
            d_temp = Domanda(testo, livello, risposta_corretta, risposte)
            domande.append(d_temp)
            counter_riga += 7
    return domande


def livello_massimo(domande):
    liv_max = 0
    for domanda in domande:
        if domanda.livello > liv_max:
            liv_max = domanda.livello
    return liv_max


def mostra_domanda(domanda):
    random.shuffle(domanda.risposte)
    print(f"Livello {domanda.livello}) {domanda.testo}")
    for i, risp in enumerate(domanda.risposte):
        print(f"{i + 1}. {risp}")


def numero_risposta_corretta(domanda):
    num = 0
    for i, risp in enumerate(domanda.risposte):
        if risp == domanda.risposta_corretta:
            num = i + 1
    return num


def dizionario_livelli(livello_max, domande):
    diz = {}
    for i in range(0, livello_max + 1):
        lista_prov = []
        for domanda in domande:
            if domanda.livello == i:
                lista_prov.append(domanda)
        diz[i] = lista_prov
    return diz


def definisci_domanda(domande):
    i = random.randint(0, len(domande) - 1)
    return domande[i]


def aggiungi_punteggio(file, player):
    with open(file, "a") as f:
        f.write("\n" + player.__str__() + "\n")


def ordina_punteggi(file):
    with open(file, "r") as f:
        punteggi = f.readlines()
        punteggi_ordinati = []
        for punteggio in punteggi:
            punteggio.strip()
            if punteggio != "":
                punteggi_ordinati.append(punteggio[::-1].strip())
        punteggi_ordinati.sort(reverse=True)
        punteggi_finali = []
        for punteggio in punteggi_ordinati:
            if punteggio != "":
                punteggi_finali.append(punteggio[::-1])
    giocatori = ""
    for punteggio in punteggi_finali:
        giocatori += punteggio + "\n"
    with open(file, "w") as f:
        f.write(giocatori)
    print("Giocatore aggiunto al database.")


game()
