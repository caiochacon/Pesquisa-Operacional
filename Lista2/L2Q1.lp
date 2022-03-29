\Problem name: Fluxo de transporte

Minimize
OBJROW: 7 x_F1D1 + 3 x_F1CD + 2 x_CDD1 + 4 x_F2CD + 9 x_F2D2 + 4 x_CDD2
Subject To
constr(0):  x_F1D1 >= -0
constr(1):  x_F1CD >= -0
constr(2):  x_F1CD <= 50
constr(3):  x_CDD1 >= -0
constr(4):  x_CDD1 <= 50
constr(5):  x_F2CD >= -0
constr(6):  x_F2CD <= 50
constr(7):  x_F2D2 >= -0
constr(8):  x_CDD2 >= -0
constr(9):  x_CDD2 <= 50
constr(10):  - x_F1D1 - x_F1CD = -80
constr(11):  - x_F2CD - x_F2D2 = -70
constr(12):  x_F1D1 + x_CDD1 = 60
constr(13):  x_F2D2 + x_CDD2 = 90
constr(14):  x_F1CD - x_CDD1 + x_F2CD - x_CDD2 = -0
Bounds
End
