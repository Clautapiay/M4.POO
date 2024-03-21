from pizza import Pizza

print("Precio de todas las pizzas:", Pizza.valor)
print("Tamaño de todas las pizzas:", Pizza.tamano)

salsa_posible = ["Salsa de tomate", "Salsa BBQ"]

salsa_esta_en = Pizza.validar_elemento("Salsa de tomate", salsa_posible)

if salsa_esta_en:
    print("La Salsa de tomate está presente en la lista")
else:
    print("La Salsa de tomate no está presente en la lista")

crear_pizza = Pizza()
crear_pizza.realizar_pedido()
print("Pizza creada")

print("Imgrediente proteico:", crear_pizza.ing_proteico) 
print("Primer Imgrediente vegetal:", crear_pizza.ing_vegetal1)
print("Segundo Imgrediente vegetal:", crear_pizza.ing_vegetal2)
print("Tipo de masa:", crear_pizza.masa)   

if crear_pizza.es_valida():
    print("Esta instancia es una pizza valida")
else:
    print("Esta instancia no es una pizza valida")



#debe dar error
if Pizza.es_valida():
    print("La pizza es valida")
else:
    print("La pizza no es valida")