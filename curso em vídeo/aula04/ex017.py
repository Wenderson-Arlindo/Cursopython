import math 
cpo = float(input('Digite a medida do cateto oposto: ')) 
cad = float(input('digite a medida do cateto adjacente: ')) 
p1 = cpo*cpo 
p2 = cad*cad 
pp = p1 + p2 
print('O valor da hipotenusa e {:.2f}'.format(math.sqrt(pp)))