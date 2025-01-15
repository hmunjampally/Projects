"""
if __name__ == '__main__':
    x = 'anagram'
    y = 'garam'

    if sorted(x) == sorted(y):
        print(True) 
    print(False)

"""
x = 3.0
series_time = x**2.0
print(series_time)

y = 2.0
p = 4.0
numerator = (y**2.0/p)
parallel_time = numerator + p**2.0 + 3
print(parallel_time)


speed_up = series_time/parallel_time
efficiency = speed_up/p
print(speed_up)
print(efficiency)