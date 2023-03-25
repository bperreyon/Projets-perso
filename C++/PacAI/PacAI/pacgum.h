#ifndef PACGUM_H
#define PACGUM_H


class Pacgum
{
public:

    static const int points = 10;

    Pacgum();
    Pacgum(int x,int y,bool isSuper = false);
    bool isSuperPacgum() const;
    int getX() const;
    int getY() const;

private:
    int x;
    int y;
    bool isSuper;

};

#endif // PACGUM_H
