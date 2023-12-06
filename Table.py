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
Potassium = Element(4, 19, "K", "Potassium", 19, 39.098)
Calcium = Element(4, 20, "Ca", "Calcium", 20, 40.078)
Scandium = Element(4, 3, "Sc", "Scandium", 21, 44.956)
Titanium = Element(4, 4, "Ti", "Titanium", 22, 47.867)
Vanadium = Element(4, 5, "V", "Vanadium", 23, 50.942)
Chromium = Element(4, 6, "Cr", "Chromium", 24, 51.996)
Manganese = Element(4, 7, "Mn", "Manganese", 25, 54.938)
Iron = Element(4, 8, "Fe", "Iron", 26, 55.845)
Cobalt = Element(4, 9, "Co", "Cobalt", 27, 58.933)
Nickel = Element(4, 10, "Ni", "Nickel", 28, 58.693)
Copper = Element(4, 11, "Cu", "Copper", 29, 63.546)
Zinc = Element(4, 12, "Zn", "Zinc", 30, 65.38)
Gallium = Element(4, 13, "Ga", "Gallium", 31, 69.723)
Germanium = Element(4, 14, "Ge", "Germanium", 32, 72.630)
Arsenic = Element(4, 15, "As", "Arsenic", 33, 74.922)
Selenium = Element(4, 16, "Se", "Selenium", 34, 78.971)
Bromine = Element(4, 17, "Br", "Bromine", 35, 79.904)
Krypton = Element(4, 18, "Kr", "Krypton", 36, 83.798)
Rubidium = Element(5, 1, "Rb", "Rubidium", 37, 85.468)
Strontium = Element(5, 2, "Sr", "Strontium", 38, 87.62)
Yttrium = Element(5, 3, "Y", "Yttrium", 39, 88.906)
Zirconium = Element(5, 4, "Zr", "Zirconium", 40, 91.224)
Niobium = Element(5, 5, "Nb", "Niobium", 41, 92.906)
Molybdenum = Element(5, 6, "Mo", "Molybdenum", 42, 95.95)
Technetium = Element(5, 7, "Tc", "Technetium", 43, 98)
Ruthenium = Element(5, 8, "Ru", "Ruthenium", 44, 101.07)
Rhodium = Element(5, 9, "Rh", "Rhodium", 45, 102.91)
Palladium = Element(5, 10, "Pd", "Palladium", 46, 106.42)
Silver = Element(5, 11, "Ag", "Silver", 47, 107.87)
Cadmium = Element(5, 12, "Cd", "Cadmium", 48, 112.41)
Indium = Element(5, 13, "In", "Indium", 49, 114.82)
Tin = Element(5, 14, "Sn", "Tin", 50, 118.71)
Antimony = Element(5, 15, "Sb", "Antimony", 51, 121.76)
Tellurium = Element(5, 16, "Te", "Tellurium", 52, 127.60)
Iodine = Element(5, 17, "I", "Iodine", 53, 126.90)
Xenon = Element(5, 18, "Xe", "Xenon", 54, 131.29)

element_list = [Hydrogen, Helium, Lithium, Beryllium, Boron, Carbon, Nitrogen, Oxygen, Fluorine, Neon, Sodium, Magnesium, Aluminium, Silicon, Phosphorus, Sulfur, Clorine, Argon, Potassium, Calcium, Scandium, Titanium, Vanadium, Chromium, Manganese, Iron, Cobalt, Nickel, Copper, Zinc, Gallium, Germanium, Arsenic, Selenium, Bromine, Krypton, Rubidium, Strontium, Yttrium, Zirconium, Niobium, Molybdenum, Technetium, Ruthenium, Rhodium, Palladium, Silver, Cadmium, Indium, Tin, Antimony, Tellurium, Iodine, Xenon]
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