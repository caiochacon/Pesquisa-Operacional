from mip import *

def CreateModel():
    names = ['ARSP', # 0
             'ARRE', # 1
             'SPMA', # 2
             'SPPA', # 3
             'SPSA', # 4
             'SAPA', # 5
             'SAMA', # 6
             'RESA', # 7
             'REMA', # 8
             'REPA'] # 9
    costs = [800, 900, 280, 220, 80, 40, 50, 100, 170, 140]

    model = Model(sense='MINIMIZE', solver_name='CBC', name='Fluxo de transporte')

    x = [model.add_var(var_type='CONTINUOUS', lb=0.0, name='x_' + str(i))
        for i in names]

    model.objective = xsum(costs[i] * x[i] for i in range(len(names)))

    # Restrições, s.t, s.a:
    model += x[0] <= 500
    model += x[1] <= 500
    model += x[2] <= 300
    model += x[3] <= 400
    model += x[4] <= 500
    model += x[5] <= 400
    model += x[6] <= 300
    model += x[7] <= 500
    model += x[8] <= 300
    model += x[9] <= 400

    model += 0 - (x[0] + x[1]) == -700
    model += x[0] - (x[4] + x[2] + x[3]) == 0
    model += x[1] - (x[8] + x[9] + x[7]) == 0
    model += (x[4] + x[7]) - (x[5] + x[6]) == 0
    model += (x[3] + x[5] + x[9]) == 400
    model += (x[2] + x[6] + x[8]) == 300
    
    return model


def main():

    model = CreateModel()

    status = model.optimize()

    print("Status = ", status)
    print("Solution value  = ", model.objective_value)

    model.write('L2Q2.lp')

    print("Solution:")
    for v in model.vars:
        if v.x > 0.00001:
            print(v.name, " = ", v.x)

main()

