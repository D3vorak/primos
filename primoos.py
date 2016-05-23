# -*- coding: utf-8 -*-
while True:
    n = input(": ")
    if n < 3:
        print"Apenas numeros apartir de 3"
        r = (2^n+n^2)/3
    elif r % 3 == 0:
        print "%.2f é primo"%(n)
    else:
        print "%.2f nao é primo" %(n)