# el nombre de la clase siempre debe empezar con mayusccula

class Persona:
    """
    Existe una funcion que se ejecuta cuando instancioiamos a nuestra clase, a esa funccion se le dice constructor, podemosa tener mas de 1 y la forma en la que utililza en python es con el nombre __init__
    cuando estamos dentro de una clase el primer parametro de todas las funciones  sera self, luego podemos colocar los parametros que queramos 
    """

    def __init__(self, nombre, apellido, edad,  altura, direccion, peso):
        """
        vamos a agregar propriendades a aself y para hacer estos es de la siguinete m,anera
        swel.nombre_de_la prorpiedad = valor 

        """
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.altura = altura
        self.direccion = direccion
        self.peso = peso

    def saludar(self):
        return f"hola me llamo{self.nombre} {self.apellido}, tengo {self.edad} anos de edad."
    
    def mostrar_direccion(self):
        return f"vivo en la avenida{self.direccion}"


"""
para poder instanmciAR UNA CLASE, DEBEMOS SIMPLEMENTE LLAMARLA POR SU NOMBRE  Y GUARDARLA EN  UNA VARIABLE

"""
persona1 = Persona("Pepe", "Perez", 29, 1.94, "av mi casa 123", 85.4)
print(persona1.saludar())
print(persona1.mostrar_direccion())


    