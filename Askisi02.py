#Γράψτε ένα κώδικα σε Python ο οποίος ελέγχει αν ο ν όρος της ακολουθίας Fibonacci είναι πρώτος ή όχι. 
#Για να απαντήσετε αν ένας αριθμός p είναι πρώτος θα πρέπει για 20 τυχαίες επιλογές του a να ισχύει ότι a^p=a mod p. Ο κώδικάς σας παίρνει τον όρο της ακολουθίας Fibonacci από το χρήστη.
#Για παράδειγμα:
#5ος όρος είναι ο 5 και είναι πρώτος.
#11ος όρος είναι ο 89 και είναι πρώτος.
#15ος όρος είναι ο 610 και δεν είναι πρώτος
#Στον κώδικα θεώρησα ως πρώτο όρο της ακολουθίας το "1"

import random
def checkifprwtos():
  check = 0
  for i in range(20):
    a = random.randint(1,35)
    if (a**n_epomeno) % n_epomeno == a % n_epomeno :
      check = check + 1
    else:
      print(n,"ος  όρος είναι το",n_epomeno, "και δεν είναι πρώτος")
      break
  if check == 20 :
    print(n,"ος  όρος είναι το",n_epomeno, "και είναι πρώτος")
n = int(input("Ζητείστε θέση όρου: "))
metritis = 2
n3 = 2
n2 = 1
if n == 1 or n == 2  :
  print(n,"ος  όρος είναι το",1, "και δεν είναι πρώτος")
elif n==3 :
  print(n,"ος  όρος είναι το",2, "και είναι πρώτος")
else :
  while metritis < n-1 and n>0:
    n_epomeno = n3 + n2
    n2 = n3 
    n3 = n_epomeno
    metritis = metritis + 1
  n_epomeno = int(n_epomeno)
  checkifprwtos()




