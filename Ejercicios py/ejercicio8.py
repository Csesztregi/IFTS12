#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Fillory
#
# Created:     04/09/2022
# Copyright:   (c) Fillory 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

lista=[23,44,55,22]
minimo = 10000000000000000000000000000000000000000000000

for i in lista:
    if i < minimo:
            minimo = i
print(f"el minimo es: {minimo}")

if __name__ == '__main__':
    main()
