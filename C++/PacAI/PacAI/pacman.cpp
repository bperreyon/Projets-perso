#include "pacman.h"
#include "pacgum.h"

#include <QTransform>

Pacman::Pacman() : Character("Pacman",xStart,yStart)
{
    score = 0;
    desiredDirection = Direction::LEFT;
    lastDirection = Direction::LEFT;
    nGhostsEaten = 0;
}

void Pacman::resetForNextGame() {
    x = xStart;
    y = yStart;
    lastDirection = Direction::LEFT;
    icon.load(name+".png");
    icon = icon.scaled(SIZE,SIZE);

    desiredDirection = Direction::LEFT;
    nGhostsEaten = 0;

}

void Pacman::move(Direction d) {
    if (d!=Direction::NONE) {
        icon = icon.transformed(QTransform().rotate(90*(d-lastDirection)));
    }

    Character::move(d);
}



Direction Pacman::getDirection() const {
    return desiredDirection;
}

void Pacman::setDesiredDirection(Direction d) {
    desiredDirection = d;
}

void Pacman::increaseScore(int value) {
    score+=value;
}

int Pacman::getScore() const {
    return score;
}

void Pacman::increaseNGhostEaten(){
    nGhostsEaten++;
}

void Pacman::resetNGhostEaten() {
    nGhostsEaten=0;
}

int Pacman::getNGhostEaten() const {
    return nGhostsEaten;
}
