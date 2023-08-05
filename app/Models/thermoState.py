import CoolProp.CoolProp as CP

class thermoState:
    def __init__(self, fluid, prop1Type, prop1Value, prop1Unit, prop2Type, prop2Value, prop2Unit,prop3Type, prop3Value, prop3Unit):
        self.fluid = fluid
        prop1 = {
            'Type' : prop1Type,
            'Value' : prop1Value,
            'Unit' : prop1Unit
        }
        prop2 = {
            'Type' : prop2Type,
            'Value' : prop2Value,
            'Unit' : prop2Unit
        }
        prop2 = {
            'Type' : prop3Type,
            'Value' : prop3Value,
            'Unit' : prop3Unit
        }
        

