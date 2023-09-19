# new dozen = lambda n:n+12

def myfunc(x):
    return lambda n : n + x

# new_century = myfunc(100)

# print(new_century(100))

l = [['red', 'truck'], ['blue', 'truck'], ['red', 'sedan']]

# print(sorted(l, key=lambda v:v[1], reverse=True))


def myfunc2(x):
    return lambda a, b : (a + b) * x


sum_times_two = myfunc2(2)

print(sum_times_two(10,20))