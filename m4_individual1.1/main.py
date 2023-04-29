import time,os
# Stock inicial de productos y clientes
stock = {'Zapatillas' : 20, 'Poleras' : 10, 'Zapatos' : 15, 'Poleron' : 3, 'Chaqueta' : 5, 'Guantes' : 5}
clientes = {
    '1' : {'nombre' : 'Alberto García', 'password' : 'Alberto_1990', 'ciudad' : 'Viña del Mar', 'volumen_compra' : 14990},
    '2' : {'nombre' : 'Jose Martínez'},
    '3' : {'nombre' : 'Steffania Schweikart'},
    '4' : {'nombre' : 'Marcos Alarcón'},
    '5' : {'nombre' : 'Luis Martínez'},
    '6' : {'nombre' : 'Baltasar Fernández'}}
compras = []

# Función decorativa de cada sección
def banner(seccion):
    os.system('cls')
    print('*'*10+seccion+'*'*10)
    
# Verificar el stock antes de procesar la compra
def verifica_stock(producto,cantidad):
    if stock[producto] >= cantidad:
        return True
    else:
        return False
    
# Clases Usuario y subclases
class Usuario:
    def __init__(self, id, nombre, password):
        self.id = id
        self.nombre = nombre
        self.password = password
        
class Administrativo(Usuario):
    def __init__(self, id, nombre, password, fecha_incorporacion, oficina, salario):
        self.fecha_incorporacion = fecha_incorporacion
        self.oficina = oficina
        self.salario = salario
        super().__init__(id, nombre, password)
        
    # Almacenar nuevos productos
    def ingresa_producto(self):
        banner('Ingresar nuevo producto')
        producto = input('Ingrese el nombre del nuevo producto: ')
        cantidad = int(input('¿Cuántas unidades tendremos de este producto?: '))
        if producto not in stock:
            stock.update({producto : cantidad})
            print('Se añadió el producto al catálogo')
        else:
            stock[producto] = stock[producto] + cantidad
            print(f'El producto ya está en nuestro catálogo, se añadieron {cantidad} unidades de {producto}')
        time.sleep(2)
    
    # Ingresa nuevo cliente a la "base de datos"
    def ingresa_cliente(self):
        banner('Ingresar nuevo cliente')
        nombre = input('Ingrese el nombre del cliente: ')
        password = input('Ingrese la contraseña del cliente: ')
        if nombre not in clientes:
            id = int(list(clientes)[-1]) + 1
            clientes[str(id)] = {'nombre' : nombre, 'password' : password}
            print('Se añadió el cliente a la base de datos')
        else:
            print('El cliente ya está registrado, se ignorarán lso datos')
        time.sleep(2)
        
    # Mostrar clientes registrados
    def listado_clientes(self):
        banner('Nuestros clientes')
        for key in clientes:
            if clientes[key]["nombre"] != '':
                print(f'{key}) {clientes[key]["nombre"]}')
        
class Vendedor(Usuario):
    def __init__(self, id, nombre, password, fecha_incorporacion, seccion, salario):
        self.fecha_incorporacion = fecha_incorporacion
        self.seccion = seccion
        self.salario = salario
        super().__init__(id, nombre, password)
    
    # Añadir unidades a un producto del catálogo
    def actualiza_stock(self):
        banner('Actualizar stock')
        print('Seleccione el producto al cual añadiremos unidades')
        stockNames = []
        stockList = []
        i = 1
        for key in stock:
            stockNames.append(key)
            stockList.append(stock[key])
            print(f'{i}) {key}')
            i += 1
        producto = int(input('Ingrese el número del producto:'))
        cantidad = int(input('¿Cuántas unidades añadiremos?: '))
        stock[stockNames[producto-1]] = stock[stockNames[producto-1]] + cantidad
        
    # Mostrar unidades por producto
    def muestra_unidades(self):
        banner('Unidades por producto')
        for producto in stock:
            print(f'{producto}: {stock[producto]}')
            
    # Mostrar unidades de un producto en particular
    def muestra_unidades_producto(self):
        banner('Unidades de un producto')
        print('Seleccione el producto del cual quiere saber las unidades en stock')
        # Listas auxiliares para mostrar los nombres de los productos y almacenar temporalmente el stock
        stockNames = []
        stockList = []
        i = 1
        for key in stock:
            stockNames.append(key)
            stockList.append(stock[key])
            print(f'{i}) {key}')
            i += 1
        producto = int(input('Ingrese el número del producto:'))
        if producto <= len(stockList) and producto > 0:
            print(f'Tenemos actualmente {stockList[producto-1]} unidades de {stockNames[producto-1]}')
        else:
            print('Introdujo una opción incorrecta')
            time.sleep(2)


