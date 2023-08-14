def read_testdata(testfile):
    n = 0
    arr = []
    with open(testfile, 'r') as f:
        n = int(f.readline())
        for i in range(1, n+1):
            arr.append(int(f.readline()))
    return n, arr