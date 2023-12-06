from Element import Element
import re

Hydrogen = Element(1, 1, "H", "Hydrogen", 1, 1.008)
Helium = Element(1, 8, "He", "Helium", 2, 4.0026)
Lithium = Element(2, 1, "Li", "Lithium", 3, 6.94)
Beryllium = Element(2, 2, "Be", "Beryllium", 4, 9.0122)
Boron = Element(2, 13, "B", "Boron", 5, 10.81)
Carbon = Element(2, 14, "C", "Carbon", 6, 12.011)
Nitrogen = Element(2, 7, "N", "Nitrogen", 7, 14.007)
Oxygen = Element(2, 16, "O", "Oxygen", 8, 15.999)
Fluorine = Element(2, 17, "F", "Fluorine", 9, 18.998)
Neon = Element(2, 18, "Ne", "Neon", 10, 20.180)
Sodium = Element(3, 1, "Na", "Sodium", 11, 22.990)
Magnesium = Element(3, 2, "Mg", "Magnesium", 12, 24.305)
Aluminium = Element(3, 13, "Al", "Aluminium", 13, 26.982)
Silicon = Element(3, 14, "Si", "Silicon", 14, 28.085)
Phosphorus = Element(3, 15, "P", "Phosphorus", 15, 30.974)
Sulfur = Element(3, 16, "S", "Sulfur", 16, 32.06)
Clorine = Element(3, 17, "Cl", "Clorine", 17, 35.45)
Argon = Element(3, 18, "Ar", "Argon", 18, 39.948)

element_list = [Hydrogen, Helium, Lithium, Beryllium, Boron, Carbon, Nitrogen, Oxygen, Fluorine, Neon, Sodium, Magnesium, Aluminium, Silicon, Phosphorus, Sulfur, Clorine, Argon]

def findElement(userInput):

    if re.search("[1-9]", userInput):
        for i in range(len(element_list)):
            if int(userInput) == element_list[i].atomic_number:
                return element_list[i]
        
    elif len(userInput) <= 2:
        for i in range(len(element_list)):
            if userInput.upper() == element_list[i].symbol.upper():
                return element_list[i]
            
            elif i == 18:
                print("Not an element or spelled incorrenctly.")
        
    elif len(userInput) > 2:
        for i in range(len(element_list)):
            if userInput.upper() == element_list[i].name.upper():
                return element_list[i]
            
            elif i == 18:
                print("Not an element or spelled incorrectly.")