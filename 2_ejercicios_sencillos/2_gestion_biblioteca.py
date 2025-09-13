class Libro:
    def __init__(self, id, title, description, author):
        self.id = id
        self.title = title
        self.description = description
        self.author = author
        self.avaliable = True

    def lend(self):
        self.avaliable = False

    def devolver(self):
        self.avaliable = True


class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.borrowed_books = []

    def order_book(self, id_book):
        self.borrowed_books.append(id_book)

    def return_book(self, id_book):
        if self.borrowed_books.__contains__(id_book):
            self.borrowed_books.remove(id_book)


class Library:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.list_books = []
        self.users = []

    def register_user(self, id, name):
        self.users.append(User(id, name))

    def add_book(self, id , title, description, author):
        self.list_books.append(Libro(id, title, description, author))

    def lend_book(self, id_book, id_user):
        for i in self.list_books:
            if i.id == id_book:
                if i.avaliable == False:
                    print("\nEl libro con id: "+ str(i.id)+ " no se encuentra disponible\n")
                else:
                    print("\nLibro con id: "+ str(i.id)+ " solcitado con exito por la persona con CI: "+str(id_user)+"\n")
                    for x in self.users:
                        if x.id == id_user:
                            x.order_book(id_book)
                            i.avaliable = False


    def return_book(self, id_book, id_user):
        for i in self.list_books:
            if i.id == id_book:
                if i.avaliable == True:
                    print("\nEl libro con id: "+ str(i.id)+ " no se puede devolver porque ya está disponible\n")
                else:
                    print("\nLibro con id: "+ str(i.id)+ " devuelto con exito por la persona con CI: "+str(id_user)+"\n")
                    for x in self.users:
                        if x.id == id_user:
                            x.return_book(id_book)
                            i.avaliable = True

    def print_books_in(self):
        print("----------------------------------BOOKS----------------------------------")
        for i in self.list_books:
            if i.avaliable == True:
                print("Libro: " + i.title + " - Autor: " + i.author + " - Disponible: Si ")
            else:
                print("Libro: " + i.title + " - Autor: " + i.author + " - Disponible: No ")

    def list_people(self):
        print("----------------------------------PEOPLE---------------------------------")
        if not self.users:
                print("Aún no hay usuarios registrados")
                print("--------------------------------------")
        else:
            for i in self.users:
                if not i.borrowed_books:
                    print("Cedula: " + str(i.id) + " - Nombre: " + i.name + "\nLibros: No tiene libros solicitados")
                else:
                    print("Cedula: " + str(i.id) + " - Nombre: " + i.name + "\nLibros: ")
                    for j in i.borrowed_books:
                        for h in self.list_books:
                            if j == h.id:
                                print("Libro: " + h.title + " - Id: " + str(h.id))
                print("--------------------------------------")

# Crear biblioteca
library = Library("Library Montes del Plata", "Nueva Palmira, Lucas Roselli 1331")

# Crear libros
library.add_book(1, "Game of Thrones 1", "Game of Thrones is an acclaimed fantasy drama TV series that aired on HBO from 2011 to 2019, based on George R.R. Martin's book series A Song of Ice and Fire", "George R. R. Martin")
library.add_book(2, "Game of Thrones 2", "Game of Thrones is an acclaimed fantasy drama TV series that aired on HBO from 2011 to 2019, based on George R.R. Martin's book series A Song of Ice and Fire - V2", "George R. R. Martin")
library.add_book(3, "Game of Thrones 3", "Game of Thrones is an acclaimed fantasy drama TV series that aired on HBO from 2011 to 2019, based on George R.R. Martin's book series A Song of Ice and Fire - V3", "George R. R. Martin")
library.add_book(4, "101 Dalmatas", "Libro de perros dalmatas", "Robert de Niro")
library.add_book(5, "Peaky Blinders", "Pandilla de Birmhigham post primer guerra mundial", "Angelina Jolie")
library.add_book(6, "La guerra", "Trata de una guerra que gano messi", "Lionel Messi")

# Crear usuario
library.register_user(56315544, "Bruno Albin")
library.register_user(12341234, "Robertinshio")
library.register_user(44444444, "Lionel Messi")
library.register_user(23232323, "CR7")
library.register_user(56310000, "Juan Chori")

# Solcitar libro 
library.lend_book(2, 56315544)
library.list_people()
library.print_books_in()
library.return_book(2, 56315544)
library.list_people()
library.print_books_in()
