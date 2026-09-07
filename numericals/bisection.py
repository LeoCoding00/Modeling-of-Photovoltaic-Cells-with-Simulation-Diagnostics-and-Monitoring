from math import exp

def calc_root(I,Iph,I0,Rs,Rsh,Vt,n,V):
    return (Iph-I0(exp((V+I*Rs)/(n*Vt))-1)-((V+I*Rs)/(Rsh))-I)
