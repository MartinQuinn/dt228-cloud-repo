#Martin Quinn

n1=0
n2=1
sum = n2
var = ""

while (len(var)<1000):
  sum = n1 + n2

  var = str(sum)

  n1 = n2
  n2 = sum

print var