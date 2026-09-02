#aggregation example customer HAS A RELATIONSHIP with address
class Customer:
    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address

    def print_address(self):
        print(self.address.get_city(),self.address.pincode,self.address.state)


    
class Address:
    def __init__(self,city,pincode,state):
        self.__city=city
        self.pincode=pincode
        self.state=state

    def get_city(self):
        return self.__city

a=Address('Indore',123456,'Madhya Pradesh')
c1=Customer('Ojaswi','Female',a)
c1.print_address()


# what if we want to edit - profile of customer
class Customer:
    def __init__(self,name,gender,address):

        self.name=name
        self.gender=gender
        self.address=address

    def print_address(self):
        print(self.address.city,self.address.pincode,self.address.state)

    def edit_profile(self,new_name,new_city,new_pincode,new_state):
        self.name=new_name
        self.address.change_address(new_city,new_pincode,new_state)
        
        


class Address:
    def __init__(self,city,pincode,state):
        self.city=city
        self.state=state
        self.pincode=pincode

    def change_address(self,new_city,new_pincode,new_state):
        self.city=new_city
        self.pincode=new_pincode
        self.state=new_state

a=Address('Indore',12345,'Madhya Pradesh')
c1=Customer('Ojaswi','Female',a)
c1.print_address()
c1.edit_profile('Mohit','Pune',12568,'Maharashtra')
c1.print_address()






