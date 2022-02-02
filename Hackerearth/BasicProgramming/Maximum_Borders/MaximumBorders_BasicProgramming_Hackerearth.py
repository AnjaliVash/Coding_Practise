testcases=int(input())
for _ in range(testcases):
    lines, length=(int(i) for i in (input().split(" ")))
    maxhash=0
    for _ in range(lines):
        string= input()
        maxhash=max(maxhash,string.count("#"))
    print(maxhash)