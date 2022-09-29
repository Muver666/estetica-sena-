print ("Bienvenido a la tienda en linea de Ecipar")
print ("Para ver el catalogo de productos digita 1")
print ("Para ver el catalogo de servicios digita 2")
print ("Si ya conoces los servicios y deseas agendar o cancelar una cita, dighita 3")
op = int(input("A que servicio deseas acceder?"))
if op == 1:
    print ("Para consultar un tipo especifico de producto debes digitar un numero en el buscador en base al tipo de producto que desees")
    print ("Digita 1 para productos faciales: cremas, mascarillas, maquillage, ETC.")
    print ("Digita 2 para productos de aplicacion general: jabon, perfumes, cremas, ETC.")
    print ("Digita 3 para productos de ducha: champoo, jabon de baño, locion de baño, ETC.")
    productos = int(input("Buscador"))
    if productos == 1:
        print ("Los productos disponibles son: polvos de maquillage, cremas para arrugas, mascarillas y agua micelar")
    elif productos == 2:
        print ("Los productos disponibles son: bloqueador solar, perfumes, cremas para el cuidado de la piel y bronceador")
    elif productos == 3:
        print ("Los productos disponibles son: jabon de baño, lociones de baño, champoo y jabones intimos")
    else:
        print ("El tipo de producto buscado no coincide con nuestro catalogo, intentalo nuevamente")
elif op == 2:
    print ("En Ecipar chop ofrecemos distintos servicios de bellesa")
    print ("Si deseas un servicio de spa digita 1 para ver las distintas opciones")
    print ("Si deseas un servicio de manicura o pedicura digita 2")
    print ("Si deseas un corte de cabello o labado de tratamiento digita 3")
