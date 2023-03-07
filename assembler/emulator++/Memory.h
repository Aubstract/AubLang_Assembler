#ifndef ALU_H
#define ALU_H

#include <vector>
#include <cmath>
#include <iomanip>

class Memory
{
public:
    Memory(int, int);
    void setMem(int, int);
    int getMem(int) const;
    int getNumAddr() const;
    int getNumBits() const;
private:
    int num_addr;
    int num_bits;
    std::vector<int> mem;
};

#endif