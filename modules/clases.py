#*************
# Sena, Mosquera CBA
# Brayan Esteban Penagos Gutierrez
# Version 1.0
# 02/05/2024
# Ficha: 2877795
# Funcionalidad: Clases Aprendiz e Instructor

#*************

#Importamos las librerias que necesitemos y vallamos a usar
from colorama import Fore, Style
import os
from datetime import datetime
from dateutil.relativedelta import *
from random import randint

#Funcion para digitar solo numeros
def solo_numeros(prompt):
    while True:
        entrada=input(prompt)
        if entrada.isdigit():
            return entrada
        else:
            print ("Solo se pueden digitar numeros")
            


#Funcion para digitar 6 numeros como minimo y 10 como maximo
def solo_numeros_seis(prompt):
    while True:
        entrada = input(prompt)
        if entrada.isdigit() and 6 <= len(entrada) <= 10:
            return entrada
        else:
            print("La entrada debe contener solo numeros y un minimo entre 6 y 10 caracteres.")


#Funcion para digitar 7 numeros exactamente
def solo_numeros_siete(prompt):
    while True:
        entrada = input(prompt)
        if entrada.isdigit() and len(entrada) == 7:
            return entrada
        else:
            print("La entrada debe ser solo numeros y debe contener exactamente 7 caracteres")



#Funcion para digitar solo letras           
def solo_letras(prompt):
    while True:
        entrada=input(prompt)
        #Reemplaza los espacios para que los cuente como digitos validos
        if  entrada.replace(" ","").isalpha():
            return entrada
        else:
            #Si no digita letras
            print ("Solo se pueden digitar letras")


#Creamos la primera clase llamada Persona
class Persona():
    def __init__(self, documento=0, nombre_completo=' ', informacion= ' '):
        self.__documento = documento
        self.__nombre_completo = nombre_completo
        self.__informacion = informacion


    #Definimos el metodo get para mostar el nombre completo
    def get_nombre_completo(self):
        return self.__nombre_completo
    
    #Definimos el metodo set para guardar el nombre completo
    def set_nombre_completo(self, nombre_completo):
        self.__nombre_completo = nombre_completo
    
    #Definimos el metodo get para mostar el documento
    def get_documento(self):
        return self.__documento
    
    #Definimos el metodo set para guardar el documento
    def set_documento(self, documento):
        self.__documento = documento
    
    #Definimos el metodo set para guardar la informacion
    def set_informacion(self, informacion):
        self.__informacion = informacion
    

    #Definimos el metodo get para mostar la informacion
    def get_informacion(self):
        return self.__informacion


#Creamos la clase Aprendiz que hereda de la clase Persona
class Aprendiz(Persona):
    def __init__(self,  programa=' ', ficha=0, matriculado=' ', documento=0, nombre_completo=' '):
        super().__init__(documento, nombre_completo)
        self.__programa = programa
        self.__matriculado = matriculado
        self.__ficha = ficha


    #Definimos el metodo get para mostar el programa
    def get_programa(self):
        return self.__programa


    #Definimos el metodo set para guardar el programa
    def set_programa(self, programa):
        self.__programa = programa


    #Definimos el metodo set para guardar la ficha
    def set_ficha(self, ficha):
        self.__ficha = ficha
    

    #Definimos el metodo get para mostar la ficha
    def get_ficha(self):
        return self.__ficha


    #Definimos el metodo get para mostar el estado de matricula
    def get_matriculado(self):
        return self.__matriculado


    #Definimos el metodo set para guardar el estado de matricula
    def set_matriculado(self, matriculado):
        self.__matriculado = matriculado
    
        
    #Creamos una funcion para que el estado de la matricula sea random
    def matricula(self):
        os.system('cls')
        matricula = ['Inscripcion', 'Prueba 1', 'Prueba 2', 'Induccion', 'Formacion']
        alerta = randint(0, len(matricula) - 1)
        print('\n''El estado de la matricula del aprendiz es: {0}'.format(matricula[alerta]))


