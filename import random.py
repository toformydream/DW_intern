def main():
    b=0
    for i in range(0,5):
        b = a(b)
        print(b)


def a(a):
    for i in range(0, 5):
        b = 0
        b = b + 3
    a = a + b
    return a

if __name__ == '__main__':
    main()

