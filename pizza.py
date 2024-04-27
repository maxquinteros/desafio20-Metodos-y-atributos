class Pizza:
    """
    Ingredientes: Vegetales y Proteicos

    Masa: Tradicional o Delgada

    No siempre están todas las alternativas posibles.

    Cualquier pizza ordenada debe tener 1 ingrediente proteico y dos vegetales.

    Todas las pizzas tienen un precio de $10.000 y tamaño familiar.
    """
    ############## Punto 1 ########################
    ingredientes_proteicos_disponibles = ["pollo", "vacuno", "carne vegetal"]
    ingredientes_vegetales_disponibles = ["tomate", "aceitunas", "champiñones"]
    masa_disponible = ["tradicional", "delgada"]
    precio = 10000
    tamano = "Familiar"
    
    def crear_pizza(self):
        self.ingrediente1_proteico = ""
        self.ingrediente2_vegetal = ""
        self.ingrediente3_vegetal = ""
        self.masa = ""
        self.es_valida = False
     
    ######## Punto 2 ###########
    @staticmethod
    def validar_elemento(elemento: str, lista: list) -> bool:
        if elemento in lista:
            return True
        else:
            return False

    ######## Punto 3 ###########
    def realizar_pedido(self):
        self.ingrediente1_proteico = input("Ingrese el ingrediente proteico (pollo o vacuno o carne vegetal):\n").lower()
        self.ingrediente2_vegetal = input("Ingrese el primer ingrediente vegetal (tomate o aceitunas o champiñones):\n").lower()
        self.ingrediente3_vegetal = input("Ingrese el segundo ingrediente vegetal (tomate o aceitunas o champiñones):\n").lower()
        self.masa = input("Ingrese el tipo de masa (tradicional o delgado):\n").lower()
        
        ######## Punto 4 ###########
        self.es_valida = (
            Pizza.validar_elemento(self.ingrediente1_proteico, self.ingredientes_proteicos_disponibles)
            and Pizza.validar_elemento(self.ingrediente2_vegetal, self.ingredientes_vegetales_disponibles)
            and Pizza.validar_elemento(self.ingrediente3_vegetal, self.ingredientes_vegetales_disponibles)
            and Pizza.validar_elemento(self.masa,self.masa_disponible)
        )
