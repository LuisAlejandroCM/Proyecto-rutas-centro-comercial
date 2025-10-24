from SegundaEntrega import AVL

def mostrar_menu():
    print("\n" + "=" * 60)
    print("     GESTIÓN DE LUGARES DEL CENTRO COMERCIAL")
    print("=" * 60)
    print("1. Agregar nuevo lugar")
    print("2. Buscar un lugar por nombre")
    print("3. Mostrar todos los lugares (inorden)")
    print("4. Mostrar cantidad total de lugares")
    print("5. Eliminar un lugar por nombre")
    print("6. Filtrar lugares (tipo / piso / ambos)")
    print("7. Salir")
    print("=" * 60)


def seleccionar_tipo():
    print("\nSeleccione el tipo de lugar:")
    print("1. Tienda")
    print("2. Restaurante")
    print("3. Pasillo")
    print("4. Escaleras")
    print("5. Ascensor")

    while True:
        opcion = input("Opción (1-5): ").strip()
        tipos = {
            "1": "Tienda",
            "2": "Restaurante",
            "3": "Pasillo",
            "4": "Escaleras",
            "5": "Ascensor"
        }
        if opcion in tipos:
            return tipos[opcion]
        print("  Opción no válida. Intente nuevamente.")


def menu():
    arbol = AVL()

    #========================================================
    #Lugares pre creados
    arbol.AgregarElemento("D1", 2, "Tienda")
    arbol.AgregarElemento("Pasillo_P2", 2, "Pasillo")
    arbol.AgregarElemento("Escalera_Norte", 1, "Escalera")
    arbol.AgregarElemento("Nike", 1, "Tienda")
    arbol.AgregarElemento("Addidas", 1, "Tienda")
    arbol.AgregarElemento("Ascensor_Central", 3, "Ascensor")
    #========================================================


    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-7): ").strip()


        # 1. Agregar nuevo lugar
        if opcion == "1":
            print("\n--- Agregar nuevo lugar ---")
            nombre = input("Nombre del lugar: ").strip()
            piso = input("Número de piso: ").strip()

            if not nombre or not piso:
                print("  Todos los campos son obligatorios.")
                continue

            try:
                piso = int(piso)
            except ValueError:
                print("  El piso debe ser un número entero.")
                continue

            tipo = seleccionar_tipo()
            arbol.AgregarElemento(nombre, piso, tipo)
            print(f" Lugar '{nombre}' ({tipo}) agregado correctamente en el piso {piso}.")



        # 2. Buscar lugar por nombre
        elif opcion == "2":
            print("\n--- Buscar lugar ---")
            nombre = input("Ingrese el nombre del lugar a buscar: ").strip()
            if not nombre:
                print("  Debe ingresar un nombre.")
                continue

            resultado = arbol.buscar(nombre)
            if resultado:
                print(f" Lugar encontrado:")
                print(f"   Nombre: {resultado['nombre']}")
                print(f"   Piso: {resultado['piso']}")
                print(f"   Tipo: {resultado['tipo']}")
            else:
                print(f"No se encontró el lugar '{nombre}'.")



        # 3. Mostrar todos los lugares (inorden)
        elif opcion == "3":
            print("\n--- Lugares ordenados por nombre ---")
            lista = arbol.inorder()
            if not lista:
                print("El árbol está vacío.")
            else:
                for lugar in lista:
                    print(f"   - {lugar['nombre']} (Piso {lugar['piso']}, {lugar['tipo']})")


        # 4. Mostrar cantidad total de lugares
        elif opcion == "4":
            total = arbol.cantidad_elementos()
            print(f"\nTotal de lugares registrados: {total}")


        # 5. Eliminar lugar
        elif opcion == "5":
            print("\n--- Eliminar lugar ---")
            nombre = input("Ingrese el nombre del lugar a eliminar: ").strip()
            if not nombre:
                print("  Debe ingresar un nombre.")
                continue

            if arbol.buscar(nombre):
                arbol.EliminarElemento(nombre)
                print(f" Lugar '{nombre}' eliminado correctamente.")
            else:
                print(f" No se encontró el lugar '{nombre}' para eliminar.")

        # 6. Filtrar lugares(tipo / piso / ambos)
        elif opcion == "6":
            print("\n--- FILTRO DE LUGARES ---")
            print("Seleccione el tipo de filtro:")
            print("1. Por tipo")
            print("2. Por piso")
            print("3. Por tipo y piso")

            filtro_opcion = input("Opción (1-3): ").strip()

            if filtro_opcion == "1":
                tipo = seleccionar_tipo()
                resultados = arbol.filtrar_por_tipo(tipo)
                if resultados:
                    print(f"\n Lugares del tipo '{tipo}':")
                    for d in resultados:
                        print(f"   - {d['nombre']} (Piso {d['piso']})")
                else:
                    print(f" No se encontraron lugares del tipo '{tipo}'.")

            elif filtro_opcion == "2":
                piso = input("Ingrese el número de piso: ").strip()
                try:
                    piso = int(piso)
                except ValueError:
                    print("  El piso debe ser un número entero.")
                    continue
                resultados = arbol.filtrar_por_piso(piso)
                if resultados:
                    print(f"\n Lugares del piso {piso}:")
                    for d in resultados:
                        print(f"   - {d['nombre']} ({d['tipo']})")
                else:
                    print(f" No se encontraron lugares en el piso {piso}.")

            elif filtro_opcion == "3":
                tipo = seleccionar_tipo()
                piso = input("Ingrese el número de piso: ").strip()
                try:
                    piso = int(piso)
                except ValueError:
                    print("  El piso debe ser un número entero.")
                    continue
                resultados = arbol.filtrar(tipo=tipo, piso=piso)
                if resultados:
                    print(f"\n Lugares del tipo '{tipo}' en el piso {piso}:")
                    for d in resultados:
                        print(f"   - {d['nombre']}")
                else:
                    print(f" No se encontraron lugares tipo '{tipo}' en el piso {piso}.")

            else:
                print("  Opción no válida. Intente nuevamente.")


        # 7. Salir

        elif opcion == "7":
            print("\n Saliendo del programa...")
            break

        else:
            print("  Opción no válida. Intente nuevamente.")

menu()
