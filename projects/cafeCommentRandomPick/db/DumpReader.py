def main():
    dumpNum = None
    while dumpNum is not 'q':
        dumpNum = input()

        f = open("../dump%s.txt"%dumpNum, 'r')
        for line in f.readlines():
            for t in line.split("$"):
                if t.split(":")[0] == 'comment':
                    print("")
                    print(t.split(':')[1])
        f.close()

if __name__ == "__main__":
    main()
