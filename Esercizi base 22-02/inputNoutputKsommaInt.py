# programma che riceve in ingresso un numero positivo N e 
# determina il massimo K tale che la somma dei primi K interi sia
# minore o unguale a N 
# Es. N=20 --> K=5, perchè 1+2+3+4+5=15

N=int(input('Inserisci un numero N: '))
somma = 0
K = 0
while somma <= N:
    somma = K*(K+1)/2
    if somma <= N:
        K += 1
    else:
        K = K - 1
print('Il massimo K tale che la somma dei primi K interi sia minore o unguale a N è: ', K)

