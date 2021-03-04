# Crea una funzione che presi in input una stringa (nome) e 
# un carattere (i.e. stringa di lunghezza 1), 
# conti le occorrenze del carattere all’interno della stringa

def find(parola, lettera):
    
    contatore = 0
    i = 0
    while i<len(parola):
        if parola[i]==lettera:
            contatore += 1
        i+=1
    return contatore


# esiste la funzione parola.count(lettera) per contare l'occorrenza
