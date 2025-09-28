# Task 10 Oshovska
def average():
    count = 0
    total = 0.0

    def add_and_average(x):
        nonlocal count, total
        count += 1
        total += x
        return total/count
    return add_and_average

avg = average()
print(avg(15))
print(avg(25))
print(avg(30))