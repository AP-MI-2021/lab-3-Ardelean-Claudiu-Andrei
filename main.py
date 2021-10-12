#Ardelean Andrei
def citire_date_problema():
    l = input("Dati lista cu elemente cu virgula ")
    l = [int(x) for x in l.split(",")]
    return l


def is_prime(x):
    '''
    Functia verifica daca numarul pe care il primim este prim.
    :param x: Numarul de verificat.
    :return: True daca numarul este prim ,false daca nu este prim.
    '''
    if x < 2:
        return False
    for i in range(2, x//2 + 1):
        if x % i == 0:
            return False
    return True


def test_is_prim():
    assert  is_prime(3) is True
    assert is_prime(2) is True
    assert is_prime(16) is False


def suma_numere(lista):
    '''
    Se calculeaza suma unor numere
    :param lista: lista de nr intregi pentru care calculam suma
    :return: suma numerelor din lista.
    '''
    s = 0
    for x in range(len(lista)):
        s = s + lista[x]
    return s


def get_longest_sum_is_prime(lista):
    """
    Determinarea celei mai lungi subsecvente cu proprietatea ca suma numerelor este număr prim
    :param lista: lista care este citita de la tastatura
    :return: secventa maxima cu propirtatea ca suma numerelor este numar prim
    """
    secventa_Max = []
    for i in range (len(lista)):
        for j in range (i,len(lista)):
            suma=suma_numere(lista[i:j+1])
            if is_prime(suma)==True and len(lista[i:j+1]) > len(secventa_Max):
                secventa_Max = lista[i:j+1]
    return secventa_Max


def test_get_longest_sum_is_prime():
    assert get_longest_sum_is_prime([1, 2, 3, 4, 5]) == [1, 2]
    assert get_longest_sum_is_prime([4,5,8,6,2,7,9,5]) == [4, 5, 8, 6, 2, 7, 9]
    assert get_longest_sum_is_prime([4, 5, 6, 7, 8, 9, 2, 5, 6]) == [4, 5, 6, 7, 8, 9, 2]
test_get_longest_sum_is_prime()


def numarul_de_cifre(numar):
    numar_cifre = 0
    while numar:
        numar_cifre = numar_cifre + 1
        numar = numar // 10
    return numar_cifre


def numarul_cifre_este_descrescator(lista):
    """
    Determina daca o lista are o secventa elemente ale caror numere au un numar de cifre descrescator
    :param lista: lista care este verifiata
    :return: True in cazul ca lista este ordonata desresctor si false in caz contrar
    """
    for i in range(len(lista)-1):
        if numarul_de_cifre(lista[i]) < numarul_de_cifre(lista[i+1]):
            return False
    return True


def test_numarul_cifre_este_descrescator():
    assert numarul_cifre_este_descrescator([1, 22, 3]) is False
    assert numarul_cifre_este_descrescator([3, 2, 44]) is False
    assert numarul_cifre_este_descrescator([55555, 4444, 333, 22, 0]) is True


def get_longest_digit_count_desc(lista):
    """
    Determina cea mai lunga secventa cu propietatea sa fie ordonata descrescator
    :param lista:Lista care trebuie verificata
    :return: Lista maxima determinata
    """
    lungDesc=[]
    for i in range(len(lista) + 1):
        for j in range(len(lista) + 1):
            if numarul_cifre_este_descrescator(lista[i:j+1]) and len(lungDesc) < len(lista[i:j+1]):
                lungDesc = lista[i:j+1]
    return lungDesc


def test_get_longest_digit_count_desc():
    assert get_longest_digit_count_desc([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert get_longest_digit_count_desc([44,5,8888,6666,2222,777,99,5]) == [8888, 6666, 2222, 777, 99, 5]
    assert get_longest_digit_count_desc([543, 44, 3, 123]) == [543, 44, 3]


def main():
    test_numarul_cifre_este_descrescator()
    test_get_longest_digit_count_desc()
    lista = []
    while True:
        print('1. Citirea listei.')
        print('2. Determinarea celei mai lungi subsecvente in care suma numerelor este numar prim.')
        print('3. Determinarea celei mai lungi subsecvente in care numărul de cifre este în ordine descrescătoare.')
        print('4. Iesire din program - exit.')
        optiune = input('Alege optiunea: ')
        if optiune == "1":
            lista = citire_date_problema()
            print("\n")
        elif optiune == "2":
            print(get_longest_sum_is_prime(lista))
            print("\n")
        elif optiune == "3":
            print(get_longest_digit_count_desc(lista))
            print("\n")
        elif optiune=="4":
            break
        else:
            print("Optiune invalida!")

main()