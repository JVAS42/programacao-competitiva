import sys

def solve():
    data = sys.stdin.read().strip().split()
    if len(data) < 2:
        return  # não há dados suficientes

    try:
        a = int(data[0])
        n = int(data[1])
    except ValueError:
        return  # entradas inválidas

    # se quiser forçar n positivo, procuro no restante dos tokens um n>0
    if n <= 0:
        for token in data[2:]:
            try:
                nv = int(token)
                if nv > 0:
                    n = nv
                    break
            except ValueError:
                continue
        if n <= 0:
            return  # não encontrou n positivo

    # usar fórmula fechada (mais eficiente e sem loop)
    soma = n * (2*a + n - 1) // 2
    print(soma)

if __name__ == "__main__":
    solve()