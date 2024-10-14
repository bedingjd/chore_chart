from enum import Enum, Flag, auto


class CHORE_STATUS(Flag):
    TODO : int = 1
    DONE : int = 2
    LATE : int = 4


class DAY(Enum):
    SUNDAY : int = 0
    MONDAY : int = 1
    TUESDAY : int = 2
    WEDNESDAY : int = 3
    THURSDAY : int = 4
    Friday : int = 5
    SATURDAY : int = 6


class Person:
    def __init__(self, name, icon = "icons/lemonadepixel_kidschores-21.jpg"):
        self.name = name
        self.icon = icon
        self.bank = 0.0
        self.listOChores = set()
        return
    def deposit(self, amount):
        self.bank += amount
        return
    def getBankBalance(self):
        return self.bank
    def addChore(self, chore):
        self.listOChores.add(chore)
        return
    def getChores(self):
        return self.listOChores
    def getName(self):
        return self.name
    def getIcon(self):
        return self.icon
    def getBank(self):
        return self.bank
    
    

class Chore:
    def __init__(self, id, chore_name, person, value):
        self.chore_name = chore_name
        self.person = person
        self.status = CHORE_STATUS.TODO
        self.value = value
        self.chore_icon = "icons/lemonadepixel_kidschores-75.jpg"
        self.id = id
        return

    def setIcon(self, icon):
        self.chore_icon = icon
        return

    def upDateStatus(self, status):
        # union (or) the current status with the new status.  This allows us to track late completions
        self.status = self.status | status
        return
    
    def getID(self):
        return self.id
    
    def getPerson(self):
        return self.person

class Chore_System:
    def __init__(self):
        self.listOPeople = set()
        self.listOfChores = set()
        self.nextID = 0
        return
    def addPerson(self, person):
        self.listOPeople.add(person)
        return
    def addPerson(self, name, icon = "icons/lemonadepixel_kidschores-21.jpg"):
        self.listOPeople.add(Person(name, icon))
        return
    def getPeople(self):
        return self.listOPeople
        return
    def addChore(self, chore_name, person, value):
        self.listOfChores.add(Chore(self.nextID, chore_name, person, value))
        self.nextID += 1
        return
    def getChores(self):
        return self.listOfChores
    def getSpecificChore(self, id):
        for c in self.listOfChores:
            if (id == c.getID()):
                return c


if __name__ == "__main__":
    cs = Chore_System()

    dad = Person("dad")
    '''
    takeOutTrash = Chore("Take out trash", dad, 0.50)
    dad.addChore(takeOutTrash)
    '''
    cs.addPerson(dad)
    cs.addChore("take out trash", dad, 0.25)
    cs.addChore("Take trash bin to curb", dad, 0.50)

    for c in cs.getChores():
        print(f"{c.getID()} | Chore: {c.chore_name} | {c.getPerson().getName()} | status: {c.status}")
    

    




