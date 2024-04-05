import numpy as np
from scipy import integrate

def fourier_coef(m,n, a_lenght, b_height, func):
    """
    Función para calcular el coeficiente de furier (m,n)
    m,n : indices
    a_lenght = ancho de la placa
    b_height = alto de la placa
    func     = Condición inicial del problema T(x,y,0) = func
    """
    inprod_coef = lambda y,x: np.sin((m*x*np.pi)/a_lenght)*np.sin((n*y*np.pi)/b_height)
    igral_arg   = lambda y,x: func(y,x)*inprod_coef(y,x)
    norm_const  = 4/(a_lenght*b_height)

    igral, _    = integrate.dblquad(igral_arg, 0, a_lenght, 0, b_height)
    A_mn        = norm_const*igral

    return A_mn
