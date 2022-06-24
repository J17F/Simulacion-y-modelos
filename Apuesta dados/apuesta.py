#Lanzamiento de dados
#Autor: José Gómez
#Cedula: 27.547.101

from random import randint

def lanzamiento():
  return randint(1,6)

def apuestas(cartera):
  #cartera = 200
  print("Bienvenido a la apuesta")
  print("Cartera inicial:", cartera, "$")
 
  for i in range(0,100):
    apuesta = 10
    dado = lanzamiento()
    if dado % 2 == 0:
      cartera +=10
      print("Dado: ", dado, "Apuesta: ", apuesta, "Ganancia +10$", "Cartera: ", cartera, "$")
    else:
      cartera -=10 
      print("Dado: ", dado, "Apuesta: ", apuesta, "Perdida -10$", "Cartera: ", cartera, "$")
    i = i + 1
  
    if i == 100:
      print("Haz apostado",i,"veces")

    if i == 100 and cartera > 0:
      print("Tu cartera era de 200$ ahora es de:", cartera, "$")
      break
    elif i == 100 and cartera == 0 or cartera == 0: 
      print("PERDISTE en la apuesta: ", i)
      print("Tu cartera era de 200$ ahora es de:", cartera, "$")
      break

    napuesta = i 
    wallet = cartera
  return napuesta, wallet

def corridas():
  corrida = 100
  cartera = 200
  numeroapuestas = 0
  dinero = 0
  while cartera > 0 and corrida > 0 :
    napuesta, wallet = apuestas(cartera)
    numeroapuestas += napuesta
    dinero += wallet
    corrida = corrida - 1
  
  numeroapuestas = numeroapuestas / 100
  print("Promedio de apuestas: ", numeroapuestas)
  dinero = dinero / 100
  print("Promedio de cartera: ", dinero)
  return

main = corridas()