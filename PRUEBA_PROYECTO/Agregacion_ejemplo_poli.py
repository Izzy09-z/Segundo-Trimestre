# CLASES BASE
class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.catalogo = []
        self.usuarios_registrados = []
        self.prestamos_activos = []  # Atributo nuevo

    def registrar_usuario(self, usuario):
        self.usuarios_registrados.append(usuario)

    def agregar_libro(self, libro):
        self.catalogo.append(libro)

    def buscar_libro(self, titulo):
        for libro in self.catalogo:
            if libro.titulo == titulo:
                return libro
        return None

    # Método nuevo para mostrar estadísticas
    def estadisticas(self):
        return {
            'total_libros': len(self.catalogo),
            'total_usuarios': len(self.usuarios_registrados),
            'prestamos_activos': len(self.prestamos_activos)
        }

class Libro:
    def __init__(self, isbn, titulo, año_publicacion, ejemplares, genero=None):
        self.isbn = isbn
        self.titulo = titulo
        self.año_publicacion = año_publicacion
        self.estado = "disponible"
        self.ejemplares = ejemplares
        self.genero = genero  # Atributo nuevo
        self.veces_prestado = 0  # Atributo nuevo para estadísticas

    def prestar(self):
        if self.esta_disponible():
            self.ejemplares -= 1
            self.veces_prestado += 1  # Nuevo: contador de préstamos
            if self.ejemplares == 0:
                self.estado = "prestado"
            return True
        return False

    def devolver(self):
        self.ejemplares += 1
        self.estado = "disponible"

    def esta_disponible(self):
        return self.ejemplares > 0

    # Método nuevo para obtener información extendida
    def info_extendida(self):
        return f"'{self.titulo}' ({self.año_publicacion}) - Género: {self.genero} - Prestado {self.veces_prestado} veces"

class Usuario:
    def __init__(self, id_usuario, nombre, correo):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.libros_prestados = []
        self.max_libros = 3  # Atributo nuevo
        self.dias_prestamo = 15  # Atributo nuevo

    def solicitar_prestamo(self, libro):
        if len(self.libros_prestados) >= self.max_libros:
            print(f"{self.nombre} ya tiene el máximo de libros prestados ({self.max_libros})")
            return False
        if libro.prestar():
            self.libros_prestados.append(libro)
            return True
        return False

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.devolver()
            self.libros_prestados.remove(libro)
            return True
        return False

    # Método nuevo para mostrar información del usuario
    def mostrar_info(self):
        return f"Usuario: {self.nombre} ({self.correo})"

# HERENCIA: Estudiante hereda de Usuario
class Estudiante(Usuario):
    def __init__(self, id_usuario, nombre, correo, carrera):
        super().__init__(id_usuario, nombre, correo)
        self.carrera = carrera  # Atributo específico de Estudiante
        self.max_libros = 5  # Sobrescribe el valor para estudiantes
        self.dias_prestamo = 30  # Más días de préstamo

    # Polimorfismo: método específico para estudiantes
    def mostrar_info(self):
        return f"Estudiante: {self.nombre} - Carrera: {self.carrera}"

# HERENCIA: Profesor hereda de Usuario
class Profesor(Usuario):
    def __init__(self, id_usuario, nombre, correo, departamento):
        super().__init__(id_usuario, nombre, correo)
        self.departamento = departamento  # Atributo específico
        self.max_libros = 10  # Profesores pueden pedir más libros
        self.dias_prestamo = 60  # Mucho más tiempo de préstamo

    # Polimorfismo: método específico para profesores
    def mostrar_info(self):
        return f"Profesor: {self.nombre} - Departamento: {self.departamento}"

class Prestamo:
    def __init__(self, id_prestamo, fecha_prestamo, fecha_devolucion, usuario, libro):
        self.id_prestamo = id_prestamo
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.usuario = usuario
        self.libro = libro

    def calcular_multa(self):
        # Implementar lógica de multa aquí (ejemplo simple)
        from datetime import date
        hoy = date.today()
        if hoy > self.fecha_devolucion:
            dias_retraso = (hoy - self.fecha_devolucion).days
            return dias_retraso * 2.0  # $2 por día de retraso
        return 0.0

class Autor:
    def __init__(self, id_autor, nombre, nacionalidad):
        self.id_autor = id_autor
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

# FUNCIÓN PARA DEMOSTRAR POLIMORFISMO
def mostrar_informacion_usuarios(usuarios):
    """Función que demuestra polimorfismo: mismo método, comportamientos diferentes"""
    print("\n=== INFORMACIÓN DE USUARIOS (POLIMORFISMO) ===")
    for usuario in usuarios:
        # ¡Polimorfismo en acción! mismo método mostrar_info(), diferente comportamiento
        print(usuario.mostrar_info())
        print(f"Puede pedir hasta {usuario.max_libros} libros por {usuario.dias_prestamo} días")
        print("-" * 40)

# EJEMPLO DE USO
if __name__ == "__main__":
    # Crear biblioteca
    biblioteca_central = Biblioteca("Biblioteca Central")
    
    # Crear libros
    libro1 = Libro("123-ABC", "Cien años de soledad", 1967, 5, "Realismo mágico")
    libro2 = Libro("456-DEF", "1984", 1949, 3, "Ciencia ficción")
    libro3 = Libro("789-GHI", "Don Quijote", 1605, 2, "Novela")
    
    # Agregar libros a la biblioteca
    biblioteca_central.agregar_libro(libro1)
    biblioteca_central.agregar_libro(libro2)
    biblioteca_central.agregar_libro(libro3)
    
    # Crear diferentes tipos de usuarios (herencia)
    estudiante = Estudiante("U-001", "Ana García", "ana@email.com", "Ingeniería")
    profesor = Profesor("P-001", "Carlos Ruiz", "carlos@universidad.edu", "Matemáticas")
    usuario_normal = Usuario("U-002", "María López", "maria@email.com")
    
    # Registrar usuarios en la biblioteca
    biblioteca_central.registrar_usuario(estudiante)
    biblioteca_central.registrar_usuario(profesor)
    biblioteca_central.registrar_usuario(usuario_normal)
    
    # Simular préstamos
    print("=== SIMULACIÓN DE PRÉSTAMOS ===")
    estudiante.solicitar_prestamo(libro1)
    profesor.solicitar_prestamo(libro2)
    profesor.solicitar_prestamo(libro3)
    
    # Demostrar polimorfismo
    lista_usuarios = [estudiante, profesor, usuario_normal]
    mostrar_informacion_usuarios(lista_usuarios)
    
    # Mostrar información extendida de libros
    print("\n=== INFORMACIÓN DE LIBROS ===")
    for libro in biblioteca_central.catalogo:
        print(libro.info_extendida())
    
    # Mostrar estadísticas de la biblioteca
    print("\n=== ESTADÍSTICAS DE LA BIBLIOTECA ===")
    stats = biblioteca_central.estadisticas()
    print(f"Total libros: {stats['total_libros']}")
    print(f"Total usuarios: {stats['total_usuarios']}")
    print(f"Préstamos activos: {stats['prestamos_activos']}")