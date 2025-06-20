def func():

        x = list(map(int, input().split()))


        min_index = x.index(min(x))
        max_index = x.index(max(x))

        start = min(min_index, max_index) + 1
        end = max(min_index, max_index)

        if start >= end:
           print(sum(i for i in x if i > 0), 1)
           return

        p = 1
        for i in range(start, end):
            p *= x[i]

        print(sum(i for i in x if i > 0), p)

func()

