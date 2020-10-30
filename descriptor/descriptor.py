class Value:
    def __init__(self):
        self.value = None
    
    def __set__(self, obj, value):
        self.value = value - value * obj.commission
        return self.value
    def __get__(self, obj, obj_type):
        return self.value

       

class Account:
    amount = Value()
    def __init__(self, commission):
        self.commission = commission
