import os
import time

def forca(x=0):
  if x==0:
    print("------------")
    print("|          |")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|")
  elif x==1:
    print("------------")
    print("|          |")
    print("|          0")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|")
  elif x==2:
    print("------------")
    print("|          |")
    print("|          0")
    print("|          |")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|")
  elif x==3:
    print("------------")
    print("|          |")
    print("|          0")
    print("|         -|")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|")
  elif x==4:
    print("------------    ")
    print("|          |    ")
    print("|          0    ")
    print("|         -|-   ")
    print("|               ")
    print("|               ")
    print("|               ")
    print("|")
  elif x==5:
    print("------------    ")
    print("|          |    ")
    print("|          0    ")
    print("|         -|-   ")
    print("|         /      ")
    print("|               ")
    print("|               ")
    print("|")
  elif x==6:
    print("------------    ")
    print("|          |    ")
    print("|          0    ")
    print("|         -|-   ")
    print("|         / \\    ")
    print("|               ")
    print("|    Lamento! Perdeu! ")
    print("|")

erros=0

print("Walter Holthausen")
print("Por Heliberto Dos Santos Pereira");
print("Professora Elizandra Mendes")
print("Turma: 102 EMI")

print("")

print("A arte bizantina é uma arte cristã que surge no periodo em que o cristianismo passa a ser reconhecido como religião. Jesus, considerado uma ameaça para o Imperio Romano, foi perseguido e morto pelos romanos. Após sua morte, seus adeptos se escondiam em catacumbas para rezar, pois continuaram sendo perseguidos!")
time.sleep(30)

print("")  

print("Até que em 313 o imperador Constatino outorgou o Édito de Milão, que proibia a perseguição aos cristão e, então, o Cristianismo começa a crescer. Surgem assim, as igrejas cristãs e um novo estilo de arte, a Arte Bizantina!")
time.sleep(30)

print("")
word=input('Informe uma palavra: ');
temp=[]
for letra in word:
    temp.append('_')
    
while True:
    print('\n'*20)
    forca(erros)
    print('\n\nAdivinhe: ', end='')
    for let in temp:
        print(let, end='')
    print('\n'*2)
    if erros==6:
        break
    ganhouJogo=True
    for let in temp:
      if let=='_':
        ganhouJogo=False
    if ganhouJogo:
        print('\nPARABÉNS VENCEDOR!!!')
        break
    letraDig=input("Informe uma letra: ")
    errouLetra=True
    for i, let in enumerate(word):
        if word[i]==letraDig:
          temp[i]=word[i]
          errouLetra=False
    if errouLetra:
        erros=erros+1
