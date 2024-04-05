import coeficiente
import numpy as np
def plaque_temp(x,y,t,a,b,alpha,f,lim_1=6,lim_2=6):
    """
    Temperatura al tiempo 't' de la posición '(x,y)'
    x     : filas
    y     : columnas
    lim_1 : límite truncado de la sumatoria externa
    lim_2 : límite truncado de la sumatoria interna
    a     : ancho
    b     : alto
    alpha : coeficiente de difusión térmica
    f     : condición inicial de la placa
    """
    u = 0
    for m in range(1,lim_1):
        for n in range(1,lim_2):
            mu_m       = (m*np.pi) / a
            nu_n       = (n*np.pi) / b
            lamsqrd_mn = alpha * (mu_m**2+nu_n**2)

            oscilatory_comp = np.sin(mu_m*x) * np.sin(nu_n*y)
            decay_com       = np.exp(-lamsqrd_mn*t)
            fourier_coeff   = coeficiente.fourier_coef(m,n,a,b,f)

            u = u + fourier_coeff*decay_com*oscilatory_comp
    
    return u