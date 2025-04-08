# set significa grupo o conjunto
primer = {1, 1, 1, 2, 2, 3, 4}
print(primer)  # imprime y elimina los duplicados

segundo = [3, 5, 6, 7]
segundo = set(segundo)  # convertimos lista a set

print(primer | segundo)  # union de sets
print(primer & segundo)  # intercesion
print(primer - segundo)  # Diferencia
print(primer ^ segundo)  # diferencia simetrica
