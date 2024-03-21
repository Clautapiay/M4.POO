#Que usuario pueda elegir 3 ingredientes y el tipo de masa
# Debe elegir 1 ingrediente proteico y 2 vegetales
# 2 tipos ingredientes --> vegetales y proteicos, pueden variar segun stock/estacionalidad
#Proteicos : pollo - vacuno - carne vegetal
#Vegetales : tomate - aceituna -champiñon 
# 2 tipos de masa --> tradicional y delgada
# Todas las pizzas valen $10.000 y son tamaño familiar


class Pizza():
    #atributos
    valor = "$10.000 pesos"
    tamano = "Familiar"
    proteicos_posibles = ["pollo", "carne", "carne vegetal"]
    vegetales_posibles = ["tomate", "aceituna", "champiñones"]
    masa_posible = ["tradicional", "delgada"]

    @staticmethod
    #validar elemento dentro de la lista
    def validar_elemento(elemento,valores_posibles):
        return elemento.lower() in valores_posibles
    

    def crear_pizza(self:str):
        self.masa = None
        self.ing_proteico = None
        self.ing_vegetal1 = None
        self.ing_vegetal2 = None
        self.es_valida = None 
    

    def realizar_pedido(self):
        self.masa = input(f"Ingrese el tipo de masa que desea (Tradicional/Delgada): ")
        self.ing_proteico = input(f"Ingrese la proteina que desea (Pollo/Carne/Proteina Vegetal): ")
        self.ing_vegetal1 = input(f"Ingrese el primer vegetal que desea (Tomate/Aceitunas/Champiñones): ")
        self.ing_vegetal2 = input(f"Ingrese el segundo vegetal que desea (Tomate/Aceitunas/Champiñones): ")

#vaidar si ingredientes y tipo de masa son validos
    def es_valida(self):
        
        ingredientes_proteicos = ["carne", "pollo", "carne vegetal"]
        ingredientes_vegetales = ["aceitunas", "champiñones", "tomate"]
        masas = ["tradicional", "delgada"]

        proteico_valido = self.validar_elemento(self.ing_proteico, ingredientes_proteicos)
        vegetal1_valido = self.validar_elemento(self.ing_vegetal1, ingredientes_vegetales)
        vegetal2_valido = self.validar_elemento(self.ing_vegetal2, ingredientes_vegetales)
        masa_valida = self.validar_elemento(self.masa, masas) 
        print(proteico_valido, vegetal1_valido, vegetal2_valido, masa_valida)

        if proteico_valido and vegetal1_valido and vegetal2_valido and masa_valida:
            self.es_valida = True
            print("La pizza es válida")
        else:
            self.es_valida = False
            print("La pizza no es válida")
        
    

    def resumen_pizza(self):
        return f"Pizza {self.tamano} de masa {self.masa} con {self.ing_proteico}, {self.ing_vegetal1} y {self.ing_vegetal2}"
