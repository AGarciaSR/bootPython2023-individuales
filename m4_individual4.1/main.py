import time,os

# Clases Usuario y subclases
class Usuario(object):
    def __init__(self, id, nombre, apellido, password):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.password = password
        
    def saluda_usuario(self):
        print(f"Hola, me llamo {self.nombre}, y mi rol es de {self.__class__.__name__} pelao, sin ná que hacer")
        
class Administrativo(Usuario):
    def __init__(self, id, nombre, apellido, password, fecha_incorporacion, oficina, salario, fecha_nacimiento = None):
        super().__init__(id, nombre, apellido, password)
        self.fecha_incorporacion = fecha_incorporacion
        self.oficina = oficina
        self.salario = salario
        self.fecha_nacimiento = fecha_nacimiento
    
    def saluda_usuario(self):
        print(f"Hola, me llamo {self.nombre}, y mi rol es de {self.__class__.__name__}, déjame que tengo mucho que hacer")
        
class Contable(Administrativo):
    def __init__(self, id, nombre, apellido, password, fecha_incorporacion, oficina, salario, anyos_experiencia, fecha_nacimiento = None):
        super().__init__(id, nombre, apellido, password, fecha_incorporacion, oficina, salario, fecha_nacimiento)
        self.anyos_experiencia = anyos_experiencia
        
    def revisa_factura(self, factura):
        print(f"Revisando la factura número {factura}")
        
    def saluda_usuario(self):
        print(f"Hola, me llamo {self.nombre}, y mi rol es de {self.__class__.__name__}, si no me vas a ayudar con estas facturas, te agradeceré que me dejes tranquilo")
        
class Encargado(Administrativo):
    def __init__(self, id, nombre, apellido, password, fecha_incorporacion, oficina, salario, bono_objetivo, fecha_nacimiento = None):
        super().__init__(id, nombre, apellido, password, fecha_incorporacion, oficina, salario, fecha_nacimiento)
        self.bono_objetivo = bono_objetivo
        
    def compra_art_oficina(self):
        print("Comprando más artículos de oficina")
        
    def saluda_usuario(self):
        print(f"Hola, me llamo {self.nombre}, y mi rol es de {self.__class__.__name__}, tengo que andar detrás de todos, ni que fuera nana oye")

class Vendedor(Usuario):
    def __init__(self, id, nombre, apellido, password, run, fecha_incorporacion, salario, seccion = None):
        super().__init__(id, nombre, apellido, password)
        self.fecha_incorporacion = fecha_incorporacion
        self.seccion = seccion
        self.salario = salario
        self.run = run
        self.__comision = 0
    
    def saluda_usuario(self):
        print(f"Hola, me llamo {self.nombre}, y mi rol es de {self.__class__.__name__}, aquí ganándome mi comisión si")

class Cliente(Usuario):
    def __init__(self, id, nombre, apellido, correo, fecha_registro, password, ciudad, volumen_compra = 0, genero = None):
        self.apellido = apellido
        self.correo = correo
        self.fecha_registro = fecha_registro
        self.ciudad = ciudad
        self.volumen_compra = volumen_compra
        # Atributo encapsulado
        self.__saldo = 500000
        super().__init__(id, nombre, apellido, password)
    
class Producto:
    def __init__(self, sku, nombre, categoria, stock, valor_neto) -> None:
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.stock = stock
        self.valor_neto = valor_neto
        self.__impuesto = 1.19
        self.proveedor = None
        
class Proveedor:
    def __init__(self, rut, nombre_legal, razon_social, pais, tipo_persona):
        self.rut = rut
        self.nombre_legal = nombre_legal
        self.razon_social = razon_social
        self.pais = pais
        self.tipo_persona = tipo_persona

# Creamos los objetos con las nuevas clases
usuario = Usuario('1','Alberto','García','NoSeXD_4820')
administrativo = Administrativo('a1','Paulina','Fernández','Paulina_1992','2023/03/05','Quilpué',1120000)
vendedor = Vendedor('v1','Marcos','Pérez','Marcos_45','12345678-9','2023/04/15','Informática',800000)
encargado = Encargado('v2','Fernando','Herrera','Marcos_45','12345678-9','2023/04/15','Informática',800000)
contable = Contable('cont1','Cristian','Martínez','Cris_77','12345678-9','2023/04/15','Informática',800000)
usuario.saluda_usuario()
administrativo.saluda_usuario()
vendedor.saluda_usuario()
contable.saluda_usuario()
encargado.saluda_usuario()