class Employee:
    company = "Panasonic"

    @classmethod
    def display_company(cls, company_name):
        cls.company = company_name
        print(f"Company: {cls.company}")

Employee.display_company("Panasonic") 

class Company:
    department = "Special Projects"

    @classmethod
    def display_department(cls, depart_name):
        cls.department = depart_name

        print(f"Department : {cls.department}") 

class Weapons:
    weapon = "Mac-314"
    
    @classmethod
    def display_weapon(cls, weapon_name):
        cls.weapon = weapon_name
        print(cls.weapon)
    
Weapons.display_weapon("Deasert-Eagle")

# This is updating the class attribute at a Runtime
Company.display_department("Special Projects")
Company.display_department("Normal Projects") 

# A method that works on class data
# Takes cls as the first parameter
# Can access class level data and modify it