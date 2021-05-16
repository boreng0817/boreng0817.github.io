count = 0

def main():
    dumpNum = "89 40".split()
    user = []
    comment = []
    dup = {}

    for num in dumpNum:
        f = open("dump%s.txt"%num, 'r')
        for line in f.readlines():
            _id = []
            tup = []
            for t in line.split("$"):
                temp = t.split(":")[0]
                if temp == 'id':
                    if t.split(":")[1] not in user:
                        user.append(t.split(":")[1])
                        tup.append(t.split(":")[1])
                if temp == 'nickName':
                    tup.append(t.split(":")[1])
                if temp == 'comment':
                    tup.append(t.split(":")[1])
            if len(tup) == 3:
                comment.append(tup)

        f.close()


    test = []
    wrong = []
    import emojis
    for i in range(len(comment)):
        containedEmojis = emojis.get(comment[i][2])
        if len(containedEmojis) == 1:
            test.append([comment[i][1], comment[i][2]])
        else:
            wrong.append([comment[i][1], comment[i][2]])

    test.append(['겸멍', '잠와도 / 검정색 ♟'])
    test.append(['쌍배', '크라운산도/검은색🕶'])

    import random
    result = random.sample(test, len(test))

    string = """
    
    날이 좋아서 마일 나눔 𝟎𝟕 추첨 결과

    _

     1. %s
     2. %s

    _


    """%(result[0][0], result[1][0])

    print(string)

if __name__ == "__main__":
    main()