#Creamos la clase EtapaLectiva que hereda de Aprendiz
class EtapaLectiva(Aprendiz):
    def __init__(self, trimestre = 0 , fecha_inicio=' ',fecha_terminacion=0,documento= 0,   programa=0, estado=' ', ficha = 0, nombre_completo = ' '):
        super().__init__( programa, ficha, documento, nombre_completo)
        self.__fecha_inicio = fecha_inicio
        self.__fecha_terminacion = fecha_terminacion
        self.__trimestre = trimestre
        self.__programa = programa
        self.__estado = estado


    #Definimos el metodo get para mostar la fecha de inicio
    def get_fecha_inicio(self):
        return self.__fecha_inicio


    #Definimos el metodo set para guardar la fecha de inicio
    def set_fecha_inicio(self, fecha_inicio):
        self.__fecha_inicio = fecha_inicio
    

    #Definimos el metodo get para mostar el numero de trimestre
    def get_trimestre(self):
        return self.__trimestre


    #Definimos el metodo set para guardar el numero de trimestre
    def set_trimestre(self, trimestre):
        self.__trimestre = trimestre
        

    #Definimos el metodo get para mostar la fecha de terminacion
    def get_fecha_terminacion(self):
        return self.__fecha_terminacion


    #Definimos el metodo set para guardar la decha de terminacion
    def set_fecha_terminacion(self, fecha_terminacion):
        self.__fecha_terminacion = fecha_terminacion


    #Definimos el metodo get para mostar la informacion
    def set_informacion(self, informacion):
        self.__informacion = informacion
        

    #Definimos el metodo get para mostar la informacion 
    def get_informacion(self):
        return self.__informacion
    

    #Definimos el metodo set para guardar el programa
    def set_programa(self, programa):
        self.__programa = programa
        

    #Definimos el metodo get para mostar el programa
    def get_programa(self):
        return self.__programa
    

    #Definimos el metodo set para guardar el estado del aprendiz
    def set_estado(self, estado):
        self.__estado = estado

    #Definimos el metodo get para mostrar el estado
    def get_estado(self):
        return self.__estado
    

    #Definimos el metodo get para mostar el nombre completo
    def get_nombre_completo(self):
        return self.__nombre_completo


    #Definimos el metodo set para guardar el nombre completo
    def set_nombre_completo(self, nombre_completo):
        self.__nombre_completo = nombre_completo
    
    
    ##Definimos el metodo get para guardar la matricula
    def get_matriculado(self):
        return self.__matriculado


    #Definimos el metodo set para guardar el estado de matricula
    def set_matriculado(self, matriculado):
        self.__matriculado = matriculado
    
        
    #Creamos una funcion para que el estado de la matricula sea random
    def matricula(self):
        matricula = ['Inscripcion', 'Prueba 1', 'Prueba 2', 'Induccion', 'Formacion']
        alerta = randint(0, len(matricula) - 1)
        print('\n''El estado de la matricula del aprendiz es: {0}'.format(matricula[alerta]))
        
    #Creamos una funcion para que ingrese todos los datos del aprendiz
    def ingrese_datos(self):
        
        #Le decimos al usuario que va a empezar con la Etapa Lectiva
        nombre = solo_letras('\n''Ingrese su nombre: ')
        self.set_nombre_completo(nombre)
        
        documento = solo_numeros_seis('\n''Ingrese su documento: ')
        self.set_documento(documento)
        
        ficha = solo_numeros_siete('\n''Ingrese el numero de su ficha: ') 
        self.set_ficha(ficha)   
        
        programa = solo_letras('\n''Ingrese el programa que esta haciendo: ')
        self.set_programa(programa)
        
        trimestre = input ('\n''Ingrese el trimestre que va: ')
        self.set_trimestre(trimestre)

        #Creamos un while para que el usuario hasta que no digite el formato que es no seguira el programa
        while True:
            try:
                fecha = input ('\n''Ingrese la fecha en la que inicio de su programa(AÑO/MES/DIA): ')
                datetime.strptime(fecha, "%Y-%m-%d")
                self.set_fecha_inicio(fecha)
                break
            except ValueError:
                print('La fecha solo puede estar en formato: AÑO/MES/DIA')

        #Creamos otro while para que el usuario hasta que no digite el formato de fecha que es no seguira el programa
        while True:
            try:
                fecha_terminacion = input ('\n''Ingrese la fecha en la que finaliza su programa(AÑO/MES/DIA): ')
                datetime.strptime(fecha, "%Y-%m-%d")
                self.set_fecha_terminacion(fecha_terminacion)
                break
            except ValueError:
                print('La fecha solo puede estar en formato: AÑO/MES/DIA')
    
        #Para mostrar el estado del aprendiz random
        estado = ['Aplazado', 'En comision', 'Induccion', 'Formacion', 'Retirado']
        alerta = randint(0, len(estado) - 1)
        print('\n''El estado del aprendiz es: {0}'.format(estado[alerta]))


        
    #Creamos una funcion para mostar la informacion que digito anteriormente
    def informacion(self):
            print('\n''El nombre del aprendiz es {0}, su documento es: {1}, la ficha correspondiente es: {2} su trimestre es: {3}, la fecha de inicio del programa es: {4}, y la ficha de finalizacion es: {5}'.format(self.get_nombre_completo(),self.get_documento(), self.get_ficha(), self.get_trimestre(), self.get_fecha_inicio(), self.get_fecha_terminacion(), self.get_estado()))
    


