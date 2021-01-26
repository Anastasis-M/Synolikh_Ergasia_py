#Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει τις διαστάσεις ενός ορθογωνίου και θα φτιάχνει μέσα από λίστες τον αντίστοιχο πίνακα.  DONE
#Στην συνέχεια θα βρίσκει το πλήθος των θέσεων και γεμίζει στην τύχη τις μισές με S και τις μισές με O (στρογγυλοποίηση προς τα πάνω). DONE
#Σκοπός είναι να μετρήσετε πόσες φορές εμφανίζεται το SOS οριζόντια, κάθετα,DONE---> και διαγώνια. Το πρόγραμμα επαναλλαμβάνεται 100 φορές (για τις ίδιες διαστάσεις) και επιστρέφει τον μέσο όρο των τριάδων SOS.

import random
xd = int(input("Δώσε την οριζόντια διάσταση: "))
yd = int(input("Δώσε την κατακόρυφη διάσταση: "))
sos = 0
for u in range(0,100):

  a = (xd * yd) / 2 
  if xd*yd % 2 >0 :
    a =int( a + 0.5 )

  b = (xd * yd) / 2
  if xd*yd % 2 >0 :
    b =int( b - 0.5 )


  arr = ["S"]*int(a) + ["O"]*int(b)
  random.shuffle(arr)
  arr = [arr[i:i+xd] for i in range(0, xd*yd, xd)] 
  
  c = 0
  #οριζόντια
  while c+2-xd < 0 :
    for g in range(0,  yd) :
      if arr[g][c] == "S" and arr[g][c+1] == "O" and arr[g][c+2] == "S":
        sos  = sos + 1
    c = c + 1	

  c = 0
  #κάθετα
  while c+2-yd < 0 :
    for m in range(0,  xd) :
      if arr[c][m] == "S" and arr[c+1][m] == "O" and arr[c+2][m] == "S":
        sos  = sos + 1
    c = c + 1
  
  #διαγώνια από αριστερά προς τα δεξιά
  for i in range(-yd+3,xd-2):
    if yd <= xd : 
      if i < 0 :  
        for j in range(0, yd-2-abs(i)):
          if arr[-i+j][j]=="S" and arr[-i+j+1][j+1]=="O" and arr[-i+j+2][j+2] =="S" :
            sos = sos + 1           
      elif i <= xd - yd:
        for j in range(0, yd -2):
          if arr[j][i+j] =="S" and arr[j+1][i+j+1] =="O" and arr[j+2][i+j+2] =="S":
            sos = sos + 1 
      else:   
        for j in range(0, yd-2-abs(i-(xd-yd))):
          if arr[j][i+j] =="S" and arr[j+1][i+j+1] =="O" and arr[j+2][i+j+2] =="S":
            sos = sos + 1    
    else:
      if i < xd - yd :  
        for j in range(0, yd-2-abs(i)):
          if arr[-i+j][j]=="S" and arr[-i+j+1][j+1]=="O" and arr[-i+j+2][j+2] =="S" :
            sos = sos + 1
      elif 0 >= i >= xd - yd:
        for j in range(0, xd -2):
          if arr[-i+j][j] =="S" and arr[-i+j+1][j+1] =="O" and arr[-i+j+2][j+2] =="S":
            sos = sos + 1 
      else:   
        for j in range(0, xd-2-i):
          if arr[j][i+j] =="S" and arr[j+1][i+j+1] =="O" and arr[j+2][i+j+2] =="S":
            sos = sos + 1    

  #διαγώνια από δεξιά προς τα αριστερά
  for i in range(-yd+3,xd-2):
    if yd <= xd : 
      if i < 0 :  
        for j in range(0, yd-2-abs(i)):
          if arr[-i+j][xd-1-j]=="S" and arr[-i+j+1][xd-2-j] =="O" and arr[-i+j+2][xd-3-j] =="S":
            sos = sos + 1           
      elif i <= xd - yd:
        for j in range(0, yd -2):
          if arr[j][-i-j+xd-1] =="S" and arr[j+1][-i-j+xd-2] =="O" and arr[j+2][-i-j+xd-3] =="S":
            sos = sos + 1 
      else:   
        for j in range(0, yd-2-abs(i-(xd-yd))):
          if arr[j][-i-j+xd-1]=="S" and arr[j+1][-i-j+xd-2] =="O" and arr[j+2][-i-j+xd-3] =="S":
            sos = sos + 1   
    else:
      if i < xd - yd :  
        for j in range(0, yd-2-abs(i)):
          if arr[-i+j][xd-1-j]=="S" and arr[-i+j+1][xd-2-j] =="O" and arr[-i+j+2][xd-3-j] =="S":
            sos = sos + 1
      elif 0 >= i >= xd - yd:
        for j in range(0, xd -2):
          if arr[j-i][xd-1-j] =="S" and arr[j-i+1][xd-2-j] =="O" and arr[j-i+2][xd-3-j] =="S":
            sos = sos + 1 
      else:   
        for j in range(0, xd-2-i):
          if arr[j][-i-j+xd-1]=="S" and arr[j+1][-i-j+xd-2] =="O" and arr[j+2][-i-j+xd-3] =="S":
            sos = sos + 1     

#μέσος όρος
mo = sos/100
print(mo)
