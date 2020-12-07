// day07 .cpp
//
// Advent of Code 2020
//

#include <iostream>
#include <fstream>
#include <string>


int main(int argc, char *argv[])
{
    std::string arr[1000];
    for(unsigned int i = 0; i < 1000; ++i)
        arr[i] = "";

    int count = 0;
    int arcount = 0;

    std::ifstream inFile("input.txt");
    if (!inFile)
    {
        std::cerr << "Unable to open file input.txt";
    }

    std::string x;
    while (std::getline(inFile, x))
    {
        int cont = x.find("contain");
        if (x.find("shiny gold bags",cont) != std::string::npos)
        {
            arr[arcount] = x.substr(0, cont - 2);
            ++arcount;
        }
    }
    
    inFile.close();
    
    for(int i = 0; i < arcount; ++i)
    {
        inFile.open("input.txt");
        if (!inFile)
        {
            std::cerr << "Unable to open file input.txt";
        }
        
        std::string x;
        while (std::getline(inFile, x))
        {
            int cont = x.find("contain");
            if(x.find(arr[i],cont)!=std::string::npos){
                arr[arcount] = x.substr(0,cont-2);
                arcount++;
            }
        }
        inFile.close();
    }

    for (int i=0; i<arcount; i++)
    {
        int j;
        for (j = 0; j < i; ++j)
           if (arr[i] == arr[j])
               break;

        if (i == j)
            ++count;
    }
    std::cout << count << '\n';

    return 0;
}
