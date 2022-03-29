#include "../include/Data.hpp"
#include <stdlib.h>

Data::Data(char* filePath)
{
    FILE* f = fopen(filePath, "r");

    if(!f)
    {
        printf("Problem while reading instance 1.\n");
        exit(1);
    }

    if(fscanf(f, "%d %d", &nb_industries, &nb_cities) != 2)
    {
        printf("Problem while reading instance.2\n");
        exit(1);
    }

    //costs
    costs = std::vector<std::vector<double> >(nb_industries, std::vector<double>(nb_cities));
    for(int i = 0; i < nb_industries; i++)
    {
        for(int j = 0; j < nb_cities; j++)
        {
            if(fscanf(f, "%lf", &costs[i][j]) != 1)
            {
                printf("Problem while reading instance.5\n");
                exit(1);
            }
        }
    }

    //capacities
    capacities = std::vector<double>(nb_industries);
    for(int i = 0; i < nb_industries; i++)
    {
        if(fscanf(f, "%lf", &capacities[i]) != 1)
        {
            printf("Problem while reading instance.3\n");
            exit(1);
        }
    }

    //demands
    demands = std::vector<double>(nb_cities);
    for(int i = 0; i < nb_cities; i++)
    {
        if(fscanf(f, "%lf", &demands[i]) != 1)
        {
            printf("Problem while reading instance.4\n");
            exit(1);
        }
    }

    fclose(f);
}

int Data::getNbIndustries()
{
    return nb_industries;
}

int Data::getNbCities()
{
    return nb_cities;
}

double Data::getCost(int industry, int city)
{
    return costs[industry][city];
}

double Data::getCapacity(int industry)
{
    return capacities[industry];
}

double Data::getDemand(int city)
{
    return demands[city];
}
