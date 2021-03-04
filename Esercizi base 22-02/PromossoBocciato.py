scritto = int(input("inserisci voto prova scritta: "))


if (scritto < (-8) or scritto >8):
    print('il voto inserito non è valido!')
    scritto = int(input("inserisci voto prova scritta: "))
  
pratica = int(input("inserisci voto prova pratica: ")) 

if (pratica <0 or pratica >24):
    print('il voto inserito non è valido!')
    pratica = int(input("inserisci voto prova pratica: "))

risultatoFinale = scritto + pratica

if scritto<=0 and risultatoFinale>18:
    print('Bocciato!')
elif scritto>0 and risultatoFinale<=18:
    print('Bocciato!')
elif risultatoFinale>30:
    print('Congratulazioni! 30 e lode')
else:
    print('Promosso con:', risultatoFinale)
    


         


