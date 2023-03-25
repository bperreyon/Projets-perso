#include "ghost.h"
#include "gamewidget.h"
#include <QRandomGenerator>
#include <QTextStream>

Ghost::Ghost(QString name,int x,int y) : Character(name,x,y)
{
    state= State::NORMAL;
    keepDirection = false;
    wait = false;
}

void Ghost::resetForNextGame(int x, int y) {
    this->x = x;
    this->y = y;
    lastDirection = Direction::NONE;
    icon.load(name+".png");
    icon = icon.scaled(SIZE,SIZE);

    state= State::NORMAL;
    keepDirection = false;
    wait = false;
}


void Ghost::move(Direction d) {
    Character::move(d);
    possibleDirections.clear();
}

bool Ghost::getKeepDirection() const {
    return keepDirection;
}

void Ghost::resetKeepDirection() {
    keepDirection = false;
}

Direction Ghost::getDirection(int pacmanX, int pacmanY, int difficulty)  {
    if (wait) {
        return Direction::NONE;
    }


    // Case 1 : the ghost is in the spawner, it tries to go out
    if (GameWidget::GHOST_SPAWNER.contains(getRect())) {
        int r = QRandomGenerator::global()->bounded(0,5);
        switch (r) {
        case 0:
            return Direction::UP;
            break;
        case 1:
            return Direction::DOWN;
            break;
        case 2:
            return Direction::LEFT;
            break;
        case 3:
            return Direction::RIGHT;
            break;
        case 4:
            return (x<300) ? Direction::RIGHT :
                   (x>300) ? Direction::LEFT :
                             Direction::UP;
            break;
        }
    }

    // Case 2 : the ghost continues on its path (no intersection)
    if (keepDirection) {
        return lastDirection;
    }

    keepDirection = true;

    // Case 3 : the ghost is in normal mode, it tries to catch pacman
    if (state==State::NORMAL) {

        if (possibleDirections.isEmpty()) {

            Direction horizontalDirection = (pacmanX<x) ? Direction::LEFT : (pacmanX>x) ? Direction::RIGHT : Direction::NONE;
            Direction verticalDirection = (pacmanY<y) ? Direction::UP : (pacmanY>y) ? Direction::DOWN : Direction::NONE;

            Direction oppositeDirection = getOppositeDirection(lastDirection);

            setPossibleDirections(horizontalDirection,verticalDirection,oppositeDirection);

        }

        int r = QRandomGenerator::global()->bounded(0,9);
        if (r<2*difficulty){
            return possibleDirections.takeFirst();
        }
        r = QRandomGenerator::global()->bounded(0,possibleDirections.length());
        return possibleDirections.takeAt(r);

    } else if (state==State::EATABLE) { // Case 4 : the ghost is in etable mode, it tries to run away from pacman

        if (abs(pacmanX-x)+abs(pacmanY-y)<MINIMUM_DISTANCE_WITH_PACMAN_WHEN_EATABLE) {
            if (possibleDirections.isEmpty()) {
                Direction horizontalDirection = (pacmanX<x) ? Direction::RIGHT : (pacmanX>x) ? Direction::LEFT : Direction::NONE;
                Direction verticalDirection = (pacmanY<y) ? Direction::DOWN : (pacmanY>y) ? Direction::UP : Direction::NONE;

                Direction oppositeDirection = getOppositeDirection(lastDirection);

                setPossibleDirections(horizontalDirection,verticalDirection,oppositeDirection);
            }

            int r = QRandomGenerator::global()->bounded(0,9);
            if (r<2*difficulty) {
                return possibleDirections.takeFirst();
            }
            r = QRandomGenerator::global()->bounded(0,possibleDirections.length());
            return possibleDirections.takeAt(r);
        }

        Direction oppositeDirection = getOppositeDirection(lastDirection);
        Direction chosenDirection = oppositeDirection;
        while (chosenDirection==oppositeDirection) {
            chosenDirection = chooseRandomDirection();
        }
        return chosenDirection;

    } else { // Case 5 : the ghost has been eaten, it goes back to the spawner
        if (pathToSpawner.isEmpty()) {
            return chooseRandomDirection();
        }
        return pathToSpawner.takeFirst();
    }


    return Direction::NONE;

}

State Ghost::getState() const {
    return state;
}

void Ghost::setState(State state) {
    this->state = state;
    setIcon();
}

void Ghost::setIcon(bool end) {
    switch(state) {
    case State::NORMAL:
        icon.load(name+".png");
        break;
    case State::EATABLE:
        if (!end) {
            icon.load("EatableGhost.png");
        } else {
            icon.load("EndEatableGhost.png");
        }
        break;
    case State::EATEN:
        icon.load("EatenGhost.png");
    }
    icon = icon.scaled(SIZE,SIZE);
}

void Ghost::setPathToSpawner(QVector<Direction> path) {
    pathToSpawner = path;
}

bool Ghost::hasPathToSpawner() const {
    return !pathToSpawner.isEmpty();
}

void Ghost::waitAtIntersection() {
    wait = true;
}

bool Ghost::hasWaited() const {
    return wait;
}

void Ghost::stopWaiting() {
    wait = false;
}

Direction Ghost::chooseRandomDirection() const {
    int r = QRandomGenerator::global()->bounded(0,4);
    switch (r) {
    case 0:
        return Direction::UP;
        break;
    case 1:
        return Direction::DOWN;
        break;
    case 2:
        return Direction::LEFT;
        break;
    case 3:
        return Direction::RIGHT;
        break;
    default:
        return Direction::NONE;
    }
}

void Ghost::setPossibleDirections(Direction hor, Direction ver, Direction opp) {
    if ((ver!=Direction::NONE) && (ver!=opp)) {
        possibleDirections.append(ver);
    }
    if ((hor!=Direction::NONE) && (hor!=opp)) {
        possibleDirections.append(hor);
    }

    if (possibleDirections.length()==2) {
        int r = QRandomGenerator::global()->bounded(0,2);
        if (r==0) {
            possibleDirections.swapItemsAt(0,1);
        }
    }

    // Get all others directions
    QVector<Direction> remainingDirections;
    for (int i(Direction::UP);i<Direction::NONE;i++){
        Direction dir = static_cast<Direction>(i);

        if ((!possibleDirections.contains(dir)) && (dir!=opp)) {
            remainingDirections.append(dir);
        }
    }

    while (!remainingDirections.isEmpty()) {
        int r = QRandomGenerator::global()->bounded(0,remainingDirections.length());
        possibleDirections.append(remainingDirections[r]);
        remainingDirections.remove(r);
    }
}
