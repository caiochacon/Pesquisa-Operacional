#!/usr/bin/python
import sys
import cplex
from cplex.exceptions import CplexError

def readInstance(filePath):
    f = file(filePath, "r")

    l = f.readline()
    nb_industries, nb_cities = int(l.split()[0]), int(l.split()[1])
    
    costs = []
    for i in range(nb_industries):
        l = f.readline()
        costs.append([float(c) for c in l.split()])

    l = f.readline()
    capacities = [float(c) for c in l.split()]

    l = f.readline()
    demands = [float(d) for d in l.split()]

    f.close()

    return nb_industries, nb_cities, costs, capacities, demands

def createProblem(nb_industries, nb_cities, costs, capacities, demands):

    prob = cplex.Cplex()
    prob.objective.set_sense(prob.objective.sense.minimize)

    for i in range(nb_industries):
        for j in range(nb_cities):
            prob.variables.add(obj=[costs[i][j]], lb=[0], types="C", names=["x_" + str(i) + "_" + str(j)])

    for i in range(nb_industries):
        names, coeffs = [], []
        for j in range(nb_cities):
            names.append("x_" + str(i) + "_" + str(j))
            coeffs.append(1)
        prob.linear_constraints.add(lin_expr=[[names, coeffs]], senses="L", rhs=[capacities[i]], names=["CAP_" + str(i)])

    for i in range(nb_cities):
        names, coeffs = [], []
        for j in range(nb_industries):
            names.append("x_" + str(j) + "_" + str(i))
            coeffs.append(1)
        prob.linear_constraints.add(lin_expr=[[names, coeffs]], senses="G", rhs=[demands[i]], names=["DEM_" + str(i)])

    return prob

def main():

    try:
        nb_industries, nb_cities, costs, capacities, demands = readInstance(sys.argv[1])
        prob = createProblem(nb_industries, nb_cities, costs, capacities, demands)
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
    for i in range(nb_industries):
        for j in range(nb_cities):
            value = prob.solution.get_values("x_" + str(i) + "_" + str(j))
            if value > 0.00001:
                print "From industry ", i, " to city ", j, ":", value
        
if __name__ == "__main__":
   main()
