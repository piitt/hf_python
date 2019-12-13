class CountFromBy:

  def __init__(self, v: int=0, i: int=1) -> None:
    self.val = v
    self.incr = i


  def increase(self) -> None:
    self.val += self.incr


  def __repr__(self) -> str:
    return str(self.val)


h = CountFromBy(100, 10)
print(h)
print(h.val)
print(h.incr)
h.increase()
print(h.val)

print("------------------")

j = CountFromBy(100, 10)
print(j)
print(type(j))
print(id(j))
print(hex(id(j)))

print("------------------")

i = CountFromBy()
print(i)
print(i.val)
print(i.incr)
i.increase()
print(i.val)

print("------------------")

n = CountFromBy(i=15)
print(n)
print(n.val)
print(n.incr)
n.increase()
print(n.val)