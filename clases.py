
from unittest import result
from unicodedata import decimal

class finanzas:
    def __init__(self,):
        self.cuentasPersonales = 0.0
    def cuentaTotal(self):
        self.cuentasPersonales = result 
        return result

class ingresos:
    def __init__(self,ingresos):
        finanzas.__init__(self)
        self.ingresos = ingresos
    def sumIngreso(self):
        self.cuentasPersonales = (self.cuentasPersonales + self.ingresos) 
        return self.cuentasPersonales

class egreso:
    def __init__(self, egreso):
        finanzas.__init__(self)
        self.egreso = egreso
    def nuevoEgreso(self): 
        self.cuentasPersonales =(self.cuentasPersonales - self.egreso)
        return self.cuentasPersonales


