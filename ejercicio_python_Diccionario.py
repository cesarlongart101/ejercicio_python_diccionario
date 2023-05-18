import re #modulo importado para la función de validar correo electronico

# Funciones utilitarias

def is_only_digits (num):
    """ Función utilitaria que validar que los dígitos ingresados sean números."""
    for i in num:
        aux = ord(i)
        if aux not in range(48,58):
          return False
        return True

def is_valid_date(date):
    """ Función utilitaria que validar la fecha con los requerimientos solicitados en el ejercicio."""
    if len(date) != 10:
        return False
    if date[2] != "/" or date[5] != "/":
        return False
    dia = int(date[:2])
    mes = int(date[3:5])
    ano = int(date[6:])
    if ano < 1900:
        return False
    if mes >= 1 and mes <= 12:
        if mes == 2:
            if not ano % 4 and (ano % 100 or not ano % 400):
                if dia >= 1 and dia <= 29:
                    return True
                else:
                    return False
            elif dia >= 1 and dia <= 28:
                return True
            else:
                return False
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if dia >= 1 and dia <= 30:
                return True
            else:
                return False
        elif dia >= 1 and dia <= 31:
            return True
        else:
            return False
    else:
        return False

def is_valid_phone(phone):
    """ Función utilitaria que valida el número de teléfono y que llama a su vez a la función is_only_digits para validar que solo contenga números."""
    if len(phone) == 9:
        if phone[0] == "9" or phone[0] == "6":
            return is_only_digits(phone)
        else:
            return False
    else:
        return False

def is_valid_email(email):
    """ Función utilitaria que verifica que el correo electronico caracteres alfanumericos, simbolo arroba, seguido un dominnio."""
    if re.match("^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$", email.lower()):
        return True
    else:
        return False

def is_valid_nif(nif):
    """ Función utilitaria que verifica si el NIF es correcto, se utiliza un bucle para pedir nuevamente el NIF si no cumple con los requisitos"""
    while True:
        valido = len(nif) == 9
        if valido:
            nif_aux = nif[:8]
            letra = ord(nif[8:].upper())
            if is_only_digits(nif_aux):
                if letra >= 65 and letra <= 90:
                    return True, nif
                else:
                    print("-------------------------")
                    print("El último caracter debe ser una letra.")
                    print("-------------------------")
                    nif = input("Introduce el NIF del nuevo cliente: ").strip()
            else:
                print("-------------------------")
                print("Introduce un NIF valido, debe tener ocho digitos y una letra.")
                print("-------------------------")
                nif = input("Introduce el NIF del nuevo cliente: ").strip()
        else:
            print("-------------------------")
            print("Introduce un NIF valido, debe tener nueve caracteres.")
            print("-------------------------")
            nif = input("Introduce el NIF del nuevo cliente: ").strip()

def is_valid_name(name):
  """Función utilitaria que valida cadena de caracteres para nombre y apellido"""
  while True:
    if len(name) > 1:
      cont = 0
      for i in name:
        aux = ord(i.lower())
        if (aux > 96 and aux < 123) or aux == 241 or aux == 32:
          cont = cont + 1
          if cont == len(name):
            return name
        else:
          name = input("Intentalo nuevamente: ").strip()
    else:
      print("Al menos debe contener dos caracteres")
      name = input("Intentalo otra vez: ")

def pedir_habitual ():
    """Función que valida los datos sobre el el campo cliente habitual"""
    while True:
        habitual = input ("¿El cliente es habitual? Si / No ").strip()
        if habitual != "Si" and habitual != "No":
          print("Selecciona una opción correcta")
        else:
          if habitual == "Si":
            return True
          else:
            return False

title = "Listado de clientes"
caracter ="-"

