#ifndef CHARACTER_H
#define CHARACTER_H

#include <QString>
#include <QImage>
#include <QRect>
#include <QKeyEvent>

enum Direction {
    UP,
    RIGHT,
    DOWN,
    LEFT,
    NONE
};


class Character : public QObject
{
    Q_OBJECT

public:
    Character(QString name, int x, int y);
    /// Updates the character coordinates and lastDirection.
    void move(Direction d);
    int getX() const;
    int getY() const;
    /// Teleports the character to the other side of the map.
    void teleport(Direction d);
    /// Returns a QRect representing the caracter location and its size. Used to check collision.
    QRect getRect(Direction d=Direction::NONE) const;
    QImage getIcon() const;
    QString getName() const;
    Direction getLastDirection() const;

    static const int SIZE = 30;

protected:
    QString name;
    int x;
    int y;
    QImage icon;
    Direction lastDirection;

    static const int SPEED = 10;

};

/// Returns the opposite direction of te one in input. The opposite of NONE is NONE.
Direction getOppositeDirection(Direction const&d);

#endif // CHARACTER_H
