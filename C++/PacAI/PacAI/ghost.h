#ifndef GHOST_H
#define GHOST_H

#include "character.h"
#include <QRandomGenerator>

enum State {
    NORMAL,
    EATABLE,
    EATEN,
};


class Ghost : public Character
{
public:
    Ghost(QString name,int x,int y);
    /// Returns the direction in which the ghost wants to go. It depends mostly on whether the ghost is on an intersection, its state, the location of pacman and the difficulty level.
    Direction getDirection(int pacmanX,int pacmanY, int difficulty);
    State getState() const;
    void setState(State state);
    bool getKeepDirection() const;
    void resetKeepDirection();
    /// Change the icon of the ghost based on its state.
    void setIcon(bool end=false);
    void setPathToSpawner(QVector<Direction> path);
    /// Indicates whether the pathToSpawner attribute has been set.
    bool hasPathToSpawner() const;
    /// Allows the ghost to wait for one frame when arriving at an intersection, making him slower than pacman.
    void waitAtIntersection();
    bool hasWaited() const;
    void stopWaiting();

    /// Updates the coordinates of the ghost and clear the possibleDirections attribute.
    void move(Direction d);
    /// Resets the ghost attributes to play the next game.
    void resetForNextGame(int x,int y);



private:
    State state;
    bool keepDirection;
    bool wait;
    QVector<Direction> pathToSpawner;
    QVector<Direction> possibleDirections;

    /// Selects a random direction.
    Direction chooseRandomDirection() const;
    /// Lists the direction the ghost can choose giving priority to the most interresant ones but still randomly.
    void setPossibleDirections(Direction hor,Direction ver, Direction opp);

    static const int MINIMUM_DISTANCE_WITH_PACMAN_WHEN_EATABLE = 200;

};

#endif // GHOST_H
