#include "../include/Data.hpp"
#include <stdio.h>
#include <iostream>
#include <ilcplex/ilocplex.h>

void solve(Data& data);

int main(int argc, char** argv)
{
    if(argc != 2)
    {
        printf("Usage:\n./transport instance\n");
        return 0;
    }

    Data data(argv[1]);
    solve(data);

    return 0;
}

void solve(Data& data)
{
    IloEnv env;
    IloModel modelo(env);

    IloArray<IloNumVarArray> x(env, data.getNbIndustries());
    for(int i = 0; i < data.getNbIndustries(); i++)
    {
        IloNumVarArray x_i(env, data.getNbCities(), 0, IloInfinity);
        x[i] = x_i;
    }
    //adiciona a variavel x ao modelo
    for(int i = 0; i < data.getNbIndustries(); i++)
    {
        for(int j = 0; j < data.getNbCities(); j++)
        {
            char name[100];
            sprintf(name, "X(%d,%d)", i, j);
            x[i][j].setName(name);
            modelo.add(x[i][j]);
        }
    }

    ////////////////////////////////////////////////////////
    //Criando a Função Objetivo (FO) 
    IloExpr obj(env);
    for(int i = 0; i < data.getNbIndustries(); i++)
    {
        for(int j = 0; j < data.getNbCities(); j++)
        {
            obj += data.getCost(i,j)*x[i][j];
        }
    }
    // Adicionando a FO
    modelo.add(IloMinimize(env, obj));
    //////////////////////////////////////////////////////////

    ////////////////////////////////////////////////////////
    //Restricoes

    //demanda
    for(int i = 0; i < data.getNbCities(); i++) 
    {
        IloExpr sumX(env);
        for(int j = 0; j < data.getNbIndustries(); j++)
        {
            sumX += x[j][i];
        }

        IloRange r = (sumX >= data.getDemand(i));
        char name[100];
        sprintf(name, "DEMAND(%d)", i);
        r.setName(name);
        modelo.add(r);
    }

    //capacity
    for(int i = 0; i < data.getNbIndustries(); i++) 
    {
        IloExpr sumX(env);
        for(int j = 0; j < data.getNbCities(); j++)
        {
            sumX += x[i][j];
        }

        IloRange r = (sumX <= data.getCapacity(i));
        char name[100];
        sprintf(name, "CAPACITY(%d)", i);
        r.setName(name);
        modelo.add(r);
    }

    //fim das restricoes
    ////////////////////////////////////////////////////////

    //resolve o modelo
    IloCplex transport(modelo);
    transport.setParam(IloCplex::TiLim, 2*60*60);
    transport.setParam(IloCplex::Threads, 1);
    transport.exportModel("modelo.lp");

    try
    {
        transport.solve();
    }
    catch(IloException& e)
    {
        std::cout << e;
    }

    std::cout << "status:" << transport.getStatus() << std::endl;
    std::cout << "transportation cost:" << transport.getObjValue() << std::endl;
    for(int i = 0; i < data.getNbIndustries(); i++) 
    {
        for(int j = 0; j < data.getNbCities(); j++)
        {
            double value = transport.getValue(x[i][j]);
            if(value > 0.00001)
            {
                std::cout << "from industry " << i << " to city " << j << ":" << value << std::endl;
            }
        }
    }
}
