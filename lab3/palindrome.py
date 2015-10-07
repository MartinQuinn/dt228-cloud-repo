#Martin Quinn

Word = raw_input("Please Enter a Word!\n")
x=0

# compares first and last letter
for x in range (len(Word)/2):
  if(Word[x])==(Word[len(Word)-x-1]):
    x += 1
  else:
    t = False

  if x == (len(Word)/2):
    t = True

if t == True:
  print "True"
else:
  print "False"