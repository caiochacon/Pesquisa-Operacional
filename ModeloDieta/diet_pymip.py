#!/usr/bin/python
from inspect import BoundArguments
import sys
from mip import *


def readInstance(filePath):
    f = open(filePath, "r")

    l = f.readline()
    nb_foods, nb_nutrients = int(l.split()[0]), int(l.split()[1])

    l = f.readline()
    costs = [float(c) for c in l.split()]

    l = f.readline()
    min_levels = [float(m) for m in l.split()]

    food_nutr_levels = []
    for i in range(nb_foods):
        l = f.readline()
        levels = [float(level) for level in l.split()]
        food_nutr_levels.append(levels)

    f.close()

    return nb_foods, nb_nutrients, costs, min_levels, food_nutr_levels


def createModel(nb_foods, nb_nutrients, costs, min_levels, food_nutr_levels):

    model = Model(sense=MINIMIZE, solver_name=CBC)

    x = [model.add_var(var_type="INTERGER", lb=0.0, name="x" + str(i))
         for i in range(nb_foods)]

    model.objective = xsum(costs[i]*x[i] for i in range(nb_foods))

    for j in range(nb_nutrients):
        model += xsum(food_nutr_levels[i][j]*x[i]
                      for i in range(nb_foods)) >= min_levels[j], "NUTRI_" + str(j)

    return model


def main():

    nb_foods, nb_nutrients, costs, min_levels, food_nutr_levels = readInstance('ModeloDieta\instance.txt')

    print('Passando pro modelo\n')

    model = createModel(nb_foods, nb_nutrients, costs,
                        min_levels, food_nutr_levels)

    print('Passando pra otimização\n')
    status = model.optimize()

    print("Status = ", status)
    print("Solution value  = ", model.objective_value)

    print("Solution:")
    for v in model.vars:
        if v.x > 0.00001:
            print(v.name, " = ", v.x)


if __name__ == "__main__":
    main()
