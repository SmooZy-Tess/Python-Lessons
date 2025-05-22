print("------------Number 1------------")

class Animal:
    def speak(self):
        return "издает звук"
    
class MixinSwim:
    def swim(self):
        return "плавает"

class MixinFly:
    def fly(self):
        return "летает"

class Duck(Animal, MixinSwim, MixinFly):
    def speak(self):
        return "кря-кря"

class Penguin(Animal, MixinSwim):
    def speak(self):
        return "буль-буль"
    
animals = [Duck(), Penguin()]

for animal in animals:
    print(animal.speak())
    print(animal.swim())
    try:
        print(animal.fly())
    except:
        pass
    
print("------------Number 2------------")

class Writer:
    def write(self):
        return "пишет текст"

class Painter:
    def draw(self):
        return "рисует картину"
    
class CreativePerson(Writer, Painter):
    def write(self):
        return "творчески пишет стихотворение"
    
    def draw(self):
        return "выразительно рисует пейзаж"
    
persons = [Writer(), Painter(), CreativePerson()]

for person in persons:
    # try:
    #     print(person.write())
    # except:
    #     pass

    # try:
    #     print(person.draw())
    # except:
    #     pass

    if isinstance(person, Writer):
        print(person.write())
    if isinstance(person, Painter):
        print(person.draw())

