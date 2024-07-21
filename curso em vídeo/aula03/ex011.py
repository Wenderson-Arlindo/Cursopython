n1 = float(input('largura da parede: '))

print(' ')

n2 = float(input('altura da parede: '))

print(' ')

print('sua parede tem a dimensão de {:.1f} x {:.1f} e sua área é de {:.2f}m² \npara pintar a parede, você precisa de {:.2f}l de tinta!!!'.format(n1, n2, (n1*n2), (n1*n2/2)))