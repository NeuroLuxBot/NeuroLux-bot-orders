import os

def increment_counter(counter_file="counter_orders.txt"):
    if not os.path.exists(counter_file):
        with open(counter_file, "w") as f:
            f.write("0")

    with open(counter_file, "r") as f:
        count = int(f.read())

    count += 1
    with open(counter_file, "w") as f:
        f.write(str(count))

    return count
