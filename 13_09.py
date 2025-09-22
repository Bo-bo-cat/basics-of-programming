# Oshovska_task_10

speed = int(input("Enter start speed: "))
time = int(input("Enter time: "))
acceleration = int(input("Enter acceleration: "))

for second in range(1, time + 1):
    traveled_distance = speed * second + (acceleration * (second**2))/2
    print(f"{second} second - {traveled_distance} meters")

