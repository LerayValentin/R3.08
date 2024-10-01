def division(a: float=1, b:float=1):
    try:
        if isinstance(a, float) and isinstance(b, float):
            x = a / b
            return x
        else:
            raise TypeError("les valeurs fournies doivent être de type réel")
    except TypeError:
        raise TypeError("les valeurs fournies doivent être de type réel")
    except ValueError:
        raise ValueError("Erreur de valeur")
    except ZeroDivisionError:
        raise ZeroDivisionError("division par 0 impossible")
    except Exception:
        raise Exception("il y a eu une erreur")



def test():
    print(division(1.0, 2.0))

test()