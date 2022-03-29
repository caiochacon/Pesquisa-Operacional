\Problem name: Fluxo de transporte

Minimize
OBJROW: 800 x_ARSP + 900 x_ARRE + 280 x_SPMA + 220 x_SPPA + 80 x_SPSA + 40 x_SAPA + 50 x_SAMA + 100 x_RESA + 170 x_REMA + 140 x_REPA
Subject To
constr(0):  x_ARSP <= 500
constr(1):  x_ARRE <= 500
constr(2):  x_SPMA <= 300
constr(3):  x_SPPA <= 400
constr(4):  x_SPSA <= 500
constr(5):  x_SAPA <= 400
constr(6):  x_SAMA <= 300
constr(7):  x_RESA <= 500
constr(8):  x_REMA <= 300
constr(9):  x_REPA <= 400
constr(10):  - x_ARSP - x_ARRE = -700
constr(11):  x_ARSP - x_SPMA - x_SPPA - x_SPSA = -0
constr(12):  x_ARRE - x_RESA - x_REMA - x_REPA = -0
constr(13):  x_SPSA - x_SAPA - x_SAMA + x_RESA = -0
constr(14):  x_SPPA + x_SAPA + x_REPA = 400
constr(15):  x_SPMA + x_SAMA + x_REMA = 300
Bounds
End
