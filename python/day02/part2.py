def is_safe(report: list[int]) -> bool:
    # true if the reports should be increasing, false if they should be decreasing
    increasing = (report[1] - report[0]) > 0
    for i in range(1, len(report)):
        prev = report[i - 1]
        curr = report[i]
        diff = curr - prev
        if diff < 0 and increasing:
            return False
        elif diff > 0 and not increasing:
            return False

        if abs(diff) > 3 or abs(diff) < 1:
            return False

    return True


num_safe_reports = 0

while True:
    try:
        line = input()
    except EOFError:
        break

    report = [int(n) for n in line.split()]

    any_safe = False
    for i in range(len(report)):
        updated_report = report.copy()
        updated_report.pop(i)
        if is_safe(updated_report):
            any_safe = True

    if any_safe:
        num_safe_reports += 1

    # if is_safe(report):
    #     num_safe_reports += 1


print(num_safe_reports)
