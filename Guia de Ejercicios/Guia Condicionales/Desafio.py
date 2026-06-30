# Constantes
CARGO_FIJO = 7000
COSTO_M3 = 200
IVA = 0.21

# Ingreso de datos
consumo = float(input("Ingrese los m³ consumidos: "))
tipo_cliente = input("Ingrese el tipo de cliente (Residencial, Comercial o Industrial): ").capitalize()

# Cálculo del consumo
costo_consumo = consumo * COSTO_M3

# Factura sin descuentos ni recargos
subtotal_base = CARGO_FIJO + costo_consumo

# Variables para bonificaciones y recargos
bonificacion = 0
recargo = 0
descuento_adicional = 0

# Evaluación según tipo de cliente
match tipo_cliente:

    case "Residencial":
        if consumo < 30:
            bonificacion = costo_consumo * 0.10
        elif consumo > 80:
            recargo = costo_consumo * 0.15

        # Caso especial
        if subtotal_base < 35000:
            descuento_adicional = subtotal_base * 0.05

    case "Comercial":
        if consumo > 300:
            bonificacion = costo_consumo * 0.12
        elif consumo > 150:
            bonificacion = costo_consumo * 0.08
        elif consumo < 50:
            recargo = costo_consumo * 0.05

    case "Industrial":
        if consumo > 1000:
            bonificacion = costo_consumo * 0.30
        elif consumo > 500:
            bonificacion = costo_consumo * 0.20
        elif consumo < 200:
            recargo = costo_consumo * 0.10

    case _:
        print("Tipo de cliente inválido.")
        exit()

# Subtotal con bonificaciones y recargos
subtotal = subtotal_base - bonificacion + recargo - descuento_adicional

# IVA
iva_calculado = subtotal * IVA

# Total final
total_pagar = subtotal + iva_calculado

# Mostrar resultados
print("\n===== FACTURA DE AGUA POTABLE =====")
print(f"Tipo de cliente: {tipo_cliente}")
print(f"Consumo: {consumo} m³")

print(f"\nCargo fijo: ${CARGO_FIJO:,.2f}")
print(f"Costo por consumo: ${costo_consumo:,.2f}")

print(f"\nBonificación: -${bonificacion:,.2f}")
print(f"Recargo: +${recargo:,.2f}")
print(f"Descuento adicional: -${descuento_adicional:,.2f}")

print(f"\nSubtotal: ${subtotal:,.2f}")
print(f"IVA (21%): ${iva_calculado:,.2f}")

print(f"\nTOTAL A PAGAR: ${total_pagar:,.2f}")