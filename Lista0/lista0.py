A = [1, 2, 3, 4, 5]
B = [3, 4, 5, 6, 7, 8]

# print('I')
# for i in A:
#     print(f"x_{i} <= 50")

# print('II')
# for i in A:
#     if i > 3:
#         print(f"x_{i} <= 50")

# print('III')
# soma = ""
# for i in A:
#     soma += f"+ x_{i}"
# print(f"{soma} >= 2")

# print('IV')
# soma = ""
# for i in A:
#     if i<= 4:
#         soma += f"+ x_{i}"
# print(f"{soma} = 5")

# print('V')
# rest = ""
# for j in B:
#     rest = f"y_{j} <= "
#     soma_x = ""
#     for i in A:
#         soma_x += f"+ x_{i}"
#     rest += soma_x
#     print(rest)

# print('VI')
# restri = ""
# for j in B:
#     if j < 3:
#         restri = f"y_{j} = "
#         soma = ""
#         for i in A:
#             if i < 2:
#                 soma += f"+ x_{i}"
#         restri += soma
#         print(restri)

# print('VII')
# for i in A:
#     for j in B:
#         if i < j:
#             print(f'z_{i}{j} >= 20')

# print('VIII')
# for i in A:
#     soma = ""
#     for j in B:
#         soma += f"+ z_{i}{j}"
# print(f"{soma} = 100")

# print('IX')
# soma = ""
# for j in B:
#     for i in A:
#         if i > 5:
#             soma += f"+ z_{i}{j}"
# print(f"{soma} <= 12")

# print('X')
# for i in A:
#     if i != 2:
#         soma_z = ""
#         for j in B:
#             if j > i:
#                 soma_z += f"+ z_{i}{j}"
#         print(f'{soma_z} = y_{i}')

# print('XI')
# soma = ""
# for i in A:
#     result = ""
#     for j in B:
#         result += f"+ y_{j}"
#         if j > i:
#             soma += f"+ z_{i}{j}"
# print(f"{soma} >= {result}")

'''
2. I
x_5 <= 40
x_6 <= 40
x_7 <= 40

2. II

'''

A = [1, 2, 3, 4, 5, 6, 7]
for i in A:
    if i>4:
        print("x_" + str(i) + " " + "<= " + "40")