# Mostrar los productos que tienen más de X unidades
    def productos_mascantidad(self):
        banner('Productos con más que X cantidad')
        cantidad = int(input('Ingrese la cantidad: '))
        os.system('cls')
        banner(f'Productos con stock de más de {cantidad} unidades')
        for producto in stock:
            if stock[producto] > cantidad:
                print(f'{producto}: {stock[producto]}')

class Cliente(Usuario):
    def __init__(self, id, nombre, password, ciudad, volumen_compra = 0):
        self.ciudad = ciudad
        self.volumen_compra = volumen_compra
        super().__init__(id, nombre, password)
        
    # Mostrar todos los productos de la tienda
    def muestra_catalogo(self):
        banner('Nuestro catálogo')
        i = 1
        for key in stock:
            print(f'{i}) {key}')
            i += 1
    
    # Solicitar compra. Se pide producto y unidades
    def solicita_compra(self):
        cliente = self.id
        banner('Efectuar compra')
        stockNames = []
        i = 1
        for key in stock:
            stockNames.append(key)
            print(f'{i}) {key}')
            i += 1
        producto = int(input('Ingrese el número del producto: '))
        cantidad = int(input('Ingrese la cantidad de unidades: '))
        # Llamamos a la función que verifica si hay stock suficiente de lo que queremos comprar
        autorizado = verifica_stock(stockNames[producto-1],cantidad)
        if autorizado:
            stock[stockNames[producto-1]] = stock[stockNames[producto-1]] - cantidad
            print('Compra autorizada y en camino')
            compras.append({'cliente' : cliente, 'producto' : stockNames[producto-1], 'cantidad' : cantidad})
        else:
            print('Compra cancelada, no hay suficiente cantidad de productos')
        print(compras)

# Creamos los objetos con las nuevas clases
administrativo = Administrativo('a1','Paulina Fernández','Paulina_1992','2023/03/05','Quilpué',1120000)
vendedor = Vendedor('v1','Marcos Pérez','Marcos_45','2023/04/15','Informática',850000)
cliente = Cliente('1',clientes['1']['nombre'],clientes['1']['password'],clientes['1']['ciudad'],clientes['1']['volumen_compra'])

# Lista con llamadas a las funciones del menú
functions = ['', administrativo.ingresa_cliente, administrativo.ingresa_producto, vendedor.actualiza_stock, vendedor.muestra_unidades, vendedor.muestra_unidades_producto, cliente.muestra_catalogo, vendedor.productos_mascantidad, administrativo.listado_clientes, cliente.solicita_compra]


while True:
    banner('Bienvenido')
    # Imprimir el menú
    print('1) Ingresa nuevo cliente\n2) Ingresar nuevo producto\n3) Añadir unidades a producto existente\n4) Mostrar unidades por producto\n5) Ver las unidades de un producto\n6) Muestra el catálogo\n7) Productos con más de X cantidad en stock\n8) Mostrar listado de clientes\n\n9) Efectuar compra\n0) Salir')
    eleccion = int(input('Su elección: '))
    if eleccion == 0:
        print('Gracias, vuelva pronto')
        time.sleep(2)
        break
    elif eleccion >= len(functions):
        print('Ha seleccionado una opción incorrecta')
    else:
        # Llamamos a la función correspondiente a la posición en la lista
        functions[eleccion]()
    input('Pulse Enter para continuar')
