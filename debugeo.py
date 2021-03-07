def multiDivide(listaNum):
    salida = []
    for i in listaNum:
        import pdb; pdb.set_trace()
        if (i != 0):
            valor = 100/i
            salida.append(valor)
    return salida


print(multiDivide([4,7,0,1,45]))