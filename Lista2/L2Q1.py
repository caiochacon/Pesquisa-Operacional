from mip import *

def CreateModel():
    names = ['F1D1', # 0
             'F1CD', # 1
             'CDD1', # 2
             'F2CD', # 3
             'F2D2', # 4
             'CDD2'] # 5
    costs = [7, 3, 2, 4, 9, 4]

    model = Model(sense='MINIMIZE', solver_name='CBC', name='Fluxo de transporte')

    x = [model.add_var(var_type='CONTINUOUS', lb=0.0, name='x_' + str(i))
        for i in names]

    model.objective = xsum(costs[i] * x[i] for i in range(len(names)))

    # Restrições, s.t, s.a:
    model += x[0] >= 0
    model += x[1] >= 0
    model += x[1] <= 50
    model += x[2] >= 0
    model += x[2] <= 50
    model += x[3] >= 0
    model += x[3] <= 50
    model += x[4] >= 0
    model += x[5] >= 0
    model += x[5] <= 50

    model += 0 - (x[0] + x[1]) == -80
    model += 0 - (x[3] + x[4]) == -70
    model += (x[0] + x[2]) == 60
    model += (x[4] + x[5]) == 90
    model += (x[1] + x[3]) - (x[2] + x[5]) == 0
    
    return model


def main():

    model = CreateModel()

    status = model.optimize()

    print("Status = ", status)
    print("Solution value  = ", model.objective_value)

    model.write('L2Q1.lp')

    print("Solution:")
    for v in model.vars:
        if v.x > 0.00001:
            print(v.name, " = ", v.x)

main()

