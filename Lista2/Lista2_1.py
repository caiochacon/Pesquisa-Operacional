from mip import *


def createModel():
    names = ['F1_D1',  # 0
             'F1_CD',  # 1
             'F2_D2',  # 2
             'F2_CD',  # 3
             'CD_D1',  # 4
             'CD_D2']  # 5
    costs = [7, 3, 9, 4, 2, 4]

    model = Model(sense=MINIMIZE, solver_name=CBC, name='Transportation Network Flow')

    x = [model.add_var(var_type=CONTINUOUS, lb=0.0, name='x_' + str(i)) for i in names]

    model.objective = xsum(costs[i] * x[i] for i in range(len(names)))

    model += - x[0] - x[1] == -80, 'F1'
    model += - x[2] - x[3] == -70, 'F2'
    model += (x[1] + x[3]) - (x[4] + x[5]) == 0, 'CD'
    model += x[0] + x[4] == 60, 'D1'
    model += x[2] + x[5] == 90, 'D2'

    model += x[0] >= 0

    model += x[1] >= 0
    model += x[1] <= 50

    model += x[2] >= 0

    model += x[3] >= 0
    model += x[3] <= 50

    model += x[4] >= 0
    model += x[4] <= 50

    model += x[5] >= 0
    model += x[5] <= 50

    return model

def main():
    model = createModel()
    status = model.optimize()

    print("Status = ", status)
    print("Solution value  = ", model.objective_value)

    model.write("Lista2_1.lp")

    print("Solution:")

    for v in model.vars:
        if v.x > 0.00001:
            print(v.name, " = ", v.x)

if __name__ == '__main__':
    main()

