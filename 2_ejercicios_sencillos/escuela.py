class Escuela:

    def __init__(self, nombre, direccion, presupuesto, capacidad):
        self.nombre = nombre
        self.direccion = direccion
        self.capacidad = capacidad
        self.presupuesto = presupuesto
        self.alumnos = []
        self.clases = []
        self.salones = []
        self.profesores = []   

    def set_nombre(self, nombre):
        self.nombre = nombre  
        
    def get_nombre(self):
        return self.nombre
    
    def set_direccion(self, direccion):
        self.direccion = direccion

    def get_direccion(self):
        return self.direccion
    
    def set_capacidad(self, capacidad):
        self.capacidad = capacidad

    def aumentar_capacidad(self, aumento_capacidad):
        self.capacidad += aumento_capacidad

    def get_capacidad(self):
        return self.capacidad
    
    def set_presupuesto(self, presupuesto):
        self.presupuesto = presupuesto

    def aumentar_presupuesto(self, aumento_presupuesto):
        self.presupuesto += aumento_presupuesto

    def get_presupuesto(self):
        return self.presupuesto
    
    def inscribir_alumno(self, cedula, nombre, edad, anio_cursa):
        alumno = Alumno(cedula, nombre, edad, anio_cursa)
        self.alumnos.append(alumno)

    def dar_baja_alumno(self, cedula):
        no_encontrado = True
        for i in self.alumnos:
            if i.cedula == cedula:
                 self.alumnos.remove(i)
                 no_encontrado = False
                 break
        if no_encontrado:
             print("El alumno con la cedula "+str(cedula)+ " no se encuentra inscripto en la escuela" + self.nombre)

    def crear_salon(self, id, lugar, descripcion):
        salon = Salon(id, lugar, descripcion)
        self.salones.append(salon)
                 
    def contratar_profesor(self, cedula, nombre, materia_dicta, sueldo_anio):
        profesor = Profesor(cedula, nombre, materia_dicta, sueldo_anio)
        self.profesores.append(profesor)

    def dar_baja_profesor(self, cedula):
        no_encontrado = True
        for i in self.profesores:
            if i.cedula == cedula:
                 self.profesores.remove(i)
                 no_encontrado = False
                 break
        if no_encontrado:
             print("El profesor con la cedula "+str(cedula)+ " no se encuentra contratado en la escuela" + self.nombre)
    
    def generar_clase(self, nombre_materia, salon, profesor, horario):
        clase = Clase((nombre_materia, salon, profesor, horario))

    def imprimir_informacion(self):
        print("\n------------ "+ self.get_nombre() + " ------------\nDirección: " + self.get_direccion() + "\nCapacidad alumnos: " + str(self.get_capacidad()) + "\nPresupuesto: $" + str(self.get_presupuesto()))
        print("-------------------------------------------------------------\n")

        print("------------------------- Profesores ------------------------")
        for i in self.profesores:
            print("Cedula: " + str(i.get_cedula()) + ", Nombre: " + str(i.get_nombre()))

class Clase:
    
    def __init__(self, nombre_materia, id_salon, cedula_profesor, horario):
        self.nombre_materia = nombre_materia
        self.id_salon = id_salon
        self.cedula_profesor = cedula_profesor
        self.horario = horario
        self.alumnos = []
    
    def set_nombre_materia(self, nombre_materia):
        self.nombre_materia = nombre_materia

    def get_nombre_materia(self):
        return self.nombre_materia

    def set_id_salon(self, id_salon):
        self.id_salon = id_salon

    def get_id_salon(self):
        return self.id_salon

    def set_cedula_profesor(self, cedula_profesor):
        self.cedula_profesor = cedula_profesor

    def get_cedula_profesor(self):
        return self.cedula_profesor

    def set_horario(self, horario):
        self.horario = horario

    def get_horario(self):
        return self.horario

    def set_alumnos(self, alumnos):
        self.alumnos = alumnos

    def get_alumnos(self):
        return self.alumnos

    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)


class Profesor:

    def __init__(self, cedula, nombre, id_materia_dicta, sueldo_anio):
        self.cedula = cedula
        self.nombre = nombre
        self.id_materia_dicta = id_materia_dicta
        self.sueldo_anio = sueldo_anio
        self.materias_dictando = materias_dictando = []
    
    def set_cedula(self, cedula):
        self.cedula = cedula

    def get_cedula(self):
        return self.cedula

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_id_materia_dicta(self, id_materia_dicta):
        self.id_materia_dicta = id_materia_dicta

    def get_id_materia_dicta(self):
        return self.id_materia_dicta

    def set_sueldo_anio(self, sueldo_anio):
        self.sueldo_anio = sueldo_anio

    def aumentar_sueldo(self, incremento_sueldo):
        self.sueldo_anio += incremento_sueldo

    def get_sueldo_anio(self):
        return self.sueldo_anio

    def set_materias_dictando(self, materias_dictando):
        self.materias_dictando = materias_dictando

    def get_materias_dictando(self):
        return self.materias_dictando
    

class Alumno:

    def __init__(self, cedula, nombre, edad, anio_cursa):
        self.cedula = cedula
        self.nombre = nombre
        self.edad = edad
        self.anio_cursa = anio_cursa
        self.horarios = []
        self.materias_haciendo = materias_haciendo = []

    
class Materia:

    def __init__(self, id, nombre, descripcion, anio_cursarse):
            self.id = id
            self.nombre = nombre
            self.descripcion = descripcion
            self.anio_cursarse = anio_cursarse

    def set_id(self, nombre):
        self.id = id
        
    def get_id(self):
        return self.id

    def set_nombre(self, nombre):
        self.nombre = nombre
        
    def get_nombre(self):
        return self.nombre

    def set_descripcion(self, descripcion):
        self.descripcion = descripcion

    def get_descripcion(self):
        return self.descripcion

    def set_anio_cursarse(self, anio_cursarse):
        self.anio_cursarse = anio_cursarse

    def get_anio_cursarse(self):
        return self.anio_cursarse


class Salon:

    def __init__(self, id, lugar, descripcion):
        self.id = id
        self.lugar = lugar
        self.descripcion = descripcion
        self.horarios_ocupado = []
    

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id 
    
    def set_lugar(self, lugar):
        self.lugar = lugar

    def get_lugar(self):
        return self.lugar
    
    def set_descripcion(self, descripcion):
        self.descripcion = descripcion

    def get_lugar(self):
        return self.lugar
    
    def ocupar_salon(self, hora):
        self.horarios_ocupado.append(hora)

    def liberar_salon(self, hora):
        for i in self.horarios_ocupado:
            if hora == i:
                self.horarios_ocupado.remove(i)


class Main:

    escuelta7 = Escuela("Escuelta N°7 Zorrilla de San Martin", "Eguren y Laguna", 200000, 400)
    escuelta7.contratar_profesor(5631554, "Bruno Albín", 123, 5000)

    escuelta7.imprimir_informacion()
    