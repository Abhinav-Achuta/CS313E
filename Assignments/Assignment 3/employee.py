"""
    File: employee.py
    Description: We updated each class to inherit from another if needed
    and calculate salaries as well as print functions based on specified
    requirements.

    Student Name: Abhinav Achuta
    Student UT EID: aa85934

    Partner Name: Seowon Jeong
    Partner UT EID: sj32632

    Course Name: CS 313E
    Unique Number: 52590
    Date Created: 9/11/23
    Date Last Modified: 9/13/23

    Input: tuples_list is an unsorted list of tuples denoting intervals
    Output: a list of merged tuples sorted by the lower number of the
    interval
"""
class Employee:
    """ Creates a class for Employee """
    def __init__(self, **kwargs):
        self.name = kwargs["name"]
        self.identifier = kwargs["identifier"]

        if "salary" in kwargs:
            self.salary = kwargs["salary"]
        else:
            self.salary = None

    def __str__(self):
        return f"Employee\n{self.name},{self.identifier},{self.salary}"

    def get_name(self):
        """ Returns the name of the employee """
        return self.name


############################################################
############################################################
############################################################

class PermanentEmployee(Employee):
    """ Creates the class permenantemployee that inherits from employee """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.salary = kwargs["salary"]
        self.benefits = kwargs["benefits"]

    def cal_salary(self):
        """ Calculates salary for class PermenantEmployee """
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
    """ Creates the class manager that inherits from employee """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.salary = kwargs["salary"]
        self.bonus = kwargs["bonus"]

    def cal_salary(self):
        """ Calculates salary for manager class """
        new_salary = self.salary + self.bonus

        return new_salary

    def __str__(self):
        return f"Manager\n{self.name},{self.identifier},{self.salary},{self.bonus}"


############################################################
############################################################
############################################################
class TemporaryEmployee(Employee):
    """ creates the class temporaryemployee that inherits from employee """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.salary = kwargs["salary"]
        self.hours = kwargs["hours"]

    def cal_salary(self):
        """ Calculates salary for Temporary employee class """
        real_salary = self.salary * self.hours

        return real_salary

    def __str__(self):
        return f"TemporaryEmployee\n{self.name},{self.identifier},{self.salary},{self.hours}"


############################################################
############################################################
############################################################


class Consultant(TemporaryEmployee):
    """ Creates class consultant that inherits from temporary employee """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.travel = kwargs["travel"]

    def cal_salary(self):
        temp_salary = super().cal_salary()
        travel_bonus = self.travel * 1000

        real_salary = temp_salary + travel_bonus

        return real_salary


    def __str__(self):
        return f"Consultant\n{self.name},{self.identifier},{self.salary},{self.hours},{self.travel}"

############################################################
############################################################
############################################################


class ConsultantManager(Consultant, Manager):
    """ Creates class consultant manager that inherits from consultant and manager """
    def __init__(self,  **kwargs):
        super().__init__(**kwargs)
        super(Manager, self).__init__(**kwargs)

    def cal_salary(self):

        real_salary = self.salary*self.hours + self.travel*1000 + self.bonus

        return real_salary

    def __str__(self):
        return (f"ConsultantManager\n{self.name},{self.identifier},"
                f"{self.salary},{self.hours},{self.travel},"
                f"ConsultantManager\n{self.name},{self.identifier},"
                f"{self.salary},{self.bonus}")


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
