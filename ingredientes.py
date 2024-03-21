from pizza import Pizza

posibles_ingredientes = ["pollo", "carne", "carne vegetal", "tomate", "aceitunas", "champiñones"]
print(Pizza.validar_elemento("pollo", posibles_ingredientes))
print(Pizza.validar_elemento("pescado", posibles_ingredientes))

tipo_de_masa = ["tradicional", "delgada"]
print(tipo_de_masa)