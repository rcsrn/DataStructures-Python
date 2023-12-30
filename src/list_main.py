from my_list import List
from my_list import Element

list = List()
element = Element("Primer elemento")
print("Lista antes de agregar:")
print(list.getLength())
print(list)

list.add_at(element, 0)

print("Lista despues de agregar un elemento:")
print(list.getLength())
print(list)

for i in range(5):
    list.add_at(Element("inicio"), 0)

print("Lista despues de agregar multiples elementos al inicio:")
print(list.getLength())
print(list)
