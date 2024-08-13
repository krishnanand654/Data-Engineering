#public, protected, private access modifiers

# #protected access modifiers
# class Employee:
#     _name = None
#     _department = None

#     def __init__(self,name, department):
#         self._name = name
#         self._department = department

#     def _display(self):
#         print("Employee Name: ", self._name)
#         print("Employee Dept: ", self._department)

# class EmployeeDetails(Employee):
#     def __init__(self, name, department):
#         super().__init__(name, department)
#     def displayDetails(self):
#         self._display()

# emp = EmployeeDetails("Krishnanand", "IT")
# emp.displayDetails()

#Private Access Modifier
class PEmployee:
    __name = None
    __department = None

    def __init__(self,name, department):
        self.__name = name
        self.__department = department

    def __display(self):
        print("Employee Name: ", self.__name)
        print("Employee Dept: ", self.__department)

class PEmployeeDetails(PEmployee):
    def __init__(self, name, department):
        super().__init__(name, department)
    def displayDetails(self):
        self.__display()

PrivateObj = PEmployeeDetails("something", "It")
PrivateObj.displayDetails()