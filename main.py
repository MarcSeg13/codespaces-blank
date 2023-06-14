joc = 1
correcte=0
fallades=0
import random
import colorama
repe='si'
nom=input('escribe tu nombre:   ')
pir={
  '1':{
    '1':['¿capital de Francia?','paris','piensa en una bagette, i tambien en la letra p'], 
    '2':['¿De qué color es el sol?','blanco','union de colores aditivos'], 
    '3':['¿Qué fruto seco lleva en su interior un Ferrero Rocher?','avellana','su temporada es en otoño'],
    '4':['¿Que rango militar tuvo Napoleon?','general','quien dirige las tropas?'],
    '5':['¿Cuántos anillos tiene el logotipo de la marca de coches Audi?','4','escribelo en numeros'],
    '6':['De que nombre proviene el nombre del pais Colombia? ','cristobal colon','quien descubrio America?'],
    '7':['Cual es el bixo mas grande del mundo? ','irene la patata','no tiene pito, pero ella dice que si?'],
         },
  '2':{
    '1':['¿Cuál es el apellido de la reina Isabel II de Inglaterra?','windsor','piensa en viento en inglés'], 
    '2':['¿Quién inventó la bombilla?','thomas edison','las iniciales son T.E.'], 
    '3':['Cómo se llama el pan con chorizo típico de Asturias?','bollo preñao','cuando mama bollo y papa bollo se quieren mucho'],
    '4':['¿Qué fruta tiene como nombre científico Mangifera indica','mango','lee el nombre dos veces'],
    '5':['¿Cuántos años duró la Guerra de los Cien Años?','116','diez años mas, diez años menos'],
    '6':['¿Qué faraón egipcio es conocido por haber intentado que su imperio pasase del politeísmo al monoteísmo a través del culto al dios Atón?','akenaton','tambien llamado Amenhotep IV'],
         },
  '3':{
    '1':['¿En relación a su tamaño, ¿cuál es el músculo más potente del cuerpo humano?','masetero','se encuentra en la cara'], 
    '2':['¿Cuántos colores tiene el cubo Rubik 16x16?','6','colores bro, colores'], 
    '3':['¿dos ultimas palabras del título del primer disco de Camarón?','flores lloran','las tres primeras son ^al verte las...^'],
    '4':['¿Quién fue el primer presidente de Estados Unidos','george washington','un estado tiene su nombre'],
    '5':['¿Como se llama el funador de la religion conocida como Movimiento de los Santos de los Ultimos Días?','joseph smith','tiene el apellido del actor estadounidense Will S.'],
    '6':['¿En qué deporte se podría hacer un "grito paralelo"?','esqui','este se hace sobre hielo'],
         }
  
}
from colorama import init, Fore
init(autoreset=True)
be=0
while be!=2:
  while be==0:
    try:
      d=input('escoge un nivel de dificultad entre 1 y 3:  ')
      d=int(d)
      if type(d)==int:
        be=1
    except ValueError:
      print('ha de ser un numero!!!')
  while not(d>0 and d<4) or be==1:
    try:
      if type(d)==int and (d>0 and d<4):
        be=2
    except ValueError:
      be=1
    while type(d)!=int or be!=2:
      try:
        print('un numero entre el 1 i el 3!!!')
        d=input('escoge un nivel de dificultad entre 1 y 3:  ')
        d=int(d)
        if type(d)==int and (d>0 and d<4):
          be=2
      except ValueError:
        print('ha de ser un numero!!!')
repeticions=input('quieres que se repitan las preguntas falladas?  ')
repeticions=repeticions.strip()
repeticions=repeticions.lower()
while not(repeticions=='si' or repeticions=='no'):
  print('contesta si o no')
  repeticions=input('quieres que se repitan las preguntas falladas?  ')
  repeticions=repeticions.strip()
  repeticions=repeticions.lower()
if d==1:
  ndvides=5
  ndpistes=2
  rendpistes=ndpistes 
  ndpistes2=[1,2]
  n_lletres=25
  m=30
  d=str(d)
  print(f'tienes un total de {m} caracteres, {ndvides} vidas, {ndpistes} pistas para un total de {len(pir[d].keys())} preguntas')
elif d==2:
  ndvides=4
  ndpistes=1
  rendpistes=ndpistes 
  n_lletres=20
  ndpistes2=[1,2]
  m=25
  d=str(d)
  print(f'tienes un total de {m} caracteres, {ndvides} vidas, {ndpistes} pistas para un total de {len(pir[d].keys())} preguntas')
else:
  ndvides=3
  ndpistes=1
  rendpistes=ndpistes 
  n_lletres=20
  ndpistes2=[1,2]
  m=20
  d=str(d)
  print(f'tienes un total de {m} caracteres, {ndvides} vidas, {ndpistes} pistas para un total de {len(pir[d].keys())} preguntas')
