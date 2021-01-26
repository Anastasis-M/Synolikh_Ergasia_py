#Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει την διάσταση ενός τετραγώνου και θα φτιάχνει μέσα από λίστες τον αντίστοιχο πίνακα.
#Στην συνέχεια θα βρίσκει το πλήθος των θέσεων και θα γεμίζει στην τύχη τις μισές με μονάδες (στρογγυλοποίηση προς τα πάνω).
#Σκοπός είναι να μετρήσετε πόσες τετράδες από μονάδες υπάρχουν οριζόντια, κάθετα, και διαγώνια.
#Το πρόγραμμα επαναλλαμβάνεται 100 φορές (για την ίδια διάσταση) και επιστρέφει τον μέσο όρο των τετράδων.


import random
d = int(input("Δώσε την διάσταση: "))
syn = 0
tetr =0
for i in range(0,100):

  #χωρίζω τον πίνακα στα δύο και γεμίζω ανάλογα με 1 και 0
  a = (d**2) / 2 
  if (d**2) % 2 >0 :
    a =int( a + 0.5 )

  b = (d**2) / 2
  if (d**2) % 2 >0 :
    b =int( b - 0.5 )
  
  arr = [1]*int(a) + [0]*int(b)
  random.shuffle(arr)
  
  arr = [arr[i:i+d] for i in range(0, d**2, d)]
  
  #διφορετικός τρόπος για τη δημιουργία του πίνακα
  #matrix = []
  #matrix = [0]*d
  #h = 0
  #for i in range(0, d**2, d):
  #  matrix[h]=arr[i:i+d]
  #  h= h + 1
  
  
  c = 0
  #οριζόντια
  while c+3-d < 0 :
    for g in range(0,  d) :
      if arr[g][c] == arr[g][c+1] == arr[g][c+2] == arr[g][c+3] == 1:
        tetr  = tetr + 1
    c = c + 1
   	
  c = 0
  #κάθετα
  while c+3-d < 0 :
    for m in range(0,  d) :
      if arr[c][m] == arr[c+1][m] == arr[c+2][m] == arr[c+3][m] == 1:
        tetr  = tetr + 1
    c = c + 1
  

  #διαγώνια από αριστερά προς τα δεξιά
  for i in range(-d+4,d-3):
    for j in range(0, d-3-abs(i)):
      if i < 0:
        if arr[-i+j][j]== arr[-i+j+1][j+1] == arr[-i+j+2][j+2] == arr[-i+j+3][j+3] == 1:
          tetr = tetr + 1
      else:
        if arr[j][i+j] == arr[j+1][i+j+1] == arr[j+2][i+j+2] ==arr[j+3][i+j+3] ==1 :
          tetr = tetr + 1     
   
  #διαγώνια από δεξιά προς τα αριστερά
  for i in range(-d+4,d-3):
    for j in range(0, d-3-abs(i)):
      if i < 0:
        if arr[-i+j][d-1-j]== arr[-i+j+1][d-2-j] == arr[-i+j+2][d-3-j] == arr[-i+j+3][d-4-j] == 1:
          tetr = tetr + 1
       
      else:
        if arr[j][-i-j+d-1]== arr[j+1][-i-j+d-2] == arr[j+2][-i-j+d-3] == arr[j+3][-i-j+d-4] == 1:
          tetr = tetr + 1      
#μέσος όρος
mo = tetr/100
print(mo)