def print_header (title, pad_chard):
  espacio = 57 + (len(title)//2)
  print_cabecera_1 = title.rjust(espacio, pad_chard).ljust(114, pad_chard)
  print_cabecera_2 = "NIF          |Nombre      |Apellido      |Dirección  |Teléfon          |Habitual |Fecha            |Correo                   "
  return print_cabecera_1 + "\n" + print_cabecera_2



#----------------------
# Funciones Principales
#----------------------


def agregar_cliente():
    """ Funcion para opción 1, llama a funciones utilitarias para validar y agrega los datos al diccionario dic_clientes."""
    nif = input ("Introduce el NIF del nuevo cliente: ").strip()
    nif = (is_valid_nif(nif)[1])
    nombre = input("Introduce nombre de cliente: ").strip()
    is_valid_name(nombre)
    apellidos = input("Introduce apellidos de cliente: ").strip()
    is_valid_name(apellidos)
    direccion = input("Introduce dirección: ").strip()
    telefono = input ("Introduce el teléfono del cliente: ").strip()
    is_valid_phone(telefono)
    correo = input("Introduce correo electrónico: ").strip()
    is_valid_email(correo)
    habitual = pedir_habitual()
    fecha = input("Introduce la fecha del nuevo cliente: ").strip()
    is_valid_date(fecha)

    dic_clientes[nif] = {"Nombre": nombre, "Apellidos": apellidos,\
                         "Dirección": direccion, "Teléfono": telefono, \
                         "habitual": habitual, "Fecha": fecha, "Correo electrónico": correo}
    print("--------------------------------------------------------")
    print("Se han creado los datos del cliente con NIF:", "{}".format(nif))
    print("--------------------------------------------------------")


def eliminar_cliente():
    """Función para eliminar cliente."""
    nif_eliminar = input ("Indique el NIF a eliminar: ")
    nif_aux = dic_clientes.pop(nif_eliminar, False)
    if nif_aux == False:
        print("El NIE no existe en el registro")
    else:
        print("--------------------------------------------------------")
        print("Se han eliminado los datos del cliente NIF {}".format(nif_eliminar))
        print("--------------------------------------------------------")

def mostrar_cliente():
    nif_cliente = input("Indique el NIF que desea consultar: ").strip()
    datos_aux = dic_clientes.get(nif_cliente, False)
    if datos_aux == False:
        print("El NIE no existe en el registro")
    else:
        print(print_header(title, caracter))
        for nif, datos in dic_clientes.items():
            if nif == None:
                continue
            elif nif_cliente == nif:

                print(nif, "   |", end=" ")
                for datos1, informacion in datos.items():
                    print(informacion, "     |", end=" ")

def todos_clientes():
    """Función para mostrar todos los clientes."""
    print(print_header(title, caracter))
    for nif, datos in dic_clientes.items():
      if nif == None:
        continue
      print(nif,"   |" , end=" ")
      for datos1, informacion in datos.items():
        print(informacion,"     |", end=" ")
      print("\n")

def clientes_habituales():
    """Función para mostrar todos los clientes habituales."""
    print(print_header(title, caracter))
    for nif, datos in dic_clientes.items():
        if nif == None:
            continue
        if datos["habitual"] == True:
            print(nif, "   |", end=" ")
            for datos1, informacion in datos.items():
                print(informacion, "     |", end=" ")
            print("\n")

def salir_fun():
    """función para salir el programa"""
    print()
    print("----------------------------")
    print("** Ha salido del programa **")
    print("----------------------------")
    exit()

def default():
    print("Selecciona una opción valida dentro del menú")

cases = {
    "1": agregar_cliente,
    "2": eliminar_cliente,
    "3": mostrar_cliente,
    "4": todos_clientes,
    "5": clientes_habituales,
    "6": salir_fun
}

#dic_clientes = {None:{}}

dic_clientes = {
    None:{},
    "77841238t" : {
        "nombre": "Cesar",
        "apellido" : "Longart",
        "direccion" : "Vigo",
        "telefono": "9999999999",
        "habitual" : True,
        "fecha" : "14/11/2022",
        "correo" : "cesar@email.com"
    },
    "12345678p" : {
        "nombre": "Cata",
        "apellido" : "Lagos",
        "direccion" : "Vigo",
        "telefono": "111111111",
        "habitual" : True,
        "fecha" : "24/02/2023",
        "correo" : "cata@email.com"
    }
}

def menu():
  """Función definida para imprimir menú en pantalla y pedir una opción al usuario"""
  salir =True
  while salir:
    print()
    print("__________________")
    print("------ MENU ------")
    print("__________________")
    print()
    print("1. Agregar cliente \n"
          "2. Eliminar cliente \n"
          "3. Mostrar cliente \n"
          "4. Mostrar todos los clientes \n"
          "5. Mostrar clientes habituales \n"
          "6. Salir \n     ")

    op = input("Seleccione una opción: ").strip()
    cases.get(op, default)()

menu()
