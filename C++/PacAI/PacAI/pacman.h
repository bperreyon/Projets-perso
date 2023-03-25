#ifndef PACMAN_H
#define PACMAN_H

#include "character.h"

class Pacman : public Character
{
public:
    Pacman();
    /// Returns the desired direction of pacman.
    Direction getDirection() const;
    void setDesiredDirection(Direction d);
    void increaseScore(int value);
    int getScore() const;
    /// Increase the number of ghosts eaten during one super pacgum by one.
    void increaseNGhostEaten();
    void resetNGhostEaten();
    int getNGhostEaten() const;

    /// Updates the coordinates of pacman and rotate ist icon.
    void move(Direction d);

    /// Resets pacman attributes except from score to play the next game.
    void resetForNextGame();

private:
    int score;
    Direction desiredDirection;

    int nGhostsEaten;

    static const int xStart = 310;
    static const int yStart = 515;
};

#endif // PACMAN_H
