class Player:
    def __init__(self):
        self.__name =" "
        self.__gender =" "
        self.__age = 0
    def setPlayer(self):
        self.__name = input("ENTER YOUR NAME: ")
        self.__gender = input("ENTER YOUR GENDER: ")
        self.__age = int(input("ENTER YOUR AGE: "))
    def showPlayer(self):
        print("Name:", self.__name)
        print("Gender:", self.__gender)
        print("Age:", self.__age)

class Varsity:
    def __init__(self):
        self.__sport =" "
        self.__position =" "
    def setVarsity(self):
        self.__sport =input("ENTER YOUR SPORT: ")
        self.__position = input("ENTER YOUR POSITION: ")
    def showVarsity(self):
        print("SPORT:", self.__sport)
        print("Position:", self.__position)

class Student(Player,Varsity):
    def __init__(self):
        self.__address = " "
        self.__contact = " "
    def setStudent(self):
        self.setPlayer()
        self.__address = input("ENTER YOUR ADDRESS: ")
        self.__contact = input("ENTER YOUR CONTACT NUMBER: ")
        self.setVarsity()

    def showStudent(self):
        self.showPlayer()
        print("Address:", self.__address)
        print("Contact:", self.__contact)
        self.showVarsity()

def main():
    s=Student()
    s.setStudent()
    s.showStudent()
if __name__=="__main__":main()