from cmath import phase


if __name__ == '__main__':
    z = input()  # complex number

    print(round(phase(complex(z)), 3))
    print(round(abs(complex(z)), 3))