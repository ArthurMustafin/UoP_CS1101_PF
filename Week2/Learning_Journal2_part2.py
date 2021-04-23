
baseline_US = 78
r1 = int(input("How much in hours do you physically train every day? "))
r2 = int(input("How much in hours do you sleep on average every day? "))
r3 = int(input("What's is you average sugar level in the morning in mmol/L? "))


def physical_health(r1):
    if r1 >= 1:
        return baseline_US * 0.1
    else:
        return baseline_US * (-0.05)


def sleep_health(r2):
    if r2 >= 8:
        return baseline_US * 0.1
    else:
        return baseline_US * (-0.08)


def sugar_health(r3):
    if r3 < 6:
        return baseline_US * 0.1
    else:
        return baseline_US * (-0.07)

#def life_expectancy():
def life_expectancy():
    return baseline_US + (physical_health(r1) + sleep_health(r2) + sugar_health(r3))


print("Probably you will live", "%.2f" % life_expectancy(), "years")
#print("Probably you will live", "%.2f" % life_expectancy(1, 8, 5), "years")
