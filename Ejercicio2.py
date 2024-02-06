producto = "computador"
cantidad = 5
precio = 5000

descuento = 0.25
iva = 0.19
precio_descuento = precio-(precio * descuento)
total_con_descuento = precio_descuento * cantidad
total_con_iva = total_con_descuento + (total_con_descuento * iva)

total = total_con_descuento + total_con_iva