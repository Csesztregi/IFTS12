#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Daniela
#
# Created:     17/09/2022
# Copyright:   (c) Daniela 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def suma_de_todos(numero):

    if (numero == 0):
        return 0

    else:
        return numero + suma_de_todos(numero-1)


suma_de_todos(20)
