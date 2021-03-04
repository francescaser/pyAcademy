#Scrivi una funzione “sommatrice” che somma tra loro tutti i numeri che prende in input da tastiera 

def sommatrice() :
    n = int(input('inserisci quanti numeri vuoi: '))
    somma = 0
    
    for i in range(n):
        num = int(input('numero: '))
        somma += num
        
    return print(somma)

