print("Pizzeria Bella Napoli")
print()
print()
pizza = input("Qué tipo de pizza desea ordenar? (Vegetariana - No vegetariana): ")


if pizza.lower() == "vegetariana":
    print("Ingredientes vegetarianos: Pimiento y tofu.")
    ingrediente = input("Qué ingrediente desea agregar? (Solo 1): ")
    print("Confirmación de orden: Una pizza ",pizza," con ",ingrediente.lower(),", Mozarella y Tomate")
elif pizza.lower() == "no vegetariana":
    print("Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.")
    ingrediente = input("Qué ingrediente desea agregar? (Solo 1): ")
    print("Confirmación de orden: Una pizza ",pizza," con ",ingrediente.lower(),", Mozarella y Tomate")
