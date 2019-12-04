'''
Resumen:
    Devuelve la potencia necesaria para mover un caudal determinado a través de una tubería.

Descripción:
    Este tipo de problema se plantea cuando se quiere utilizar una tubería existente para mover
    un cierto caudal demandado y se desea conocer la bomba que debe ser colocada o la diferencia
    de nivel entre la entrada y la salida de la tubería.

Estructura de la función:
    PotenciaRequerida(Q,L,d,ks,km,p,u,z2,n)

Inputs:
    Q  -- Caudal que fluye por la tubería (Lps).
    L  -- Longitud de la tubería (mts). 
    d  -- Diámetro de la tubería (mts).
    ks -- Rugosidad Absoluta del material (mts).
    km -- Coeficiente de Pérdidas Menores.
    p  -- Densidad del fluido (kg/m^3).
    u  -- Coeficiente de Viscocidad cinemática (m^2/s).
    z2 -- Cota topográfica (mts).
    n  -- Eficiencia de la bomba.

Output:
    P = Potencia necesaria para mover un caudal determinado a través de una tubería (Kwatts).

Programado por:
    Ing. Josue Emmanuel Cruz Barragan
'''

'''Librerias'''
import math
import FactorFriccionColebrookWhite as CW

'''Función principal'''
def PotenciaRequerida(Q,L,d,ks,km,p,u,z2,n):

    '''
    Constantes
    '''
    g = 9.807 # Aceleración de la gravedad
    
    '''
    Número de Reynolds
    '''
    def Reynolds(Q,d,u):
        V = Velocidad(Q,d) 
        return V*d/u

    '''
    Velocidad de flujo
    '''
    def Velocidad(Q,d):
        return Q/(0.25*math.pi*(d**2))

    '''
    Energía por unidad de peso perdida en los accesorios
    '''
    def Suma_hm(V,km,g):
        return km*(V**2)/(2*g)
    
    '''
    Pérdidas de energía por fricción
    '''     
    def Perd_friccion(f,L,V,d,g):
        return f*L*(V**2)/(2*g*d)
            
    '''
    Altura total que debe ser producida por la bomba
    ''' 
    def H_tot(z2,hf,Shm):
        return z2+hf+Shm 
            
    #Cálculo del Número de Reynolds
    Re = Reynolds(Q,d,u)
    #Cálculo de la velocidad de flujo
    V = Velocidad(Q,d)
    #Cálculo de la energía por unidad de peso perdida en los accesorios
    Shm = Suma_hm(V,km,g)
    #Cálculo del factor de fricción 
    f = CW.Colebrook_White(Re,ks,d)
    #Cálculo de las pérdidas de energía por fricción
    hf = Perd_friccion(f,L,V,d,g)
    print(hf)
    #Cálculo de la altura total que debe ser producida por la bomba
    H = H_tot(z2,hf,Shm)

    return p*Q*g*H/(n*1000)
            