def calc_mass(val):
    val = calc_mass_ez(val)
    if val < 0:
        return 0
    else:
        return val + calc_mass(val)

def calc_mass_ez(val):
  return int(int(val) / 3) - 2

sum* = 0
sum** = 0
for line in open("1.txt", 'rb'):
    sum* += calc_mass_ez(int(line))
    sum** += calc_mass(int(line))
print (sum*, sum**)
