

# Make the class header
class Element:
    def __init__(self, period, group, symbol, name, \
                atomic_number, atomic_weight):
        # Atomic num = protons
        # Atomic weight = average atomic mass from all isotopes
        # Atomic mass = protons + neutrons
        self.period = period
        self.group = group
        self.symbol = symbol
        self.name = name

        self.atomic_number = atomic_number
        self.atomic_weight = atomic_weight
    
    def getLevels(self):
        return self.period

    def getValenceElectrons(self):
        if self.group <= 2 or self.group >= 13:
            
            if self.group <= 2:
                return self.group

            else:
                return self.group % 10

        else:
            return "These are transistion metals, these may vary."
    
    def getOxyNumber(self):
        valence_electrons = self.getValenceElectrons()

        if type(valence_electrons) == type(""):
            return "Not defined"

        elif valence_electrons > 4:
            return valence_electrons - 8
        
        else:
            return f"+{valence_electrons}"
    
    def __str__(self):
        return (f"Name: {self.name}\nSymbol: {self.symbol}\nGroup: {self.group}\nPeriod: {self.period}\nAtomic Number: {self.atomic_number}\nAtomic Weight: {self.atomic_weight}\nLevels: {self.getLevels()}\nValence Electrons: {self.getValenceElectrons()}\nOxydation Number: {self.getOxyNumber()}")
