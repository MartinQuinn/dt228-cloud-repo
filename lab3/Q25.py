#Martin Quinn

n1=0
n2=1
sum = n2
var = "" #length

while (len(var)<1000): #while length of number less than 1000 digits 
  sum = n1 + n2 

  var = str(sum) #cast to string

  n1 = n2 
  n2 = sum 

print var