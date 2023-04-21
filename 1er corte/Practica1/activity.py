'''
    data type: list practice
    date: 25/01/23
'''
#1 declarar la clase
class ListPractice:
    #2 crear funcion
    def __init__(self):
        #Definir las variables globales de la clase 
        self.student_name = ""
        self.courses_list = ["POO",'TAD']
    #3 Funcion customizada 
    def show_info_list(self):
        #imprimir contenido de la lista  courses_list 
        print(self.courses_list)
        #Cantidad de elementos que tiene la lista
        print(len(self.courses_list))
    #4 Funcion que solicita al usuario ingresar informacion
    def input_data_courses(self):
        #1 declaramos una variable a nivel de metodo
        print("ingrese la sgte informacion:")
        self.student_name = input("nombre: ")
        #solicitamos un numero entero
        courses_number = int(input("Cantidad de materias: "))
        #validamos si el courses_number es menor que el tamaño actual 
        if courses_number <= len(self.courses_list):
            print(">> Error: Cursos a inscribir < 2 <<")
        else:
        #solicitar nombre de las asignaturas
            for i in range(len(self.courses_list),courses_number):
                #variable que almaena el nombre de la asignatura
                course_name=input("Nombre Asignatura: ")
                # Añadimos nuevo  elemnto al final de la lista append()
                if course_name == self.courses_list[0] or course_name == self.courses_list[1]:
                    print("las clases son iguales")
                else:
                    self.courses_list.append(course_name)
            #imprimir contenido de la lista
            print(self.courses_list)
