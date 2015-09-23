"Multiples of 3 and 5"

def sum_multiples(num, limit):
    sum = 0
    for i in xrange(num, limit, num):
        sum += i
    return sum

def sum(limit):
    return (sum_multiples(3, limit) +
            sum_multiples(5, limit) -
            sum_multiples(15, limit))

print sum(1000)