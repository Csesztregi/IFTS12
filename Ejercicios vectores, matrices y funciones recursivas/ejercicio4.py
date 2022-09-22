#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      Fillory
#
# Created:     21/09/2022
# Copyright:   (c) Fillory 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

    v = [32, 74, 92, 25, 81]
    n3=0
    for i in v:
        n3+=1

    def vector (n1):
        n1-=1
        if n1>=0:
            print (v[n1])
            vector(n1)



    print (vector(n3))
if __name__ == '__main__':
    main()
