\Problem name: Transportation Network Flow

Minimize
OBJROW: 7 x_F1_D1 + 3 x_F1_CD + 9 x_F2_D2 + 4 x_F2_CD + 2 x_CD_D1 + 4 x_CD_D2
Subject To
F1:  - x_F1_D1 - x_F1_CD = -80
F2:  - x_F2_D2 - x_F2_CD = -70
CD:  x_F1_CD + x_F2_CD - x_CD_D1 - x_CD_D2 = -0
D1:  x_F1_D1 + x_CD_D1 = 60
D2:  x_F2_D2 + x_CD_D2 = 90
constr(5):  x_F1_D1 >= -0
constr(6):  x_F1_CD >= -0
constr(7):  x_F1_CD <= 50
constr(8):  x_F2_D2 >= -0
constr(9):  x_F2_CD >= -0
constr(10):  x_F2_CD <= 50
constr(11):  x_CD_D1 >= -0
constr(12):  x_CD_D1 <= 50
constr(13):  x_CD_D2 >= -0
constr(14):  x_CD_D2 <= 50
Bounds
End
