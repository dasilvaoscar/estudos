from Var import MyClass


class Condicional:

    MyClass.a = 1

    a = MyClass.a
    b = MyClass.b
    c = MyClass.c
    if a == 1:
        print("O valor é igual a %d" % a)
    elif a < 1:
        print('A é maior de 1')
    else:
        print('A é menor que 1')