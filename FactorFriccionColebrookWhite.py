'''
Resumen:
    Devuelve el factor de fricción utilizando la ecuacion Colebrook-White.

Descripción:
    Debido a que la ecuación de Colebrook-White es una función compleja, se
    requiere del uso de un método numérico para encontrar el valor de la 
    fricción, es por eso que se usó el método de Newton-Raphson.

Estructura de la función:
    Colebrook_White(Re,ks,d)

Inputs:
    Re -- Número de Reynols.
    ks -- Rugosidad Absoluta del material (mts). 
    d  -- Diámetro de la tubería (mts).

Output:
    f = Factor de fricción.

Programado por:
    Ing. Josue Emmanuel Cruz Barragan
'''

'''Librerias'''
import math

'''Función principal'''
def Colebrook_White(Re,ks,d):

    '''
    Constantes
    '''
    tol = 0.001 # Tolerancia de error
    error = 100 # Error inicial (%)
    
    '''
    Logaritmo base "10" de un número 
    '''
    def Log(var):
        return math.log10(var)
    
    '''
    Logaritmo base "e" de un número 
    '''
    def Ln(var):
        return math.log(var)
    
    '''
    Ecuación Colebrook-White 
    '''
    def Fricc(Re,ks,d,f):
        a = ks/(3.7*d)
        b = 2.51*f/Re

        return -2*Log(a+b)-f
    
    '''
    Derivada de la ecuación Colebrook-White 
    '''
    def Fricc_p(Re,ks,d,f):
        a = -2/Ln(10)
        b = ks/(3.7*d)
        c = 2.51*f/Re
        d = 2.51/Re
        return (a*d/(b+c))-1
    
    '''
    Método Newton-Raphson 
    '''
    while error >= tol:
        if error == 100:
            x1 = 1/math.sqrt(0.001)
            Fxp = Fricc_p(Re,ks,d,x1)
            Fx = Fricc(Re,ks,d,x1)
            x2 = x1 - (Fx/Fxp)
            error = abs((x2-x1)/x2)*100
            x1 = x2
        else:
            Fxp = Fricc_p(Re,ks,d,x1)
            Fx = Fricc(Re,ks,d,x1)
            x2 = x1 - (Fx/Fxp)
            error = abs((x2-x1)/x2)*100
            x1 = x2

    return 1/(x1**2)