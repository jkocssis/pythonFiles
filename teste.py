import sys
print (sys.version)
import statistics
print('NormalDist' in dir(statistics))

sat = statistics.NormalDist(167.44, 12.7)
a = sat.cdf(190.5) - sat.cdf(165.1)
print(round(a*800,1))
fraction = 1-sat.cdf(182.88)
print(round(fraction*800,1))
print(fraction)

