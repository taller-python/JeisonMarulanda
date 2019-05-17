"""Taller python practicando con clases"""


class Compuerta():
    """Clase padre"""
    def __init__(self, inx_, iny_):
        self.inx_ = inx_
        self.iny_ = iny_


class CompuertaAnd(Compuerta):
    """Clase hijo and"""
    def __init__(self, andx, andy):
        self.inx_ = andx
        self.iny_ = andy

    def __str__(self):
        resultado = '0'
        if self.inx_ == '1' and self.iny_ == '1':
            resultado = '1'
        else:
            resultado = '0'
        return 'Compuerta AND: '+resultado


class CompuertaOr(Compuerta):
    """Clase hijo or"""
    def __init__(self, andx, andy):
        self.inx_ = andx
        self.iny_ = andy

    def __str__(self):
        resultado = '0'
        if self.inx_ == '1' or self.iny_ == '1':
            resultado = '1'
        else:
            resultado = '0'
        return 'Compuerta OR: '+resultado

print("Ingresa x: ")
INPUTX_ = input()
print("Ingresa y: ")
INPUTY_ = input()

print('Compuerta AND: ', CompuertaAnd(INPUTX_, INPUTY_))
print('Compuerta OR: ', CompuertaOr(INPUTX_, INPUTY_))
