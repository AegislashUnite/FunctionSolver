import math

mode = int(input("Eliga el modo: \n1 - Cuadratica\n2 - Estandar\n"))

if mode == 1:

    a = int(input("Ingrese el valor de a:"))
    b = int(input("Ingrese el valor de b:"))
    c = int(input("Ingrese el valor de c:"))

    print("El punto de corte en el eje Y es en",c,)

    if a > 0:
        print("La función abre hacia arriba.")
    elif a < 0:
        print("La función abre hacia abajo.")

    d = (b * -1) + ((b ** 2) - (4 * a * c)) ** 0.5
    e = (b * -1) - ((b ** 2) - (4 * a * c)) ** 0.5
    f = 2 * a

    n = d / f
    m = e / f

    print("Los puntos de corte en el eje X son en",n,"y en",m,)

    v = (b * -1) / f
    w = (a * (v ** 2)) + (b * v) + c

    print("Las coordenadas del vertice son:",v,w,)

    if a > 0:
        print("Decreciente: (-∞,",v,")")
        print("Creciente: (",v,",∞)")
    elif a < 0:
        print("Creciente: (-∞,",v,")")
        print("Decreciente: (",v,",∞)")

    g = (w * -1) / ((n - v) ** 2)

    if v < 0 and w > 0:
        print("Forma Estandar:",g,"(x +",v * -1,")^2 +",w,)
    elif v > 0 and w < 0:
        print("Forma Estandar:",g,"(x -",v,")^2 -",w * -1,)
    elif v < 0 and w < 0:
        print("Forma Estandar:",g,"(x +",v * -1,")^2 -",w * -1,)
    elif v > 0 and w > 0:
        print("Forma Estandar:",g,"(x -",v,")^2 +",w,)

elif mode == 2:
    a = int(input("Ingrese el eje X del vertice:"))
    b = int(input("Ingrese el eje Y del vertice:"))
    c = int(input("Ingrese uno de los cortes con el eje X:"))

    d = (b * -1) / ((c - a) ** 2)

    if a < 0 and b > 0:
        print("Forma Estandar:",d,"(x +",a * -1,")^2 +",b,)
    elif a > 0 and b < 0:
        print("Forma Estandar:",d,"(x -",a,")^2 -",b * -1,)
    elif a < 0 and b < 0:
        print("Forma Estandar:",d,"(x +",a * -1,")^2 -",b * -1,)
    elif a > 0 and b > 0:
        print("Forma Estandar:",d,"(x -",a,")^2 +",b,)

    e = 2 * d * a
    f = d * (a ** 2) + b

    if e < 0 and f > 0:
        print("Forma Cuadratica:",d,"x^2 - ",e * -1,"x + ",f,)
    elif e > 0 and f < 0:
        print("Forma Cuadratica:",d,"x^2 - ",e,"x + ",f * -1,)
    elif e < 0 and f < 0:
        print("Forma Cuadratica:",d,"x^2 - ",e * -1,"x + ",f * -1,)
    elif e > 0 and f > 0:
        print("Forma Cuadratica:",d,"x^2 - ",e,"x + ",f,)

    print("El punto de corte en el eje Y es en",f,)

    if d > 0:
        print("La función abre hacia arriba.")
    elif d < 0:
        print("La función abre hacia abajo.")

    if d > 0:
        print("Decreciente: (-∞,",a,")")
        print("Creciente: (",a,",∞)")
    elif d < 0:
        print("Creciente: (-∞,",a,")")
        print("Decreciente: (",a,",∞)")
