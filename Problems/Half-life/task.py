n_atoms = abs(int(input()))
r_quantity = abs(int(input()))
t_days = 0

while n_atoms > r_quantity:
    n_atoms = n_atoms // 2
    t_days += 1
print(t_days * 12)
