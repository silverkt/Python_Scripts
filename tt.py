def colll(times=1, s_str='') :
    if times != 0 :
        times = times - 1
        for s in full_str :
            x = s_str + s
            for i in colll(times, x):
                yield i
    else :
        yield s_str

full_str = 'abcdefghi'
a = colll(3)
for i in a:
    print(i)
