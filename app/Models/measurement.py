class measurement:
    def __init__(self, value, unit):
        self.unit = unit
        self.value = value
        self.listUnit = ['-','degC','degF','K','R','Pa','kPa','MPa','bar','psi','J','kJ','MJ']
        self.baseMult = [1,1,(5/9),1,1.25,1,1E3,1E6,1E5]
        self.baseAdd = [0,273.15, 255.37222,0,273.15,0,0,0]

    def convertBase(self):
        mult = 1;
        add = 0;
        if self.unit == "degC":
            add = -273.15
        elif self.unit == "K":
            add = 0
        elif self.unit == "degF":
            sel