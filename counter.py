import os

def increment_counter(counter_file="counter.txt"):
    # Создаём файл, если его нет
    if not os.path.exists(counter_file):
        with open(counter_file, "w") as f:
            f.write("0")

    # Считываем текущее значение
    with open(counter_file, "r") as f:
        count = int(f.read())

    # Увеличиваем и сохраняем
    count += 1
    with open(counter_file, "w") as f:
        f.write(str(count))

    return count
