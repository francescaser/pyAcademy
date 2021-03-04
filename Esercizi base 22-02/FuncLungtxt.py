#Scriviamo il nostro len()! Prende in input una stringa e conta i caratteri (ehi, ricordatevi di non contare lo spazio)

def Lung ( ) :
    stringa= (input('Inserisci una frase o un numero:'))
    numCaratteri = 0


    for lettera in stringa:
        if lettera != " ":
           numCaratteri += 1 
        

    return print('Il numero di caratteri è: ', numCaratteri)
              
