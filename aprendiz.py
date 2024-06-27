#*************
# Sena, Mosquera CBA
# Brayan Esteban Penagos Gutierrez
# Version 1.0
# 02/05/2024
# Ficha: 2877795
# Funcionalidad: Clases Aprendiz e Instructor

#*************

#Importamos de la carpeta modulos el archivo llamado clases
import modules.clases as clases
from colorama import Fore, Style, init
init(autoreset=True)

#Creamos una funcion principal para llamar todas las clases y funciones del archivo que importamos
def main():
#Llamamos la clase EtapaLectiva a una varable llamada "aprendiz"
    
    aprendiz = clases.EtapaLectiva()
    
    print(Fore.LIGHTGREEN_EX + '\n'"***************ETAPA LECTIVA*************** "+ Style.RESET_ALL)
    
    aprendiz.matricula()
    
    #De la clase EtapaLectiva llamamos la funcion ingrese_datos
    aprendiz.ingrese_datos()
    
    #De la clase EtapaLectiva llamamos la funcion informacion
    aprendiz.informacion()
    
    #Llamamos la clase EtapaPractica a una vairable llamada "aprendiz_ep"
    aprendiz_ep = clases.EtapaPractica()
    
    #Le decimos al usuario que va a empezar con la Etapa Practica
    print(Fore.LIGHTYELLOW_EX + '\n'"***************ETAPA PRACTICA***************"+ Style.RESET_ALL)
    
    aprendiz_ep.matricula()
    
    #De la clase EtapaPractica llamamos la funcion leer_datos
    aprendiz_ep.leer_datos()
    
    #De la clase EtapaPractica llamamos la funcion infromacion_ep
    aprendiz_ep.informacion_ep()
    
    
    #Llamamos la clase Intructor_Planta a una variable llamada "instructor_p"
    instructor_p = clases.Instructor_Planta()
    
    print(Fore.LIGHTWHITE_EX + '\n'"*****************INSTRUCTOR PLANTA*****************"+ Style.RESET_ALL)
    
    instructor_p.contrato()
    
    #De la clase Intructor_Planta llamamos la funcion ingrese_datos
    instructor_p.ingrese_datos()
    
    #De la clase Instructor_Planta llamamos la funcion generar_grado
    instructor_p.generar_grado()
    
    #De la clase Instructor_Planta llamamos la funcion estado
    instructor_p.estado()
    
    #De la clase Instructor_Planta llamamos la funcion informacion
    instructor_p.informacion()
    
    #De la clase Instructor_Planta llamamos la funcion sueldo
    instructor_p.sueldo()
    
    #Llamamos la clase Instructor_Contrato a una variable llamada "instructor_c"
    instructor_c = clases.Instructor_Contrato()
    
    #Le decimos al usuario que va a empezar con el Instructor Planta
    print(Fore.LIGHTCYAN_EX + '\n'"***************INSTRUCTOR CONTRATO***************"+ Style.RESET_ALL)
    
    #De la clase Instructor_Contrato llamamos la funcion contrato
    instructor_c.contrato()
    
    #De la clase Instructor_Contrato llamamos la funcion ingrese_datos
    instructor_c.ingrese_datos()
    
    instructor_c.duracion_contrato()
    
    #De la clase Instructor-Contrato llamamos la funcion informacion
    instructor_c.informacion()
    
    #De la clase Instructor_Contrato llamamos la funcion estado
    instructor_c.estado()


#Llamamos a la funcion principal para ejecutarla
if __name__ == '__main__':
    main()