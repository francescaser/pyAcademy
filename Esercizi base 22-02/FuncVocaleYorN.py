# Scrivi una funzione che legga da input una lettera ed il programma risponda se é una vocale
def vocaleYorN():
    lect = input('inserisci una lettera:')
    stringa = 'aeiou'
    
    for i in range(len(stringa)):
        if stringa[i]==lect:
            print(lect,' è una vocale')
        else:
            i+=1
                
vocaleYorN()

