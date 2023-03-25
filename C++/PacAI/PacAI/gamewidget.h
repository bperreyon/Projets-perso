#ifndef GAMEWIDGET_H
#define GAMEWIDGET_H

#include <QWidget>
#include <QRect>
#include <QPoint>
#include "pacgum.h"
#include "pacman.h"
#include "ghost.h"



class GameWidget: public QWidget
{
    Q_OBJECT

public:
    GameWidget(QWidget *parent = nullptr);

    static constexpr QRect GHOST_SPAWNER = QRect(235,300,130,70);

protected:
    /// Reacts on QPaintEvent by calling doDrawing().
    void paintEvent(QPaintEvent *event);
    /// Reacts on QTimerEvent to allow to update the game.
    void timerEvent(QTimerEvent *event);
    /// Reacts on QKeyEvent by storing the correspondant direction in the desiredDirection of pacman.
    void keyPressEvent(QKeyEvent* event);

private:
    static const int G_WIDTH = 600;
    static const int G_HEIGHT = 700;
    static const int DISTANCE_BETWEEN_PACGUMS = 20;
    static const int DELAY = 50;
    static constexpr QPoint GHOST_SPAWNER_ENTRANCE = QPoint(300,335);
    static const int SPEED_MULTIPLICATOR_FOR_EATEN_GHOST = 2;
    static const int SUPER_PACGUM_DURATION = 100*DELAY;
    static const int PERCENTAGE_OF_INTERSECTION_FOR_COLLISION = 50;

    QVector<QRect> outline;
    QVector<QRect> walls;
    QVector<Pacgum> pacgums;
    QVector<QPoint> intersections;
    QVector<QVector<int>> mapMatrix;
    Pacman* pacman;
    Ghost* ghosts[4];
    int timerId;
    int timeSuper;
    bool inGame;
    int difficulty;
    int gameTimer;

    /// Draws the walls, the pacgums and the characters on the widget.
    void doDrawing();
    /// Draws the walls on the widget.
    void drawWalls(QPainter &painter);
    /// Draws the pacgums on the widget.
    void drawPacgums(QPainter &painter);
    /// Creates and stores all the pacgums in the attribute pacgums.
    void createPacgums();
    /// Creates and stores the outlines and walls in the attribute walls.
    void createOutlineAndWalls();
    /// Stores the location of all intersections and curves.
    void fillIntersections();
    /// Creates 2d-array that represents the map with the walls.
    void createMapMatrix();
    /// Asks and checks desired movement of all characters. Allows them to move and do post-movement process.
    void move();
    /// Checks if a character needs to be teleported.
    void checkTeleport(Character* chara);
    /// Checks if a character collides with a wall.
    bool checkCollision(QRect const&coords);
    /// Checks if pacman is on a pacgum.
    void checkPacgums();
    /// Activates super pacgum, allowing pacman to eat the ghosts.
    void onSuperPacgum();
    /// Stops the game and emit endGame().
    void gameOver();
    /// Stops the game and launch a new one, increasing the difficulty.
    void gameWon();

    /// Finds the shorter path to the specified target and returns it as a list of directions.
    QVector<Direction> findPathTo(Ghost* ghost, QPoint const&target = GHOST_SPAWNER_ENTRANCE) const;
    /// Explores paths to the specified target using the 2d-array representation of the map.
    QHash<QPoint,QPoint> findPathInMatrix(QPoint const&start, QPoint const&target) const;
    /// Returns the shortest path to the specified target from the paths explored.
    QVector<QPoint> returnPath(QHash<QPoint,QPoint> const&path, QPoint const&start, QPoint const&target) const;
    /// Converts the founded path into a list of directions using the intersections attribute.
    QVector<Direction> convertPathToDirections(QVector<QPoint> const&path) const;

    /// Converts the graphical coordinates into 2d-array indexes.
    QPoint convertCoordinatesToMatrix(int x,int y) const;
    /// Converts the 2d-array indexes into graphical coordinates.
    QPoint convertMatrixToCoordinates(int X, int Y) const;


signals:
    /// Calls the onEndGame() method of the MainWindow class.
    void endGame();
};



#endif // GAMEWIDGET_H
