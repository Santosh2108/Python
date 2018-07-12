def odd_check(a):
  if a%2 != 0:
    return a
def large(a,b):
  if a>b:
    return a
  else:
    return b
  
def main(x,y,z):
  x=odd_check(x)
  y=odd_check(y)
  z=odd_check(z)
  if x and y and z:
    print (large(x,large(y,z)))
    
  elif x and y and not z:
    print (large(x,y))
  elif x and z and not y:
    print (large(x,z))
  elif z and y and not x:
    print (large(z,y))
  elif x and not y and not z:
    print x
  elif y and not x and not z:
    print y
  elif z and not y and not x:
    print z
  else:
    print ("none of them are odd")

x=raw_input("Enter a num")
y=raw_input("Enter a num")
z=raw_input("Enter a num")
x=int(x)
y=int(y)
z=int(z)
main(x,y,z)
