class SistemaEscolar:
    def __init__(self):
        self.alumnos = {}
        self.profesores = {}
        self.cursos = {}
        self.horario_profesores = {}
        self.horario_cursos = {}

    def registrar_alumno(self, nombre, curso):
        self.alumnos[nombre] = curso

    def registrar_profesor(self, nombre):
        self.profesores[nombre] = []

    def asignar_profesor_a_curso(self, profesor, curso):
        if curso not in self.cursos:
            self.cursos[curso] = []
        self.cursos[curso].append(profesor)

    def asignar_horario_profesor(self, profesor, curso, dia, hora_desde, hora_hasta):
        clave = (curso, dia)
        if clave not in self.horario_profesores:
            self.horario_profesores[clave] = []
        self.horario_profesores[clave].append((profesor, hora_desde, hora_hasta))

    def asignar_horario_curso(self, curso, dia, hora_desde, hora_hasta):
        clave = (curso, dia)
        if clave not in self.horario_cursos:
            self.horario_cursos[clave] = (hora_desde, hora_hasta)

    def exportar_alumnos_curso(self, curso):
        print(f"Alumnos en el curso '{curso}':")
        for alumno, curso_alumno in self.alumnos.items():
            if curso_alumno == curso:
                print(alumno)

    def exportar_horario_profesor(self, profesor, curso):
        clave = (curso, dia)
        if clave in self.horario_profesores:
            print(f"Horario de '{profesor}' en el curso '{curso}':")
            for p, hora_desde, hora_hasta in self.horario_profesores[clave]:
                if p == profesor:
                    print(f"Día: {dia}, Desde: {hora_desde}, Hasta: {hora_hasta}")

    def exportar_horario_curso(self, curso):
        clave = (curso, dia)
        if clave in self.horario_cursos:
            hora_desde, hora_hasta = self.horario_cursos[clave]
            print(f"Horario del curso '{curso}':")
            print(f"Día: {dia}, Desde: {hora_desde}, Hasta: {hora_hasta}")


# Ejemplo de uso del sistema
sistema = SistemaEscolar()
sistema.registrar_alumno("Juan", "Matemáticas")
sistema.registrar_alumno("Maria", "Historia")
sistema.registrar_profesor("Profesor A")
sistema.asignar_profesor_a_curso("Profesor A", "Matemáticas")
sistema.asignar_horario_profesor("Profesor A", "Matemáticas", "Lunes", "08:00", "10:00")
sistema.asignar_horario_curso("Matemáticas", "Lunes", "08:00", "10:00")

# Exportar información
sistema.exportar_alumnos_curso("Matemáticas")
sistema.exportar_horario_profesor("Profesor A", "Matemáticas")
sistema.exportar_horario_curso("Matemáticas")
