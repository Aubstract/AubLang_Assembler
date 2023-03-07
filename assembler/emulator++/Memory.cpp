#include "Memory.h"


Memory::Memory(int _num_addr, int _num_bits)
{
    num_addr = _num_addr;
    num_bits = _num_bits;
    mem.resize(num_addr);
}


void Memory::setMem(int addr, int val)
{
    int max = pow(2, num_bits) - 1;

    if (val > max)
    {
        throw std::runtime_error("Error: dimensions must agree");
    }
    else
    {
        mem.at(addr) = val;
    }
}


int Memory::getMem(int addr) const
{
    return mem.at(addr);
}


int Memory::getNumAddr() const
{
    return num_addr;
}


int Memory::getNumBits() const
{
    return num_bits;
}