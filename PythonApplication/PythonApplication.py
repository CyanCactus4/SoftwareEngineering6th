#Метод, доказывающий великую теорему Ферма.
def ferm_theorem(a, b, c, n):
    return a**n + b**n != c**n

a = 3
b = 4
c = 5
print(f"Верна ли теорема Ферма при a = {a}, b = {b}, c = {c} для ")
for n in range(3, 13):
    print(f"n = {n}: {ferm_theorem(a, b, c, n)}")

# Верна ли теорема Ферма при a = 3, b = 4, c = 5 для
# n = 3: True
# n = 4: True
# n = 5: True
# n = 6: True
# n = 7: True
# n = 8: True
# n = 9: True
# n = 10: True
# n = 11: True
# n = 12: True