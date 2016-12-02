#Jon Ham
#CECS 174

class Pet:
    #init method
    def __init__(self, name, gender, happiness=4, hunger=5, cleanliness=10, affinity=0, loyalty=0, age = 0):
        self.__hunger = hunger
        self.__cleanliness = cleanliness
        self.__affinity = affinity
        self.__loyalty = loyalty
        self.__happiness = happiness
        self.__name = name
        self.__gender = gender
        self.__age = age
        if gender == 1:
            self.__gender = "him"
        elif gender == 2:
            self.__gender = "her"


    #feeds the turtle
    def feed(self):
        self.__hunger -= 1
        self.__happiness += 1

    #cleans the turtle
    def clean(self):
        self.__cleanliness += 1
        self.__happiness -= 1

    #play with the turtle
    def play(self):
        self.__happiness += 1
        self.__hunger += 1
        self.__cleanliness -= 1

    #train the turtle
    def train(self):
        self.__loyalty += 1
        self.__cleanliness -= 1
        self.__happiness -= 1

    #pet the turtle
    def pet(self):
        self.__affinity += 1
        self.__happiness += 1
        self.__cleanliness -= 1

    #turtle's age
    def pet_age(self):
        self.__age += 1

    ##get methods for each attribute
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_gender(self):
        return self.__gender

    def get_hunger(self):
        return self.__hunger

    def get_cleanliness(self):
        return self.__cleanliness

    def get_affinity(self):
        return self.__affinity

    def get_loyalty(self):
        return self.__loyalty

    def get_happiness(self):
        return self.__happiness

    #checks the values of each attribute to stay within range (1-10)
    def check_values(self):
        if self.__hunger < 0:
            self.__hunger = 0
        elif self.__hunger > 10:
            self.__hunger = 10

        if self.__cleanliness < 0:
            self.__cleanliness = 0
        elif self.__cleanliness > 10:
            self.__cleanliness = 10

        if self.__affinity < 0:
            self.__affinity = 0
        elif self.__affinity > 10:
            self.__affinity = 10

        if self.__loyalty < 0:
            self.__loyalty = 0
        elif self.__loyalty > 10:
            self.__loyalty = 10

        if self.__happiness < 0:
            self.__happiness = 0
        elif self.__happiness > 10:
            self.__happiness = 10


