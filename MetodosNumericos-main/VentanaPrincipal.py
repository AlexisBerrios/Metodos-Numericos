import sys #proveer variables y funcionalidades
#para leer interpretar las funciones matematicas
import math
import cmath
import os
#PyQt5 libreria para desarrollar interfaz grafica
from PyQt5 import uic, QtWidgets 
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PyQt5.uic import loadUi



class VentanaPrincipal(QMainWindow):#modificar si es un dialogo

    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi('mainMetodos.ui', self)#carga la ventana conversor
        self.temasBtn.clicked.connect(self.abrirVentana)
        self.setStyleSheet("background-color: silver;")
        
    def abrirVentana(self):
        self.close()
        otraVentana = VentanaTemas(self)
        otraVentana.show()
    #si se tuvieran mas botones se abriria toda  aqui

                
class VentanaTemas(QDialog):
    
    def __init__(self, parent=None):
        super(VentanaTemas, self).__init__(parent)
        loadUi('ventanaTemas.ui', self)
        self.simpsonBtn.clicked.connect(self.abrirVentanaSimpsonFun)
        self.simpsonTabBtn.clicked.connect(self.abrirSimpson)
        self.trapecioBtn.clicked.connect(self.abrirTrapecio)
        self.inicioBtn.clicked.connect(self.abrirVentanaPrincipal)
        self.puntoBtn.clicked.connect(self.abrirPuntoFijo)
        
    def abrirPuntoFijo(self):
        self.close()
        otraVentana = PuntoFijo(self)
        otraVentana.show()
    
    def abrirVentanaSimpsonFun(self):
        self.close()
        otraVentana = SimpsonFun(self)
        otraVentana.show()
    def abrirSimpson(self):
        self.close()
        otraVentana = SimpsonFun38(self)
        otraVentana.show()
    
    def abrirTrapecio(self):
        self.close()
        otraVentana = Trapecio(self)
        otraVentana.show()
    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()
        

class SimpsonFun38(QDialog):
    
    def __init__(self, parent=None):
        super(SimpsonFun38, self).__init__(parent)
        loadUi('simpsonFun38.ui', self)
        
        self.calcBtn.clicked.connect(self.calculos)
        self.inicioBtn.clicked.connect(self.abrirVentanaPrincipal)
        
    #aqui van las funciones
    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()
    def calculos(self):
        def function(x):
        #el valor de x es con el    que se evaluara
            return (eval(fun))#en esta funcion
        #funcion dada por el usuario
        fun = (self.funcionTxt.toPlainText())
        interv = (self.nBox.value())
        limInf = float((self.limInfEdit.text()))
        limSup = float((self.limSupEdit.text()))
        
        #LOGICA SIMPSON 3/8

        #obtener h = b (limSup) - a (limInf) / n (interv)
        h = (limSup-limInf)/interv 
        
        #le damos los limites de la función a la variable integral
        integral = function(limInf)+function(limSup)
        #print("aaaaa",integral)
        #Bucle for para encontrar Xi (k) y 
        for i in range(1,interv):   
            #en cada paso por el bucle iremos encontrando Xi correspondiente al intervalo
            # Xi (k) = a (limInf) + i (interv) * h (h)        
            k = limInf + i*h
            #evaluar la funcion sustituyendo x (k)
            ##integral = integral para ir sumando los valores y multipl
            if i == 0:    #sumar los valores que no son multiplicados
                integral = integral + function(k)
                #print("UNO ",integral)
            elif i== 1:
                integral = integral + (3 * function(k))
                #print("dos ",integral)
            elif i== 2:
                integral = integral + (3 * function(k))
                #print("tres",integral)
            elif i== 3:   #sumar los valores que no son multiplicados
                integral = integral + function(k)
                #print("cuatro",integral)
        #al final, despues de sumar los resultados de la integral evaluada en x (k)
        #dividimos h entre 8, multiplicamos por 3 y el resultado por nuestro valor total de la integral
        integral = integral * 3 * h / 8
            
        integral_st = str(integral)
        self.resultadoTxt.setText(integral_st)
#class SimpsonFun38(QDialog):

#aqui empieza simpson 1/3
class SimpsonFun(QDialog):
    
    def __init__(self, parent=None):
        super(SimpsonFun, self).__init__(parent)
        loadUi('simpsonFun.ui', self)
        
        self.calcBtn.clicked.connect(self.calculos)
        self.inicioBtn.clicked.connect(self.abrirVentanaPrincipal)
        
    #Funciones
    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()
    def calculos(self):
        def function(x):
        #el valor de x es con el    que se evaluara
            return (eval(fun))#en esta funcion
        #funcion dada por el usuario
        fun = (self.funcionTxt.toPlainText())
        interv = (self.nBox.value())
        limInf = float((self.limInfEdit.text()))
        limSup = float((self.limSupEdit.text()))
        
        #LOGICA SIMPSON 1/3
        #obtener h = b (limSup) - a (limInf) / n (interv)
        h = (limSup-limInf)/interv          
        #dividir h por 3 (h/3)
        k = h/3
        #le damos los limites de la función a la variable integral
        integral = function(limInf)+function(limSup)
        #print(integral)
        #sumamos a esto los valores multiplicados por 2 y 4
        if interv ==2:
            integral *=k
            integral_st = str(integral)
            self.resultadoTxt.setText(integral_st)
        else:
            for i in range (1,interv):#multiplicar por los 3 valores impares
                if (i%2==0):
                    integral += 2*(function(limInf + h*i))
                    #print("multiplicado por 2",function(limInf + h*i))
                else:
                    integral += 4*(function(limInf + h*i))
                    #print("multiplicado por 4",integral)
            integral *= k #aqui hice algo raro con el signo pero no me acuerdo por qué
            #print("La integral buscada es igual a: ", integral)## debe ir en a interfaz
            integral_st = str(integral)
            self.resultadoTxt.setText(integral_st)
        
class Trapecio(QDialog):
    
    def __init__(self, parent=None):
        super(Trapecio, self).__init__(parent)
        loadUi('trapecio.ui', self)
        
        self.calcBtn.clicked.connect(self.calculos)
        self.inicioBtn.clicked.connect(self.abrirVentanaPrincipal)
        
    #aqui van las funciones
    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()
    def calculos(self):
        
        
        def function(x):
        #el valor de x es con el que se evaluara la función
            return (eval(fun))#en esta funcion
        #funcion dada por el usuario
        fun = (self.funcionTxt.toPlainText())
        n = (self.nBox.value())
        limInf = float((self.limInfEdit.text()))
        limSup = float((self.limSupEdit.text()))


        #Logica de método del trapecio
        
        ##esta es la forma ampliada del la regla del trapecio
        if n !=0 :
            h = (limSup - limInf) / n #encontramos h (h=b-a/n)
            integral = (function(limInf) + function(limSup)) #agregamos limites a la función
            #evaluamos la integral de 1 a n
            for i in range(1,n):
                integral += 2*(function(limInf + h * i))
            integral *= h/2
        integral_st = str(integral) 
        
        self.resultadoTxt.setText(integral_st)

        

app = QApplication(sys.argv)
main = VentanaPrincipal()
main.show()
sys.exit(app.exec_())
