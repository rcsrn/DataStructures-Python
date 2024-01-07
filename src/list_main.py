from my_list import List
from my_list import Element

list = List()
element = Element("Primer elemento")
print("Lista antes de agregar:")
print(list.get_length())
print(list)

list.add_at(element, 0)

print("Lista despues de agregar un elemento:")
print(list.get_length())
print(list)

for i in range(5):
    list.add_at(Element("medio"), 1)

list.add_at(Element("Nuevo"), 1)
list.add_at(Element("Medio"), 1)
list.add_at(Element("Metido"), 3)

list.add_at(Element("X"), list.get_length())
list.add_at(Element("Penultimo"), list.get_length())
list.add_at(Element("Ultimo"), list.get_length())
list.add_at(Element("Nuevo Primero"), 0)

list.add_at(Element("Quinto"), 4)
    
print("Lista despues de agregar multiples elementos al inicio:")
print(list.get_length())
print("Iterando Lista ************************")
for e in list:
    print(e)
print("**************************************")


new_list = List.from_list(list)
print(new_list)
