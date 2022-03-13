import math
rotor = 5*4*3
starting = 26**3
plugborad = math.factorial(26)/(math.factorial(10) * (math.factorial(6) * 2**10))
estimated_number = rotor*starting*plugborad
print(estimated_number)