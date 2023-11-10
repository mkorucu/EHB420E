import cmath

def quadratic_equation_calculator(a, b, c):
	delta = (b**2 - 4*a*c)
	root1 = (-b + cmath.sqrt(delta)) / (2*a)
	root2 = (-b - cmath.sqrt(delta)) / (2*a)
	return root1, root2

print("calculating roots of (x^2) - 5.86x + 8.5408")
roots = quadratic_equation_calculator(1, 5.86, 8.5408)
print("root 1: " + str(roots[0]))
print("root 2: " + str(roots[1]))

