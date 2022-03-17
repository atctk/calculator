def plus(a,b):
  return int(a)+int(b)

def minus(a,b):
  return int(a)-int(b)

def mul(a,b):
  return int(a)*int(b)

def div(a,b):
  return int(a)/int(b)

def remain(a,b):
  return int(a)%int(b)

def power(a,b):
  return int(a)**int(b)

def negation(a):
  return (-int(a))

print(plus(3,"7"))
print(minus("7",3))
print(mul(3,"7"))
print(div("10",2))
print(remain(9,"3"))
print(power("3",7))
print(negation("3"))