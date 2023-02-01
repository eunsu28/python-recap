for_while = 0
while for_while < 10:
  for_while = for_while + 1
  print(for_while)

tree = 0
while tree < 10:
  tree = tree + 1
  if tree == 10:
    print("you've hit the tree 10 times, tree is going over")
  else:
    print(f"you've hit tree {tree} time(s)")


for i in range(1, 11):
  print("2의 배수 ",i * 2)

fighterjets = ["f117", "f22", "f18", "f16"]
for i in fighterjets:
  print(i)

dic = {"fighter" : "f22", "bomber" : "b25"}
print(dic)

def Sum(a, b):
  return a + b

function = Sum(1, 2)
print(function)

def function1(a, b):
  if a > b:
    return "a is gratest"
  else:
    return "b is gratest"

function2 = function1(2, 1)
print(function2)

def whi(a):
  i = 0
  while i < a:
    i = i + 1
    print(i)

kdjafldja = whi(20)e