#Creamos la clase llamada EtapaPractica que hereda de Aprendiz
class EtapaPractica(Aprendiz):
    def __init__(self, fecha_terminacion=' ', fecha_inicio=' ', modalidad = ' ', documento=0, nombre_completo=' ', programa=' ', ):
        super().__init__( programa, documento, nombre_completo,)
        self.__fecha_terminacion = fecha_terminacion
        self.__fecha_inicio = fecha_inicio
        self.__modalidad = modalidad
    

    #Definimos el metodo get para mostrar la modalidad
    def get_modalidad(self):
        return self.__modalidad
    

    #Creamos el metodo set para guardar la modalidad
    def set_modalidad(self, modalidad):
        self.__modalidad = modalidad
    

    #Definimos el metodo get para mostrar el estado de matricula
    def get_matricula(self):
        return self.__matricula


    #Creamos el metodo set para guardar el estado de la matricula
    def set_matricula(self, matricula):
        self.__matricula = matricula


    #Definimos el metodo get para mostrar la fecha de terminacion
    def get_fecha_terminacion(self):
        return self.__fecha_terminacion


    #Creamos el metodo set para guardar la fecha de terminacion
    def set_fecha_terminacion(self, fecha_terminacion):
        self.__fecha_terminacion = fecha_terminacion


    #Definimos el metodo get para mostrar la fecha de inicio 
    def get_fecha_inicio(self):
        return self.__fecha_inicio
    

    #Creamos el metodo set para guardar la fecha de inicio
    def set_fecha_inicio(self, fecha_inicio):
        self.__fecha_inicio = fecha_inicio
    

    #Creamos el metodo set para guardar el estado del aprendiz
    def set_estado(self, estado):
        self.__estado = estado


    #Definimos el metodo get para mostrar el estado  del aprendiz
    def get_estado(self):
        return self.__estado
        
    
    def get_matriculado(self):
        return self.__matriculado


    #Definimos el metodo set para guardar el estado de matricula
    def set_matriculado(self, matriculado):
        self.__matriculado = matriculado
    
        
    #Creamos una funcion para que el estado de la matricula sea random
    def matricula(self):
        matricula = ['Inscripcion', 'Prueba 1', 'Prueba 2', 'Induccion', 'Formacion']
        alerta = randint(0, len(matricula) - 1)
        print('\n''El estado de la matricula del aprendiz es: {0}'.format(matricula[alerta]))


    def leer_datos(self):
        
        nombre = solo_letras('\n''Ingrese su nombre: ')
        self.set_nombre_completo(nombre)
        
        documento = solo_numeros_seis('\n''Ingrese su documento: ')
        self.set_documento(documento)
        
        ficha = solo_numeros_siete('\n''Ingrese el numero de su ficha: ') 
        self.set_ficha(ficha)   
        
        programa = solo_letras('\n''Ingrese el programa que esta haciendo: ')
        self.set_programa(programa)
        

        modalidad = solo_letras('\n''Ingrese su modalidad: ')
        self.set_modalidad(modalidad)

        #Creamos un while para que el usuario hasta que no digite el formato que es no seguira el programa
        while True:
            try:
                fecha = input ('\n''Ingrese la fecha en la que inicio de su programa(AÑO/MES/DIA): ')
                datetime.strptime(fecha, "%Y-%m-%d")
                self.set_fecha_inicio(fecha)
                break
            except ValueError:
                print('La fecha solo puede estar en formato: AÑO/MES/DIA')

        #Creamos otro while para que el usuario hasta que no digite el formato de fecha que es no seguira el programa
        while True:
            try:
                fecha_terminacion = input ('\n''Ingrese la fecha en la que finaliza su programa(AÑO/MES/DIA): ')
                datetime.strptime(fecha, "%Y-%m-%d")
                self.set_fecha_terminacion(fecha_terminacion)
                break
            except ValueError:
                print('La fecha solo puede estar en formato: AÑO/MES/DIA')
    
        #Para que el estado del aprendiz sea aleatorio
        estado = ['Aplazado', 'En comision', 'Induccion', 'Formacion', 'Retirado']
        alerta = randint(0, len(estado) - 1)
        print('\n''El estado del aprendiz es: {0}'.format(estado[alerta]))


        
    #Creamos una funcion para mostrar la informacion antes dada
    def informacion_ep(self):
            print('\n''El nombre del aprendiz es {0}, su documento es: {1}, la ficha correspondiente es: {2} su modalidad es: {3}, la fecha de inicio del programa es: {4}, y la ficha de finalizacion es: {5}'.format(self.get_nombre_completo(),self.get_documento(), self.get_ficha(), self.get_modalidad(), self.get_fecha_inicio(), self.get_fecha_terminacion()))

        
