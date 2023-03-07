#ifndef ALU_H
#define ALU_H

#include "Memory.h"
#include <vector>

class Alu
{
public:
    Alu();
    auto operate();
    void setUserFlag();
    auto getUserFlag() const;
private:
    Memory gp_registers(4, 8);
    std::vector<std::vector<int>> flag_reg;
};

#endif