import sys

n = int(sys.stdin.readline())
cnt = 0
gd = {}
for i in range(n):
    s = sys.stdin.readline().strip()
    if s == 'ENTER':
        gd = {}
    else:
        if gd.get(s) == 1:
            pass
        else:
            gd[s] = 1
            cnt += 1
sys.stdout.write(str(cnt)+'\n')