#Creamos una clase llamada Instructor que hereda de Persona
class Instructor(Persona):
    def __init__(self, documento=0, nombre_completo=' ', profesion=' ', salario_basico=0 ):
        super().__init__(nombre_completo, documento)
        self.__profesion = profesion
        self.__salario_basico = salario_basico
    

    #Creamos un get para mostrar la profesion del Instructor
    def get_profesion(self):
        return self.__profesion


    #Creamos un set para guardar la profesion 
    def set_profesion(self, profesion):
        self.__profesion = profesion
    

    #Creamos un get para mostrar el salario basico
    def get_salario_basico(self):
        return self.__salario_basico
    

    #Creamos un set para guardr el salario basico
    def set_salario_basico(self, salario_basico):
        self.__salario_basico = salario_basico
        

    #Creamos una funcion para que el contrato sea aleatoria
    def contrato(self):

        contrato = ['\n''Prestacion de servicios', 'Provisional', 'Relacion Legal']
        long = randint(0, len(contrato) - 1)
        print('\n''El contrato del instructor es: {0}'.format(contrato[long]))
        

#Creamos una clase llamada Instructor_Planta que hereda de la clase Instructor
class Instructor_Planta(Instructor):
    def __init__(self, documento=0, nombre_completo=' ', profesion=' ', salario_basico=0, grado=0,fecha_vinculacion=0):
        super().__init__(nombre_completo, documento, profesion, salario_basico)
        self.__grado = grado
        self.__fecha_vinculacion = fecha_vinculacion
        
    

    #Creamos un get para mostrar el grado
    def get_grado(self):
        return self.__grado
    

    #Creamos un set para guardar el grado
    def set_grado(self, grado):
        self.__grado = grado
        
    
    #Creamos un get para mostrar la fecha de vinculacion
    def get_fecha_vinculacion(self):
        return self.__fecha_vinculacion
    

    #Creamos un set para guardar la fecha de vinculacion
    def set_fecha_vinculacion(self, fecha_vinculacion):
        self.__fecha_vinculacion = fecha_vinculacion
        

    #Creamos una funcion para que el usuario ingrese los datos
    def ingrese_datos(self):
        while True:
            #Le pedimos al usuario su nombre
            nombre = input('\n''Ingrese su nombre: ')
            #Si no son letras le saldra este mensaje
            if not nombre.replace(" ", "").isalpha():
                print('\n'"Solo puede digitar letras.")
                continue
            #Que lo guarde en el set
            self.set_nombre_completo(nombre)
            break
        #Le pedimos al usuario que digite su documento con la funcion de solo_numeros_seis
        documento = solo_numeros_seis('\n''Ingrese su documento: ')
        #Que lo guarde en el set
        self.set_documento(documento)
            
        #Le pedimos al usuario que digite su profesion con la funcion solo_letras
        profesion = solo_letras('\n''Ingrese su profesion: ')
        #Que lo guarde en el set
        self.set_profesion(profesion)
        #Creamos este while para que digite el salario basico que tenga entre 6 y 8 digitos
        while True:
            #Le pedimos al usuario que digite su salario basico
            salario_basico = input('\nIngrese su salario basico: ').strip()
            #Si lo que digito no son numeros le saldra el siguiente mensaje
            if not salario_basico.isdigit():
                print('\nDigite solo numeros por favor')
                continue
            #Si son numeros pero es menor a 6 o mayor a 8 que vuelva a digitar el salario
            elif not (6 <= len(salario_basico) <= 8):
                print('\nEl salario debe contener entre 6 y 8 digitos.')
                continue
            #Que lo guarde en el set
            self.set_salario_basico(int(salario_basico))
            break
        
        #Creamos este otro while para que escriba la fecha en el formato que dice en el programa
        while True:
            #Este try es para capturar el error y que no se salga del programa
            try:
                fecha_vinculacion = input('\n'"Ingrese la fecha de vinculacion (AÑO/MES/DIA): ").strip()
                #Formato en el que el usuario debe digitar la fecha
                datetime.strptime(fecha_vinculacion, "%Y-%m-%d")
                #Que lo guarde en el set
                self.set_fecha_vinculacion(fecha_vinculacion)
                break
            #El error que le va a mostrar si no escribe la fecha correctamente
            except ValueError:
                print("La fecha debe ser (AÑO/MES/DIA). ")
    
    
    #Funcion para generar numeros aleatorios
    def generar_grado(self):
        self.set_grado(randint(1,20))


    #Esta funcion es para el estado del instructor en modo random
    def estado(self):
        estado =['Vacaciones', 'Pensionado', 'Pre pensionado', 'En licencia', 'En formacion']
        stade = randint(0, len(estado) - 1)
        print('\n''El contrato del instructor es: {0}'.format(estado[stade]))
    
    #Funcion para mostrar la informacion antes dada
    def informacion(self):
        print('\n'"El nombre del instructor es {0}, su cedula es {1}, la profesion de el es {2}, su salario es de {3} y su fecha de vinculacion es de {4}".format(self.get_nombre_completo(), self.get_documento(),self.get_profesion(), self.get_salario_basico(),self.get_fecha_vinculacion()))
            #Funcion para calcular el sueldo del instructor
    def sueldo(self):
        #El sueldo que va a ingresar el usuario empezara en 0
        if self.get_grado() == 0:
            #Lo guardara en la funcion generar_grado
            self.generar_grado()
        #Hcaemos la operacion de el salario basico, el grado * 100000
        sueldo_final = self.get_salario_basico() + self.get_grado() * 100000
        sueldo = "{:,}".format(sueldo_final)
        #Le decimos al usuario el salario final que ganara el instructor
        print(f"\nEl grado del Instructor de planta es de: {self.get_grado()}, y el salario es de {sueldo}")
