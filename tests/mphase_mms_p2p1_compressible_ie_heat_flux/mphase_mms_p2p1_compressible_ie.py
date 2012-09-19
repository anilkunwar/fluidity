# This file was *autogenerated* from the file mphase_mms_p2p1_compressible_ie.sage.
from sage.all_cmdline import *   # import sage library
_sage_const_2 = Integer(2); _sage_const_1p0 = RealNumber('1.0'); _sage_const_1p4 = RealNumber('1.4'); _sage_const_1p5 = RealNumber('1.5'); _sage_const_100p0 = RealNumber('100.0'); _sage_const_0p1 = RealNumber('0.1'); _sage_const_0p5 = RealNumber('0.5'); _sage_const_0p707106781 = RealNumber('0.707106781'); _sage_const_0p7 = RealNumber('0.7'); _sage_const_0p8 = RealNumber('0.8'); _sage_const_3p0 = RealNumber('3.0'); _sage_const_0p4 = RealNumber('0.4')
y = var('y')

def function(phi_0, phi_x, phi_y, phi_xy, 
             f_sin_x, f_cos_x, f_sin_y, f_cos_y, f_sin_xy, f_cos_xy, 
             alpha_x, alpha_y, alpha_xy):
    
    f_0 = phi_0 
    f_x = phi_x*(f_sin_x*sin(alpha_x*x) + f_cos_x*cos(alpha_x*x)) 
    f_y = phi_y*(f_sin_y*sin(alpha_y*y) + f_cos_y*cos(alpha_y*y)) 
    f_xy = phi_xy*(f_sin_xy*sin(alpha_xy*x*y/pi) + f_cos_xy*cos(alpha_xy*x*y/pi)) 
    f = f_0 + f_x + f_y + f_xy
    return f
             
rho1 = _sage_const_0p5 *(sin(x*x + y*y) + _sage_const_1p5 )
rho2 = _sage_const_3p0 

ie1 = _sage_const_0p5 *(cos(x + y) + _sage_const_1p5 )
ie2 = _sage_const_3p0 *y

u1 = _sage_const_1p0 *(sin(x**_sage_const_2 +y**_sage_const_2 )+_sage_const_0p5 )
v1 = _sage_const_0p1 *(cos(x**_sage_const_2 +y**_sage_const_2 )+_sage_const_0p5 )

u2 = _sage_const_1p0 *(sin(x**_sage_const_2 +y**_sage_const_2 )+_sage_const_0p5 )
v2 = _sage_const_0p1 *(cos(x**_sage_const_2 +y**_sage_const_2 )+_sage_const_0p5 )
 
gamma = _sage_const_1p4 
rho0 = _sage_const_0p5 
csq = _sage_const_100p0 
#p = csq*(rho1 - rho0)
p = (gamma-_sage_const_1p0 )*ie1*rho1
             
vfrac1 = _sage_const_0p8 
vfrac2 = _sage_const_1p0  - vfrac1
             
nu1 = _sage_const_0p7 
nu2 = _sage_const_0p7 

g_x = _sage_const_0p707106781 
g_y = _sage_const_0p707106781 

tau_xx1 = nu1*diff(u1,x)            
tau_yy1 = nu1*diff(v1,y)
tau_xy1 = nu1*diff(u1,y)
tau_yx1 = nu1*diff(v1,x)  

tau_xx2 = nu2*diff(u2,x)            
tau_yy2 = nu2*diff(v2,y)
tau_xy2 = nu2*diff(u2,y)
tau_yx2 = nu2*diff(v2,x)  

Su1 = vfrac1*rho1*u1*diff(u1,x) + vfrac1*rho1*v1*diff(u1,y) - diff(vfrac1*tau_xx1, x) - diff(vfrac1*tau_xy1, y) - vfrac1*g_x*rho1 + vfrac1*diff(p,x)  
Sv1 = vfrac1*rho1*u1*diff(v1,x) + vfrac1*rho1*v1*diff(v1,y) - diff(vfrac1*tau_yy1, y) - diff(vfrac1*tau_yx1, x) - vfrac1*g_y*rho1 + vfrac1*diff(p,y)  

Su2 = vfrac2*rho2*u2*diff(u2,x) + vfrac2*rho2*v2*diff(u2,y) - diff(vfrac2*tau_xx2, x) - diff(vfrac2*tau_xy2, y) - vfrac2*g_x*rho2 + vfrac2*diff(p,x)  
Sv2 = vfrac2*rho2*u2*diff(v2,x) + vfrac2*rho2*v2*diff(v2,y) - diff(vfrac2*tau_yy2, y) - diff(vfrac2*tau_yx2, x) - vfrac2*g_y*rho2 + vfrac2*diff(p,y) 