while joc ==1 and repe=='si':
  pregunta_acabada=0
  ndpistes=rendpistes
  ndpistes2=[1,2]
  e=list(pir[d].keys())
  e=random.choice(e)
  pregunta=pir[d].get(e)
  pi=pregunta[2]
  r=pregunta[1]
  pregunta=pregunta[0]
  rlen=len(r)
  print(pregunta)
  respostatotal=0
  while pregunta_acabada!=1 and joc==1:
    resposta=input('escribe tu respuesta:  ')
    resposta=resposta.lower()
    nlletres=int(len(resposta))
    respostatotal=nlletres+respostatotal
    while nlletres>n_lletres and pregunta_acabada!=1:
      print('has superado el límite de caracteres, escribe una respuesta mas corta')
      respostatotal=respostatotal-nlletres
      resposta=input('escribe tu respuesta:  ')
      resposta=resposta.lower()
      nlletres=int(len(resposta))
      respostatotal=nlletres+respostatotal
      
    if nlletres<n_lletres:
      if r==resposta:
        print(Fore.GREEN + r)
        correcte=correcte+1
        pir[d].pop(e)
        pregunta_acabada=pregunta_acabada+1
        if ndvides<=0 or len(pir[d].keys())==0:
            print("se ha acabado el juego")
            joc=0
            d=int(d)
            if d!=3:
              repe=input('quieres subir de nivel?  ')
              repe=repe.strip()
              repe=repe.lower()
              while not(repe=='si' or repe=='no'):
                print('escribe si o no')
                repe=input('quieres subir de nivel?   ')
                repe=repe.strip()
                repe=repe.lower()
              if repe=='si':
                joc=1
                d=d+1
                d=str(d)
              #poner lo de procesando y los puntitos
              else:
                print(f'has tenido un total de {correcte} preguntas correctas i {fallades} de falladas')
                print('hasta la vista')
            else:
              repe=input('quieres hacer otro nivel?   ')
              repe=repe.strip()
              repe=repe.lower()
              while not(repe=='no' or repe=='si'):
                print('escoge si o no')
                repe=input('quieres hacer otro nivel?  ')
                repe=repe.strip()
                repe=repe.lower()
              if repe=='si':
                be=0
                while be!=2:
                  while be==0:
                    try:
                      d=input('escoge un nivel  ')
                      d=int(d)
                      if type(d)==int:
                        be=1
                    except ValueError:
                      print('ha de ser un numero!!!')
                  while not(d>0 and d<4) or be==1:
                    try:
                      if type(d)==int and (d>0 and d<3):
                        be=2
                    except ValueError:
                      be=1
                    while type(d)!=int or be!=2:
                      try:
                        print('un numero entre el 1 i el 3!!!')
                        d=input('escoge un nivel:  ')
                        d=int(d)
                        if type(d)==int and (d>0 and d<3):
                          be=2
                      except ValueError:
                        print('ha de ser un numero!!!')
                d=str(d)
                joc =1
                
              #poner lo de procesando y los puntitos
              else:
                print(f'has tenido un total de {correcte} preguntas correctas i {fallades} de falladas')
                print('hasta la vista')                   

        
        
      elif r!=resposta:
        patata=''
        n=0
        for i in range(nlletres):
          lresposta=resposta[i]
          patata=(patata+lresposta)
          listapatata=list(patata)
          
        lletra=0
        letrasalida=-1
        if nlletres==0:
          listapatata=''
        p=0
        j=len(listapatata)
        limit=0 
        while limit<j:
          if letrasalida<rlen-1:
            letrasalida=letrasalida+1
          else:
            p=1
          trobada=0
          lletra=0
          if r[letrasalida]==listapatata[limit] and p==0:
            print(Fore.GREEN + listapatata[limit], end='')
            trobada=1
          while trobada!=1 and not(limit>=j) and lletra<=rlen-1:
            tf=({listapatata[limit]}=={r[lletra]})
            if tf==True:
              print(Fore.YELLOW + listapatata[limit], end='')
              trobada=1
            else:
              if lletra<=nlletres-1:
                lletra=lletra+1        
              else:
                if p==1:
                  lletra=0
                  limit=limit+1
                if p==0:
                  lletra=lletra+1
          if trobada==1:
            limit=limit+1
            lletra=0
          else:
            if j<rlen:
              print(Fore.RED + listapatata[letrasalida], end='')
              limit=limit+1
              
            elif j>=rlen:
              print(Fore.RED + listapatata[limit], end='')
              limit=limit+1
            
        print('')
        resta=(m-respostatotal)
        
        if resta<rlen and pregunta_acabada!=1:
          pregunta_acabada=1
          if resta>0:
            print('no tienes letras suficientes')
          else:
            print("te has quedado sin letras")
          ndvides=ndvides-1
          fallades=fallades+1
          if repeticions=='no':
            pir[d].pop(e)
          print(f'te quedan {ndvides} vidas')
          if ndvides<=0 or len(pir[d].keys())==0:
            print("se ha acabado el juego")
            joc=0
            print(f'has tenido un total de {correcte} preguntas correctas y {fallades} de falladas')
        elif resta>=rlen and pregunta_acabada!=1:
          print(f'te quedan {resta} caracteres')
          siono=input('quieres una pista?   ')
          siono=siono.strip()
          siono=siono.lower()
          while not(siono=='si' or siono=='no'):
            print('escribe si o no')
            siono=input('quieres una pista?')
            siono=siono.strip()
            siono=siono.lower()
          if siono=='si' and ndpistes>0:
            pista=random.choice(ndpistes2)
            ndpistes=ndpistes-1
            if pista==1:
              print(pi)
            elif pista==2:
              print(f'la palabra tiene un total de {rlen} caracteres')
            ndpistes2.pop(ndpistes2.index(pista))
          elif siono=='no':
            print('bueno vale')
          else:
            print('no te quedan pistas')
    