import numpy as np

with open('input.txt','r') as inp:
    with open('output.txt','w') as out:
        start = int(inp.readline())
        end = int(inp.readline())
        day = int(inp.readline())

        linespace = np.linspace(start, end, day)
        for i in range(1, len(linespace)+1):
            if i % 7 == 1:
                linespace[i-1] /= 3
            elif i % 7 == 5:
                linespace[i-1] *= 2
            print(f'{linespace[i-1]:.2f}', file=out)
        out.close()
    inp.close()