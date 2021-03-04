# funzione che, data una lista di numeri, fornisce in output un
# istogramma basato su questi numeri, usando asterischi per disegnarlo.
# Ad esempio, data la lista [3,7,9,5] deve produrre questo grafico:
# ***
# *******
# *********
# *****


def istogramma():
    stampa=''
    while 3>1:
        num=int(input('Inserisci un numero: '))
        if num<0:
          print('Inserisci un numero maggiore di zero: ')
        elif num == 0:
          break
        for k in range(0, num):
           stampa = stampa + '*'
        stampa = stampa +'\n'
    print(stampa)
          
