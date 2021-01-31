def print_hi():
    fib = lambda n: n if n < 2 else fib(n - 1) + fib(n - 2)
    # print("these\tare %r nan\tseparate\vlines\04130405" %("s"))
    # command = ""
    queque = []
    while True:
        command = int(input("enter: "))
        print("1. job1")
        print("2. job1")
        print("3. job1")
        print("4. job1")
        print("5. quit")

        if command == 1:
            queque.append(1)
        elif command == 2:
            try:
                queque.pop()
            except IndexError:
                print("empty list")
        elif command == 3:
            queque.append(3)
        elif command == 4:
            del queque[:]
        else:
            break
        print([1, 2, 3] == [1, 2, 3, 4])


if __name__ == '__main__':
    print_hi()