#Creamos la clase de Instructor_Contrato que hereda de Instructor
class Instructor_Contrato(Instructor):
    #Atributos que va a tener la clase Instructor_Contrato
    def __init__(self, documento=0, nombre_completo=' ', profesion=' ', salario_basico=0,fecha_vinculacion=0, duracion_contrato=0):
        #Atributos que va a heredar de la Superclase Instructor
        super().__init__(nombre_completo, documento, profesion, salario_basico)
        self.__duracion_contrato = duracion_contrato
        self.__fecha_vinculacion = fecha_vinculacion
        
    
    #Creamos un get para mostrar la duracion del contrato
    def get_duracion_contrato(self):
        return self.__duracion_contrato


    #Creamos una set para guardar la duracion del contrato
    def set_duracion_contrato(self, duracion_contrato):
        self.__duracion_contrato = duracion_contrato


    #Creamos un get para mostrar la fecha de vinculacion
    def get_fecha_vinculacion(self):
        return self.__fecha_vinculacion
    

    #Creamos un set para guardar la fecha de vinculacion
    def set_fecha_vinculacion(self, fecha_vinculacion):
        self.__fecha_vinculacion = fecha_vinculacion
        

    #Creamos una funcion que va a preguntar los datos del usuario
    def ingrese_datos(self):
        #Le decimos al usuario que va a empezar con el Instructor Por Contrato
        while True:
            #Le pedimos que ingrese el nombre
            nombre = input('\n''Ingrese su nombre: ')
            #Para que los espacios cuenten como caracter
            if not nombre.replace(" ", "").isalpha():
                #Si el nombre no son letras le mostrara el siguiente mensaje
                print('\n'"Solo puede digitar letras.")
                continue
            #Lo guarde en el set
            self.set_nombre_completo(nombre)
            break
        #Le preguntamos al usuario el documento
        documento = solo_numeros_seis('\n''Ingrese su documento: ')
        #Lo guardamos en el set
        self.set_documento(documento)
        
        #Le preguntamos al usuario la profesion
        profesion = solo_letras('\n''Ingrese su profesion: ')
        #Lo guardamos en el set
        self.set_profesion(profesion)
        
        while True:
            #Le preguntamos al usuario que ingrese el salario que gana
            salario_basico = input('\nIngrese su salario basico: ').strip()
            if not salario_basico.isdigit():
                #Por si no digita numeros
                print('\nDigite solo numeros por favor')
                continue
            #Debe contener entre 6 y 8 digitos
            elif not (6 <= len(salario_basico) <= 8):
                #Si se pasa o no lo escribe completo le aparecera el siguiente mensaje
                print('\nEl salario debe contener entre 6 y 8 digitos.')
                continue
            #Lo guardara en el set
            self.set_salario_basico(int(salario_basico))
            break
            
        while True:
            try:
                #Le pedimos al usuario que ingrese la fecha de vinculacion en ese formato(AA/MM/DD)
                fecha_vinculacion = input('\n'"Ingrese la fecha de vinculacion (AÑO/MES/DIA): ").strip()
                #El formato debe ser como se muestra aca
                datetime.strptime(fecha_vinculacion, "%Y-%m-%d")
                #Lo guardara en el set
                self.set_fecha_vinculacion(fecha_vinculacion)
                break
            #Captura el error
            except ValueError:
                #Le muestra el siguiente mensaje si no escribie la fecha correctamente
                print('\n'"La fecha debe ser (AÑO/MES/DIA). ")
                


    #Creamos la funcion para preguntar el contrato
    def duracion_contrato(self):
        while True:
            #Le preguntamos el usuario la cantidad de meses que tiene el contrato
            mes = input('\n'"Ingrese la cantidad de meses que tiene su contrato: ").strip()
            if not mes.isdigit():
                #Si lo que escribio no son numeros, le aparece el suguiente mensaje
                print('\n'"La cantidad de meses debe ser numerico.")
                continue
            elif int(mes)< 1 or int(mes) > 99:
                #Si la cantidad es menor a 1 o mayor a 99, le aparece el siguiente mensaje 
                print('\n'"La cantidad de meses debe ser de dos digitos")
                continue
            #Lo guardara en el set
            self.set_duracion_contrato(int(mes))
            break
        

    #Creamos la funcion que mostrara la informacion anteriormente digitada
    def informacion(self):
        #Muestra toda la informacion
        print('\n'"El nombre es: {0}, la cedula es {1}, su profesion es {2}, su salario es de {3}, la fecha de vinculacion es {4}, la duracion de su contrato es de {5}".format(self.get_nombre_completo(), self.get_documento(),self.get_profesion(), self.get_salario_basico(),self.get_fecha_vinculacion(), self.get_duracion_contrato()))


    #Creamos la funcion que determinara el estado del contrato
    def estado(self):
        if self.__duracion_contrato==  0:
            #Si lo que digito anteriromente es 0, le mostrara el siguiente mensaje
            print('\n'"Aun no se ha establecido una duracion a su contrato. ")
        else:
            fecha_inicio = datetime.strptime(self.get_fecha_vinculacion(), "%Y-%m-%d")
            fecha_fin = fecha_inicio + relativedelta(months=self.__duracion_contrato)
            print(f"\nLa fecha de la finalizacion de su contrato sera: {fecha_fin.strftime("%Y-%m-%d")}")