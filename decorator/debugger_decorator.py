import functools
import pdb

def debugger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        pdb.set_trace()
        return func(*args, **kwargs)
    return wrapper

if __name__ == '__main__':
    @debugger
    def minha_funcao(x, y):
        resultado = x + y
        return resultado

    resultado = minha_funcao(3, 5)
    print("Resultado:", resultado)
