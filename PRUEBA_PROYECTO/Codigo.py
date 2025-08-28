class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.prestado = False
    
    def prestar(self):
        if not self.prestado:
            self.prestado = True
            return True
        return False
    
    def devolver(self):
        self.prestado = False

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []
    
    def tomar_libro(self, libro):
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

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None

    def buscar_usuario(self, id_usuario):
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                return usuario
        return None

# Interfaz con registro de usuarios
def main():
    bib = Biblioteca()
    
    # Datos iniciales
    bib.agregar_libro(Libro("Cien años de soledad", "García Márquez"))
    bib.agregar_libro(Libro("1984", "George Orwell"))
    
    while True:
        print("\n1. Registrar usuario")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Salir")
        
        op = input("Opción: ")
        
        if op == "1":
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID del usuario: ")
            
            if not bib.buscar_usuario(id_usuario):
                nuevo_usuario = Usuario(nombre, id_usuario)
                bib.registrar_usuario(nuevo_usuario)
                print("✓ Usuario registrado exitosamente")
            else:
                print("✗ Ya existe un usuario con ese ID")
                
        elif op == "2":
            if not bib.usuarios:
                print("✗ No hay usuarios registrados")
                continue
                
            titulo = input("Título del libro: ")
            id_user = input("ID usuario: ")
            
            libro = bib.buscar_libro(titulo)
            usuario = bib.buscar_usuario(id_user)
            
            if libro and usuario:
                if usuario.tomar_libro(libro):
                    print("✓ Préstamo exitoso")
                else:
                    print("✗ Libro no disponible")
            else:
                print("✗ Libro o usuario no encontrado")
                
        elif op == "3":
            if not bib.usuarios:
                print("✗ No hay usuarios registrados")
                continue
                
            titulo = input("Título del libro: ")
            id_user = input("ID usuario: ")
            
            libro = bib.buscar_libro(titulo)
            usuario = bib.buscar_usuario(id_user)
            
            if libro and usuario:
                if usuario.devolver_libro(libro):
                    print("✓ Devolución exitosa")
                else:
                    print("✗ Usuario no tiene este libro")
            else:
                print("✗ Libro o usuario no encontrado")
                
        elif op == "4":
            break

if __name__ == "__main__":
    main()