Srho1 = diff(vfrac1*u1*rho1,x) + diff(vfrac1*v1*rho1,y) + rho1*diff(u2*vfrac2, x) + rho1*diff(v2*vfrac2, y)

k = _sage_const_0p1 
C_v = _sage_const_0p4 
Sie1 = vfrac1*rho1*u1*diff(ie1, x) + vfrac1*rho1*v1*diff(ie1, y) + vfrac1*p*diff(u1, x) + vfrac1*p*diff(v1, y)
Sie2 = vfrac2*rho2*u2*diff(ie2, x) + vfrac2*rho2*v2*diff(ie2, y)

print 'from math import sin, cos, tanh, pi'
print ''
print 'def u1(X):'
print '    return', str(u1).replace('e^', 'exp').replace('^', '**').replace('000000000000', '').replace('x', 'X[0]').replace('y', 'X[1]')
print ''
print 'def v1(X):'
print '    return', str(v1).replace('e^', 'exp').replace('^', '**').replace('000000000000', '').replace('x', 'X[0]').replace('y', 'X[1]')
print ''  
print 'def p(X):'
print '    return', str(p).replace('e^', 'exp').replace('^', '**').replace('000000000000', '').replace('x', 'X[0]').replace('y', 'X[1]')
print ''  
print 'def rho1(X):'
print '    return', str(rho1).replace('e^', 'exp').replace('^', '**').replace('000000000000', '').replace('x', 'X[0]').replace('y', 'X[1]')
print ''  
print 'def ie1(X):'
print '    return', str(ie1).replace('e^', 'exp').replace('^', '**').replace('000000000000', '').replace('x', 'X[0]').replace('y', 'X[1]')
print ''  
print 'def vfrac1(X):'
print '    return', str(vfrac1).replace('e^', 'exp').replace('^', '**').replace('000000000000', '').replace('x', 'X[0]').replace('y', 'X[1]')
print ''  
print 'def forcing_u1(X):'
print '    return', str(Su1).replace('e^', 'exp').replace('^', '**').replace('000000000000', '').replace('x', 'X[0]').replace('y', 'X[1]')
print ''
print 'def forcing_v1(X):'
print '    return', str(Sv1).replace('e^', 'exp').replace('^', '**').replace('000000000000', '').replace('x', 'X[0]').replace('y', 'X[1]')
print ''
print 'def forcing_rho1(X):'
print '    return', str(Srho1).replace('e^', 'exp').replace('^', '**').replace('000000000000', '').replace('x', 'X[0]').replace('y', 'X[1]')
print ''
print 'def forcing_ie1(X):'
print '    return', str(Sie1).replace('e^', 'exp').replace('^', '**').replace('000000000000', '').replace('x', 'X[0]').replace('y', 'X[1]')
print ''
print 'def velocity1(X):'
print '   return [u1(X), v1(X)]'
print ''
print 'def forcing_velocity1(X):'
print '   return [forcing_u1(X), forcing_v1(X)]'
print ''
print 'def u2(X):'
print '    return', str(u2).replace('e^', 'exp').replace('^', '**').replace('000000000000', '').replace('x', 'X[0]').replace('y', 'X[1]')
print ''
print 'def v2(X):'
print '    return', str(v2).replace('e^', 'exp').replace('^', '**').replace('000000000000', '').replace('x', 'X[0]').replace('y', 'X[1]')
print ''  
print 'def rho2(X):'
print '    return', str(rho2).replace('e^', 'exp').replace('^', '**').replace('000000000000', '').replace('x', 'X[0]').replace('y', 'X[1]')
print ''  
print 'def ie2(X):'
print '    return', str(ie2).replace('e^', 'exp').replace('^', '**').replace('000000000000', '').replace('x', 'X[0]').replace('y', 'X[1]')
print ''  
print 'def vfrac2(X):'
print '    return', str(vfrac2).replace('e^', 'exp').replace('^', '**').replace('000000000000', '').replace('x', 'X[0]').replace('y', 'X[1]')
print ''  
print 'def forcing_u2(X):'
print '    return', str(Su2).replace('e^', 'exp').replace('^', '**').replace('000000000000', '').replace('x', 'X[0]').replace('y', 'X[1]')
print ''
print 'def forcing_v2(X):'
print '    return', str(Sv2).replace('e^', 'exp').replace('^', '**').replace('000000000000', '').replace('x', 'X[0]').replace('y', 'X[1]')
print ''
print 'def forcing_ie2(X):'
print '    return', str(Sie2).replace('e^', 'exp').replace('^', '**').replace('000000000000', '').replace('x', 'X[0]').replace('y', 'X[1]')
print ''
print 'def velocity2(X):'
print '   return [u2(X), v2(X)]'
print ''
print 'def forcing_velocity2(X):'
print '   return [forcing_u2(X), forcing_v2(X)]'
print ''
