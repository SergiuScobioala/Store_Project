print('Care este pretul produsului')
pretul = []
for i in range(5):
    pret = float(input('Introduceti pretul produsului: '))
    pretul.append(pret)

total = sum(pretul)
print(f'Pretul Toatal al produselor este: {total}')



