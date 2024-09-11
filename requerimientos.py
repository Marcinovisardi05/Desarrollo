# Definimos los ingredientes disponibles
ingredientes_vegetarianos = ["Pimiento", "Tofu"]
ingredientes_no_vegetarianos = ["Peperoni", "Jamón", "Salmón"]

# Preguntamos al usuario si quiere una pizza vegetariana o no
pizza_vegetariana = input("¿Quieres una pizza vegetariana? (Si/No): ")

# Mostramos el menú correspondiente según la respuesta del usuario
if pizza_vegetariana.upper() == "Si":
    print("Ingredientes disponibles:")
    for i, ingrediente in enumerate(ingredientes_vegetarianos):
        print(f"{i+1}. {ingrediente}")
    ingrediente_elegido = int(input("Elige un ingrediente (1-2): ")) - 1
    ingrediente_seleccionado = ingredientes_vegetarianos[ingrediente_elegido]
    print(f"Has elegido una pizza vegetariana con {ingrediente_seleccionado}.")
    print("Ingredientes: Mozzarella, Tomate, ", ingrediente_seleccionado)
else:
    print("Ingredientes disponibles:")
    for i, ingrediente in enumerate(ingredientes_no_vegetarianos):
        print(f"{i+1}. {ingrediente}")
    ingrediente_elegido = int(input("Elige un ingrediente (1-3): ")) - 1
    ingrediente_seleccionado = ingredientes_no_vegetarianos[ingrediente_elegido]
    print(f"Has elegido una pizza no vegetariana con {ingrediente_seleccionado}.")
    print("Ingredientes: Mozzarella, Tomate, ", ingrediente_seleccionado)