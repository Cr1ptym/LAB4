from matplotlib import pyplot as plt

def func(x):
    """
    Calculate function values for passed array of arguments
    """
    return [t/(t**2 + 1) for t in x]

def tabulate(a, b, n):
    x = [a + x*(b - a)/n for x in range(n)]
    y = func(x)
    return {'x': x, 'y': y}

def main():
    res = tabulate(0, 1, 1000)

    plt.plot(res['x'], res['y'])
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()
