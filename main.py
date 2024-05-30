import random

def crea_mazzo(semi,valori):
    mazzo = []
    for seme in semi:
        for valore in valori:
            mazzo.append({'seme': seme, 'valore': valore})
    return mazzo

def mischia_mazzo(mazzo):
    for _ in range(random.randint(5, 10)):
        random.shuffle(mazzo)
    return mazzo

def carte_sul_tavolo(mazzo):
    tavolo = []
    for _ in range(4):
        carta = random.choice(mazzo)
        mazzo.remove(carta)
        tavolo.append(carta)
    return tavolo

def estrai_carta (mazzo):
    carta = random.choice (mazzo)
    mazzo.remove (carta)
    return carta

def distribuzione_carte(mazzo):
    mano = []
    for _ in range(3):
        carta_estratta = random.choice(mazzo)
        mano.append(carta_estratta)
        mazzo.remove(carta_estratta)
    return mano

def rimuovi_carta_tavolo_giocatore(tavolo, carta_giocata):
    carte_stesso_valore = [carta for carta in tavolo if carta['valore'] == carta_giocata['valore']]
    if len(carte_stesso_valore) > 1:
        carta_aggiunta = random.choice(carte_stesso_valore)
        tavolo.remove(carta_aggiunta)
    else:
        for carta in tavolo:
            if carta['valore'] == carta_giocata['valore']:
                tavolo.remove(carta)
                break
def rimuovi_carta_tavolo_computer(tavolo, carta_giocata_computer):
    carte_stesso_valore = [carta for carta in tavolo if carta['valore'] == carta_giocata_computer['valore']]
    if len(carte_stesso_valore) > 1:
        carta_aggiunta = random.choice(carte_stesso_valore)
        tavolo.remove(carta_aggiunta)
    else:
        for carta in tavolo:
            if carta['valore'] == carta_giocata_computer['valore']:
                tavolo.remove(carta)
                break

def main():
    nuova_partita = True
    while nuova_partita == True:
        punti_giocatore = 0
        punti_computer = 0
        nome_giocatore = input('Inserisci il tuo nome: ')
        mazzo = crea_mazzo (['denari','bastoni','coppe','spade'],[1,2,3,4,5,6,7,8,9,10])
        tavolo = carte_sul_tavolo(mazzo)
        mazzo = mischia_mazzo(mazzo)
        mano_giocatore = distribuzione_carte(mazzo)
        mano_computer = distribuzione_carte(mazzo)
        primo_giocatore = 'giocatore'

        while len(mano_giocatore) > 0 and len(mano_computer) > 0:
            if primo_giocatore == 'giocatore':
                if len(mano_giocatore) == 3:
                    for carta in tavolo:
                        print(f"{carta['valore']} di {carta['seme']}")
                    print('----------------------------------------------------------------------------------------------------------------------------')
                    print(f"{mano_giocatore[0]['valore']} di {mano_giocatore[0]['seme']},{mano_giocatore[1]['valore']} di {mano_giocatore[1]['seme']},{mano_giocatore[2]['valore']} di {mano_giocatore[2]['seme']}") 
                elif len(mano_giocatore) == 2:
                    for carta in tavolo:
                        print(f"{carta['valore']} di {carta['seme']}")
                    print('----------------------------------------------------------------------------------------------------------------------------')
                    print(f"{mano_giocatore[0]['valore']} di {mano_giocatore[0]['seme']},{mano_giocatore[1]['valore']} di {mano_giocatore[1]['seme']}")
                elif len(mano_giocatore) == 1:
                    for carta in tavolo:
                        print(f"{carta['valore']} di {carta['seme']}")
                    print('----------------------------------------------------------------------------------------------------------------------------')
                    print(f"{mano_giocatore[0]['valore']} di {mano_giocatore[0]['seme']}")
                carta_scelta = int(input(f'{nome_giocatore}, scegli la carta da giocare 1/2/3: '))
                while carta_scelta not in [1, 2, 3,]:
                    print('inserisci un numero valido 1/2/3!!!')
                    carta_scelta = int(input(f'{nome_giocatore}, scegli la carta da giocare 1/2/3: '))
                carta_scelta -= 1
                carta_giocata = mano_giocatore[carta_scelta]
                mano_giocatore.remove(carta_giocata)
                if len(mazzo) > 0:
                    carta_estratta_giocatore = estrai_carta(mazzo)
                    mano_giocatore.append(carta_estratta_giocatore)

            elif primo_giocatore == 'computer':
                carta_giocata_computer = random.choice(mano_computer)
                mano_computer.remove(carta_giocata_computer)
                print(f'Il computer ha messo {carta_giocata_computer}')
                print('----------------------------------------------------------------------------------------------------------------------------')
                if len(mazzo) > 0:
                    carta_estratta_computer = estrai_carta(mazzo)
                    mano_computer.append(carta_estratta_computer)
            
            if primo_giocatore == 'giocatore':
                if carta_giocata['valore'] in [carta['valore'] for carta in tavolo]:
                    rimuovi_carta_tavolo_giocatore(tavolo, carta_giocata)
                    punti_giocatore += 2
                else:
                    tavolo.append(carta_giocata)
            
            if primo_giocatore == 'computer':
                if carta_giocata_computer['valore'] in [carta['valore'] for carta in tavolo]:
                    rimuovi_carta_tavolo_computer(tavolo, carta_giocata_computer)
                    punti_computer += 2
                else:
                    tavolo.append(carta_giocata_computer)
            
            if len(mano_giocatore) == 0 and len(mano_computer) == 0:
                if primo_giocatore == 'giocatore':
                    punti_giocatore += len(tavolo)
                if primo_giocatore == 'computer':
                    punti_computer += len(tavolo)
            
            if primo_giocatore == 'giocatore':
                primo_giocatore = 'computer'
            elif primo_giocatore == 'computer':
                primo_giocatore = 'giocatore'
                    
        if punti_giocatore > punti_computer:
            print(f'{nome_giocatore} ha vinto la partita con {punti_giocatore}.')
        elif punti_giocatore < punti_computer:
            print(f'Il computer ha vinto la partita con {punti_computer}.')
        elif punti_giocatore == punti_computer:
            print('Pareggio.')

        rematch = input("Vuoi fare un'altra partita? (s/n) ")
        while rematch not in ['s', 'n']:
            print('Inserisci una scelta valida s/n!!!')
            rematch = input("Vuoi fare un'altra partita? (s/n) ")
        if rematch == 's':
            nuova_partita = True
            print(f'{nome_giocatore} si siede nuovamente al tavolo.')
        elif rematch == "n":
            nuova_partita = False
            print(f'{nome_giocatore} si alza dal tavolo.')
        else:
            pass

main()