def standaardprijs(afstandKM):
    if afstandKM < 0:
        return afstandKM * 0
    if afstandKM > 50:
        return 15 + (afstandKM * 0.60)
    if afstandKM <=50:
        return afstandKM * 0.80

def ritprijs(leeftijd, weekendrit, afstandKM):
    if weekendrit:
        if leeftijd < 12 or leeftijd >= 65:
            return standaardprijs(afstandKM) * 0.65
        else:
            return standaardprijs(afstandKM) * 0.60

    else:
        if leeftijd < 12 or leeftijd >= 65:
            return standaardprijs(afstandKM) * 0.7
        else:
            return (standaardprijs(afstandKM))


weekendrit=True

print(ritprijs(11, False, 0))
print(ritprijs(11, True, -15))
print(ritprijs(11, True, 15))
print(ritprijs(11, False, 15))
print(ritprijs(11, True, 75))
print(ritprijs(11, False, 75))
print(ritprijs(12, True, 15))
print(ritprijs(12, False, 15))
print(ritprijs(12, True, 75))
print(ritprijs(12, False, 75))
print(ritprijs(64, True, 15))
print(ritprijs(64, False, 15))
print(ritprijs(64, True, 75))
print(ritprijs(64, False, 75))
print(ritprijs(65, True, 15))
print(ritprijs(65, False, 15))
print(ritprijs(65, False, 75))
print(ritprijs(65, False, 75))
