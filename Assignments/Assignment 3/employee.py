class Employee:

    def __init__(self, **kwargs):
        self.name = kwargs["name"]
        self.identifier = kwargs["identifier"]
        self.salary = None

    def __str__(self):
        return f"Employee\n{self.name},{self.identifier},{self.salary}"


############################################################
############################################################
############################################################

class PermanentEmployee(Employee):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.salary = kwargs["salary"]
        self.benefits = kwargs["benefits"]

    def cal_salary(self):

        new_salary = None

        if "health_insurance" in self.benefits and "retirement" in self.benefits:
            new_salary = self.salary * 0.7

        elif self.benefits == ["health_insurance"]:
            new_salary = self.salary * 0.9

        elif self.benefits == ["retirement"]:
            new_salary = self.salary * 0.8

        return new_salary

    def __str__(self):
        return f"PermenantEmployee\n{self.name},{self.identifier},{self.salary},{self.benefits}"

############################################################
############################################################
############################################################

class Manager(Employee):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.salary = kwargs["salary"]
        self.bonus = kwargs["bonus"]
    
    def cal_salary(self):
        new_salary = self.salary + self.bonus
        
        return new_salary

    def __str__(self):
        return f"TemporaryEmployee\n{self.name},{self.identifier},{self.salary},{self.bonus}"


############################################################
############################################################
############################################################
class TemporaryEmployee:
    def __init__(self, **kwargs):
        
    
    def cal_salary(self):
        

    def __str__(self):
        

    
############################################################
############################################################
############################################################


class Consultant :
  

    def cal_salary(self):
  

    def __str__(self):
  
############################################################
############################################################
############################################################


class ConsultantManager:
    def __init__(self,  **kwargs):
 

    def cal_salary(self):
 
    def __str__(self):
 


############################################################
############################################################
############################################################





###### DO NOT CHANGE THE MAIN FUNCTION ########

def main():
    """
    A Main function to create some example objects of our classes. 
    """

    chris = Employee(name="Chris", identifier="UT1")
    print(chris, "\n")

    emma = PermanentEmployee(name="Emma", identifier="UT2",
                              salary=100000, benefits=["health_insurance"])
    print(emma, "\n")

    sam = TemporaryEmployee(name="Sam", identifier="UT3", salary=100,  hours=40)
    print(sam, "\n")

    john = Consultant(name="John", identifier="UT4", salary=100, hours=40, travel=10)
    print(john, "\n")

    charlotte = Manager(name="Charlotte", identifier="UT5",
                        salary=1000000, bonus=100000)
    print(charlotte, "\n")

    matt = ConsultantManager(name="Matt", identifier="UT6",
                              salary=1000, hours=40, travel=4, bonus=10000)
    print(matt, "\n")

    ###################################
    print("Check Salaries")

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["retirement", "health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")

    print("Sam's Salary is:", sam.cal_salary(), "\n")

    print("John's Salary is:", john.cal_salary(), "\n")

    print("Charlotte's Salary is:", charlotte.cal_salary(), "\n")

    print("Matt's Salary is:",  matt.cal_salary(), "\n")

if __name__ == "__main__":
  main()



