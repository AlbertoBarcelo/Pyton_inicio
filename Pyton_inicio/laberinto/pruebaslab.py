# val = 1
# (l, c) = (5, 5)
# muros = ([0][2],[1][2],[1][3],[1][4],[2][4])
# lab = [[val] * c] * l
# for l in range(5):
#     for c in range(5):
#         if not [l][c] == muros:
#             lab[l][c] = 0
#         else:
#             lab[l][c] = 1
# print(lab) 

laberinto = [
    ['e', '1', '1', '1', '1'],
    ['0', '0', '0', '1', '1'],
    ['0', '0', '0', '0', '1'],
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '1', 's'],
]
print(laberinto)