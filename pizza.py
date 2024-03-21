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
    proteicos_posibles = ["Pollo", "Carne", "Carne vegetal"]
    vegetales_posibles = ["Tomate", "Aceituna", "Champiñones"]
    masa_posible = ["Tradicional", "Delgada"]

    @staticmethod
    #validar elemento dentro de la lista
    def validar_elemento(elemento,valores_posibles):
        return elemento.title() in valores_posibles
    

    def crear_pizza(self:str):
        self.masa = None
        self.ing_proteico = None
        self.ing_vegetal1 = None
        self.ing_vegetal2 = None
        self.es_valida = None 
    

    def realizar_pedido(self):
        self.masa = input(f"Ingrese el tipo de masa que desea (Tradicional/Delgada): ".title())
        self.ing_proteico = input(f"Ingrese la proteina que desea (Pollo/Carne/Proteina Vegetal): ".title())
        self.ing_vegetal1 = input(f"Ingrese el primer vegetal que desea (Tomate/Aceitunas/Champiñones): ".title())
        self.ing_vegetal2 = input(f"Ingrese el segundo vegetal que desea (Tomate/Aceitunas/Champiñones): ".title())

#vaidar si ingredientes y tipo de masa son validos
    def es_valida(self):
        
        ingredientes_proteicos = ["Carne", "Pollo", "Carne vegetal"]
        ingredientes_vegetales = ["Aceitunas", "Champiñones", "Tomate"]
        masas = ["Tradicional", "Delgada"]

        proteico_valido = self.ing_proteico in ingredientes_proteicos
        vegetal1_valido = self.ing_vegetal1 in ingredientes_vegetales
        vegetal2_valido = self.ing_vegetal2 in ingredientes_vegetales
        masa_valida = self.masa in masas 
        print(proteico_valido, vegetal1_valido, vegetal2_valido, masa_valida)

        if proteico_valido and vegetal1_valido and vegetal2_valido and masa_valida:
            self.es_valida = True
            print("La pizza es válida")
        else:
            self.es_valida = False
            print("La pizza no es válida")
        
    

    def resumen_pizza(self):
        return f"Pizza {self.tamano} de masa {self.masa} con {self.ing_proteico}, {self.ing_vegetal1} y {self.ing_vegetal2}"
