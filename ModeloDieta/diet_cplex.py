#!/usr/bin/python
import sys
import cplex
from cplex.exceptions import CplexError

def readInstance(filePath):
    f = file(filePath, "r")

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

def createProblem(nb_foods, nb_nutrients, costs, min_levels, food_nutr_levels):

    prob = cplex.Cplex()
    prob.objective.set_sense(prob.objective.sense.minimize)

    for i in range(nb_foods):
        prob.variables.add(obj=[costs[i]], lb=[0], ub=[10000], types="C", names=["x" + str(i)])

    for i in range(nb_nutrients):
        names, coeffs = [], []
        for j in range(nb_foods):
            names.append("x" + str(j))
            coeffs.append(food_nutr_levels[j][i])
        prob.linear_constraints.add(lin_expr=[[names, coeffs]], senses="G", rhs=[min_levels[i]], names=["NUTRI_" + str(i)])

    return prob

def main():

    try:
        nb_foods, nb_nutrients, costs, min_levels, food_nutr_levels = readInstance(sys.argv[1])
        prob = createProblem(nb_foods, nb_nutrients, costs, min_levels, food_nutr_levels)
        prob.write("model.lp")
        prob.solve()
    except CplexError as exc:
        print(exc)
        return

    # solution.get_status() returns an integer code
    print "Solution status = ", prob.solution.get_status(), ":",
    # the following line prints the corresponding string
    print prob.solution.status[prob.solution.get_status()]
    print "Solution value  = ", prob.solution.get_objective_value()

    print "Solution:"
    for i in range(nb_foods):
        value = prob.solution.get_values("x" + str(i))
        if value > 0.00001:
            print "Food ", i, ":", value
        
if __name__ == "__main__":
   main()
