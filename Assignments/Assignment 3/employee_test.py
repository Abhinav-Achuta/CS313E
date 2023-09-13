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
    
def main():
    """
    A Main function to create some example objects of our classes. 
    """

    chris = Employee(name="Chris", identifier="UT1")
    print(chris, "\n")

    emma = PermanentEmployee(name="Emma", identifier="UT2",
                              salary=100000, benefits=["health_insurance"])
    print(emma, "\n")


    charlotte = Manager(name="Charlotte", identifier="UT5",
                        salary=1000000, bonus=100000)
    print(charlotte, "\n")


    ###################################
    print("Check Salaries")

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["retirement", "health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")


    print("Charlotte's Salary is:", charlotte.cal_salary(), "\n")

if __name__ == "__main__":
  main()