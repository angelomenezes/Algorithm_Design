if __name__ == "__main__":
    try:
        while True:
            binary = str(input())
            while binary[-1] != '#':
                binary += str(input())            
            decimal = int(binary[:-1], 2)
            if decimal % 131071 == 0:
                print('YES')
            else:
                print('NO')
    except:
        pass