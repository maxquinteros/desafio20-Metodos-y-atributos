from pizza import Pizza

######## Punto 5.a ###########
print(f"El precio de la pizza es: ${Pizza.precio}")
print(f"El tamaño de la pizza es: {Pizza.tamano}")
print(
    f"Los ingredientes proteicos disponibles son: {Pizza.ingredientes_proteicos_disponibles}"
)
print(
    f"Los ingredientes vegetales disponibles son: {Pizza.ingredientes_vegetales_disponibles}"
)
print(f"Los tipos de masa disponibles son: {Pizza.masa_disponible}")

######## Punto 5.b ###########
print(Pizza.validar_elemento("salsa de tomate", ["salsa de tomate", "salsa bbq"]))

######## Punto 5.c ###########
pizza1 = Pizza()
pizza1.realizar_pedido()

######## Punto 5.d ###########
print(f"El ingrediente proteico seleccionado fue: {pizza1.ingrediente1_proteico}")
print(f"El primer ingrediente vegetal seleccionado fue: {pizza1.ingrediente2_vegetal}")
print(f"El segundo ingrediente vegetal seleccionado fue: {pizza1.ingrediente3_vegetal}")
print(f"La masa seleccionada fue: {pizza1.masa}")

if pizza1.es_valida:
    print("La instancia es válida")
else:
    print("La instancia no es válida")
    
'''
######## Punto 5.e ###########
if Pizza.es_valida:
    print("La clase es válida")
else:
    print("La clase no es válida")
'''