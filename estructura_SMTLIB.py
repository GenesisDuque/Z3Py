#!/usr/bin/python3

import sys

# Cambio opciones para el compoortamiento del Solvers  
def setlogic(l):
    return "(set-logic "+ l +")"

# Declaracion de una varible sort para establecer un orden
def sortvar(b,n):
    return "(declare-sort "+ b + " " + n +")"

# Declaracion de una funcion con de un sort existente
def sortfun(b , c):
    return "(declare-fun "+ b +" ()"+ c + " )"

# Declaración una variable booleana
def boolvar(b):
    return "(declare-fun "+b+" () Bool)"

# Declaración varibale entera 
def intvar(v):
    return "(declare-fun "+v+" () Int)"

# Funcion p
def bool2int(b):
    return "(ite "+b+" 1 0 )"

# Funcion sobre la implicacion de a1 sobre a2 
def addimplies(a1,a2):
    return "(=> "+a1+" "+a2+" )"

# Funcion sobre la conjución de a1 y a2
def addand(a1,a2):
    return "(and "+a1+" "+a2+" )"

#Funcion sobre la disyuncion de a1 y a2
def addor(a1,a2):
    return "(or "+a1+" "+a2+" )"

#Funcion sobre la negación de a 
def addnot(a):
    return "(not "+a+" )"

#Funcion sobre la negación de a 
def addproposicional(a):
    return "(! "+a+" )"

def addexists(a):
    if len(a) == 0:
        return "false"
    elif len(a) == 1:
        return a[0]
    else :
        x = a.pop()
        return "(or " + x + " " + addexists(a) + " )" 

# Funcion de equidad sobre a1 y a2
def addeq(a1,a2):
    return "(= "+a1+" "+a2+" )" 

#Función de diferencia de elementos 
def distinc(a1,a2)
        return "( distinct "+a1+" "+a2+" )" 

# Funcion menor igual que a1 y a2
def addle(a1,a2):
    return "(<= "+a1+" "+a2+" )" 

# Funcion mayor igual que a1 y a2
def addge(a1,a2):
    return "(>= "+a1+" "+a2+" )" 

# Funcion 
def addlt(a1,a2):
    return "(< "+a1+" "+a2+" )"

#Funcion mayar a1 que a2
def addgt(a1,a2):
    return "(> "+a1+" "+a2+" )" 

# Funcion suma a1 y a2 
def addplus(a1,a2):
    return "(+ "+a1+" "+a2+" )"

# Funcion creación de restricciones 
def addassert(a):
    return "(assert "+a+" )"

# Funcion de creación de restricciones no-obligatorias
def addassertsoft(a,w):
    return "(assert-soft "+a+" :weight "+ w + " )"

# Funcion para sumar una lista 
def addsum(a):
    if len(a) == 0:
        return "0"
    elif len(a) == 1:
        return a[0]
    else :
        x = a.pop()
        return "(+ " + x + " " + addsum(a) + " )" 

# Ejecutor de solucion : sat- satisfación | unsat - insatisfacion del problema
def checksat():
    print("(check-sat)")

#
def getobjectives():
    print("(get-objectives)")
#
def getmodel():
    print("(get-model)")

# Salida de los valores del problema
def getvalue(l):
    print("(get-value " + l + " )")

def getassignment(l):
    print("(get-assignment " + l + " )")


################################
#> (assert (not (=> (or (! p :named P) (! q :named Q)) (! r :namedR))))
#success
#> (check-sat)
#sat
#> (get-assignment)
#((P true)(Q true)(R false))
################################
# generamos un fichero smtlib2
################################

print("(set-option :produce-models true)")
#print(setlogic("QF_?"))

#declaración de variables de la solución
