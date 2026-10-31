
def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                name, salary = line.strip().split(",")
                total += int(salary)
                count += 1

        if count == 0:
            return (0, 0)

        average = total / count

        return (total, average)

    except (FileNotFoundError, ValueError):
        return ('File not found or invalid data format.', 0)

total, average = total_salary("salary_file.txt")

print(f"Загальна сума: {total}")
print(f"Середня зарплата: {average}")