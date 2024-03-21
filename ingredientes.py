from pizza import Pizza

posibles_ingredientes = ["Pollo", "Vacuno", "Carne vegetal", "Tomate", "Aceitunas", "Champiñones"]
print(Pizza.validar_elemento("Pollo", posibles_ingredientes))
print(Pizza.validar_elemento("Pescado", posibles_ingredientes))

tipo_de_masa = ["Tradicional", "Delgada"]
print(tipo_de_masa)