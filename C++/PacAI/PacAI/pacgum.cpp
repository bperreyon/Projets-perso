#include "pacgum.h"

Pacgum::Pacgum()
{

}

Pacgum::Pacgum(int x,int y,bool isSuper) {
    this->x = x;
    this->y = y;
    this->isSuper = isSuper;
}

bool Pacgum::isSuperPacgum() const {
    return isSuper;
}

int Pacgum::getX() const {
    return x;
}

int Pacgum::getY() const {
    return y;
}
