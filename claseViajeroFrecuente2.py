class ViajeroFrecuente:
    __numero=""
    __documento=""
    __nombre=""
    __apellido=""
    __millas=""
    
    def __init__(self, numero, documento, nombre, apellido, millas):
        self.numero = numero
        self.documento = documento
        self.nombre = nombre
        self.apellido = apellido
        self.millas = millas
    
    def __gt__(self, otro):
        return self.millas > otro.millas
    
    def __add__(self, millas):
        return ViajeroFrecuente(self.numero, self.documento, self.nombre, self.apellido, self.millas + millas)
    
    def __sub__(self, millas):
        return ViajeroFrecuente(self.numero, self.documento, self.nombre, self.apellido, self.millas - millas)
