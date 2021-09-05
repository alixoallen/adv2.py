from random import randint
print("""sou seu computador e pensei em um numero de 0 a 10, tente adivinhar !""")
palpite= randint (0,10)
while True:
  a=int(input('qual o seu palpite ?'))
  print('tente mais uma vez...')
  if palpite == a:
    print('parabens voce chegou ao resultado')
    break