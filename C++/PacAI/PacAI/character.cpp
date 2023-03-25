#include "character.h"

#include <QTextStream>

Character::Character(QString name, int x, int y)
{
    this->name = name;
    this->x = x;
    this->y = y;
    icon.load(name+".png");
    icon = icon.scaled(SIZE,SIZE);
    lastDirection = Direction::NONE;
}



QString Character::getName() const {
    return name;
}

int Character::getX() const {
    return x;
}

int Character::getY() const {
    return y;
}

void Character::teleport(Direction d){
    switch (d) {
    case Direction::LEFT:
        x = 580;
        break;
    case Direction::RIGHT:
        x=20;
        break;
    default:
        break;
    }
}

QImage Character::getIcon() const {
    return icon;
}

QRect Character::getRect(Direction d) const {
    int futureX(x),futureY(y);

    switch (d) {
    case Direction::UP:
        futureY-=SPEED;
        break;
    case Direction::DOWN:
        futureY+=SPEED;
        break;
    case Direction::LEFT:
        futureX-=SPEED;
        break;
    case Direction::RIGHT:
        futureX+=SPEED;
        break;
    default:
        break;
    }

    return QRect(futureX-SIZE/2,futureY-SIZE/2,SIZE,SIZE);
}


void Character::move(Direction d) {

    switch (d) {
    case Direction::UP:
        y-=SPEED;
        break;
    case Direction::DOWN:
        y+=SPEED;
        break;
    case Direction::LEFT:
        x-=SPEED;
        break;
    case Direction::RIGHT:
        x+=SPEED;
        break;
    default:
        break;
    }
    if (d!=Direction::NONE) {
        lastDirection = d;
    }

}


Direction Character::getLastDirection() const {
    return lastDirection;
}


Direction getOppositeDirection(const Direction &d) {
    switch (d) {
    case Direction::UP:
        return Direction::DOWN;
        break;
    case Direction::DOWN:
        return Direction::UP;
        break;
    case Direction::LEFT:
        return Direction::RIGHT;
        break;
    case Direction::RIGHT:
        return Direction::LEFT;
        break;
    default:
        return Direction::NONE;
        break;
    }
}
