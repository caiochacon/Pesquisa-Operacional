#ifndef _DATA_H_
#define _DATA_H_

#include <vector>
#include <stdio.h>

class Data
{
   private:

      int nb_industries;
      int nb_cities;
      std::vector<std::vector<double>> costs;
      std::vector<double> demands;
      std::vector<double> capacities;

   public:

      Data(char* filePath);

      int getNbIndustries();

      int getNbCities();

      double getCost(int industry, int city);

      double getCapacity(int industry);

      double getDemand(int city);
};

#endif

