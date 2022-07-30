from fractions import Fraction


with500 = [Fraction(2)]
for i in range(1, 500):
    with500.append((1 + with500[-1] * Fraction(i, 500)) * Fraction(1000, 500 + i))

without500 = [(1 + with500[0] * Fraction(1, 1000)) * 2]
for i in range(1, len(with500)):
    without500.append((1 + without500[-1] * Fraction(i, 500) + with500[i] * Fraction(1, 1000)) * Fraction(1000, 500 + i))


print(without500[-1])
