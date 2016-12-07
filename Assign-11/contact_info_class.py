#Jon Ham
#CECS174

class Contact:
    #init
    def __init__(self, first_name, last_name, phone_num, address, city, state, zip):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__phone_num = phone_num
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zip = zip

    #Get methods
    def get_first_name(self):
        return self.__first_name
    def get_last_name(self):
        return self.__last_name
    def get_phone_num(self):
        return self.__phone_num
    def get_address(self):
        return self.__address
    def get_city(self):
        return self.__city
    def get_state(self):
        return self.__state
    def get_zip(self):
        return self.__zip

    #Set methods
    def set_first_name(self, info):
        self.__first_name = info
    def set_last_name(self, info):
        self.__last_name = info
    def set_phone_num(self, info):
        self.__phone_num = info
    def set_address(self, info):
        self.__address = info
    def set_city(self, info):
        self.__city = info
    def set_state(self, info):
        self.__state = info
    def set_zip(self, info):
        self.__zip = info

    #string
    def __str__(self):
        return self.__first_name+" "+self.__last_name+"\n"+str(self.__phone_num)+"\n"+str(self.__address)+"\n"+self.__city+" "+self.__state+" "+str(self.__zip)
