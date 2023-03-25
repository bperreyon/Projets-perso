#include "gamewidget.h"
#include <QPainter>
#include <QTextStream>
#include <QQueue>
#include <QCoreApplication>
#include <QTime>
#include <QThread>

GameWidget::GameWidget(QWidget *parent) : QWidget(parent)
{
    setStyleSheet("background-color:black;");
    setFixedSize(G_WIDTH,G_HEIGHT);
    setFocusPolicy(Qt::StrongFocus);

    createMapMatrix();
    createPacgums();
    createOutlineAndWalls();
    fillIntersections();



    pacman = new Pacman();
    ghosts[0] = new Ghost("Clyde",260,335);
    ghosts[1] = new Ghost("Blinky",300,335);
    ghosts[2] = new Ghost("Pinky",300,305);
    ghosts[3] = new Ghost("Inky",340,335);

    timerId = startTimer(DELAY);
    inGame = true;
    gameTimer = 0;
    difficulty = 1;

}



void GameWidget::createMapMatrix() {

    mapMatrix.append({1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1});
    mapMatrix.append({1,1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1,1});
    mapMatrix.append({1,1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1,1});
    mapMatrix.append({1,1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1,1});
    mapMatrix.append({1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1});
    mapMatrix.append({1,1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1,1});
    mapMatrix.append({1,1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1,1});
    mapMatrix.append({1,1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1});
    mapMatrix.append({1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1});
    mapMatrix.append({1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1});
    mapMatrix.append({1,1,1,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1,1,1,1});
    mapMatrix.append({1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1});
    mapMatrix.append({1,1,1,1,1,1,1,0,1,1,0,1,0,0,0,0,0,0,0,1,0,1,1,0,1,1,1,1,1,1,1});
    mapMatrix.append({0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0});
    mapMatrix.append({1,1,1,1,1,1,1,0,1,1,0,1,0,0,0,0,0,0,0,1,0,1,1,0,1,1,1,1,1,1,1});
    mapMatrix.append({1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1});
    mapMatrix.append({1,1,1,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1,1,1,1});
    mapMatrix.append({1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1});
    mapMatrix.append({1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1});
    mapMatrix.append({1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1});
    mapMatrix.append({1,1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1,1});
    mapMatrix.append({1,1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1,1});
    mapMatrix.append({1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,1});
    mapMatrix.append({1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1,1});
    mapMatrix.append({1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1,1});
    mapMatrix.append({1,1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1});
    mapMatrix.append({1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1});
    mapMatrix.append({1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1});
    mapMatrix.append({1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1});

}

void GameWidget::createPacgums() {

    // Create all the pacgums (one group of code is one line of pacgums)
    for (int i(0);i<12;i++) {
        pacgums.append(Pacgum(50+DISTANCE_BETWEEN_PACGUMS*i,75));
    }
    for (int i(0);i<12;i++) {
        pacgums.append(Pacgum(330+DISTANCE_BETWEEN_PACGUMS*i,75));
    }

    for (int i(0);i<3;i++) {
        pacgums.append(Pacgum(50,95+DISTANCE_BETWEEN_PACGUMS*i,i%2!=0));
        pacgums.append(Pacgum(150,95+DISTANCE_BETWEEN_PACGUMS*i));
        pacgums.append(Pacgum(270,95+DISTANCE_BETWEEN_PACGUMS*i));
        pacgums.append(Pacgum(330,95+DISTANCE_BETWEEN_PACGUMS*i));
        pacgums.append(Pacgum(450,95+DISTANCE_BETWEEN_PACGUMS*i));
        pacgums.append(Pacgum(550,95+DISTANCE_BETWEEN_PACGUMS*i,i%2!=0));
    }

    for (int i(0);i<26;i++) {
        pacgums.append(Pacgum(50+DISTANCE_BETWEEN_PACGUMS*i,155));
    }
    for (int i(0);i<2;i++) {
        pacgums.append(Pacgum(50,175+DISTANCE_BETWEEN_PACGUMS*i));
        pacgums.append(Pacgum(150,175+DISTANCE_BETWEEN_PACGUMS*i));
        pacgums.append(Pacgum(210,175+DISTANCE_BETWEEN_PACGUMS*i));
        pacgums.append(Pacgum(390,175+DISTANCE_BETWEEN_PACGUMS*i));
        pacgums.append(Pacgum(450,175+DISTANCE_BETWEEN_PACGUMS*i));
        pacgums.append(Pacgum(550,175+DISTANCE_BETWEEN_PACGUMS*i));
    }

    for (int i(0);i<6;i++) {
        pacgums.append(Pacgum(50+DISTANCE_BETWEEN_PACGUMS*i,215));
    }
    for (int i(0);i<4;i++) {
        pacgums.append(Pacgum(210+DISTANCE_BETWEEN_PACGUMS*i,215));
    }
    for (int i(0);i<4;i++) {
        pacgums.append(Pacgum(330+DISTANCE_BETWEEN_PACGUMS*i,215));
    }
    for (int i(0);i<6;i++) {
        pacgums.append(Pacgum(450+DISTANCE_BETWEEN_PACGUMS*i,215));
    }

    for (int i(0);i<11;i++) {
        pacgums.append(Pacgum(150,235+DISTANCE_BETWEEN_PACGUMS*i));
        pacgums.append(Pacgum(450,235+DISTANCE_BETWEEN_PACGUMS*i));
    }

    for (int i(0);i<12;i++) {
        pacgums.append(Pacgum(50+DISTANCE_BETWEEN_PACGUMS*i,455));
    }
    for (int i(0);i<12;i++) {
        pacgums.append(Pacgum(330+DISTANCE_BETWEEN_PACGUMS*i,455));
    }

    for (int i(0);i<2;i++) {
        pacgums.append(Pacgum(50,475+DISTANCE_BETWEEN_PACGUMS*i));
        pacgums.append(Pacgum(150,475+DISTANCE_BETWEEN_PACGUMS*i));
        pacgums.append(Pacgum(270,475+DISTANCE_BETWEEN_PACGUMS*i));
        pacgums.append(Pacgum(330,475+DISTANCE_BETWEEN_PACGUMS*i));
        pacgums.append(Pacgum(450,475+DISTANCE_BETWEEN_PACGUMS*i));
        pacgums.append(Pacgum(550,475+DISTANCE_BETWEEN_PACGUMS*i));
    }

    pacgums.append(Pacgum(50,515,true));
    pacgums.append(Pacgum(70,515));
    pacgums.append(Pacgum(90,515));
    for (int i(0);i<7;i++) {
        pacgums.append(Pacgum(150+DISTANCE_BETWEEN_PACGUMS*i,515));
    }
    for (int i(0);i<7;i++) {
        pacgums.append(Pacgum(330+DISTANCE_BETWEEN_PACGUMS*i,515));
    }
    pacgums.append(Pacgum(510,515));
    pacgums.append(Pacgum(530,515));
    pacgums.append(Pacgum(550,515,true));

    for (int i(0);i<2;i++) {
        pacgums.append(Pacgum(90,535+DISTANCE_BETWEEN_PACGUMS*i));
        pacgums.append(Pacgum(150,535+DISTANCE_BETWEEN_PACGUMS*i));
        pacgums.append(Pacgum(210,535+DISTANCE_BETWEEN_PACGUMS*i));
        pacgums.append(Pacgum(390,535+DISTANCE_BETWEEN_PACGUMS*i));
        pacgums.append(Pacgum(450,535+DISTANCE_BETWEEN_PACGUMS*i));
        pacgums.append(Pacgum(510,535+DISTANCE_BETWEEN_PACGUMS*i));
    }

    for (int i(0);i<6;i++) {
        pacgums.append(Pacgum(50+DISTANCE_BETWEEN_PACGUMS*i,575));
    }
    for (int i(0);i<4;i++) {
        pacgums.append(Pacgum(210+DISTANCE_BETWEEN_PACGUMS*i,575));
    }
    for (int i(0);i<4;i++) {
        pacgums.append(Pacgum(330+DISTANCE_BETWEEN_PACGUMS*i,575));
    }
    for (int i(0);i<6;i++) {
        pacgums.append(Pacgum(450+DISTANCE_BETWEEN_PACGUMS*i,575));
    }

    for (int i(0);i<2;i++) {
        pacgums.append(Pacgum(50,595+DISTANCE_BETWEEN_PACGUMS*i));
        pacgums.append(Pacgum(270,595+DISTANCE_BETWEEN_PACGUMS*i));
        pacgums.append(Pacgum(330,595+DISTANCE_BETWEEN_PACGUMS*i));
        pacgums.append(Pacgum(550,595+DISTANCE_BETWEEN_PACGUMS*i));
    }

    for (int i(0);i<26;i++) {
        pacgums.append(Pacgum(50+DISTANCE_BETWEEN_PACGUMS*i,635));
    }
}

void GameWidget::createOutlineAndWalls() {
    // outline
    outline.append(QRect(20,310,105,5));
    outline.append(QRect(125,235,5,80));
    outline.append(QRect(30,235,95,5));
    outline.append(QRect(25,50,5,190));
    outline.append(QRect(30,50,540,5));
    outline.append(QRect(570,50,5,190));
    outline.append(QRect(475,235,95,5));
    outline.append(QRect(470,235,5,80));
    outline.append(QRect(475,310,105,5));

    outline.append(QRect(20,355,105,5));
    outline.append(QRect(125,355,5,80));
    outline.append(QRect(30,430,95,5));
    outline.append(QRect(25,430,5,230));
    outline.append(QRect(30,655,545,5));
    outline.append(QRect(570,430,5,230));
    outline.append(QRect(475,430,95,5));
    outline.append(QRect(470,355,5,80));
    outline.append(QRect(475,355,105,5));

    // Ghost start place
    outline.append(QRect(230,295,5,80));
    outline.append(QRect(235,370,130,5));
    outline.append(QRect(365,295,5,80));
    outline.append(QRect(235,295,45,5));
    outline.append(QRect(320,295,45,5));

    // Upper rectangles
    walls.append(QRect(70,95,60,40));
    walls.append(QRect(170,95,80,40));
    walls.append(QRect(70,175,60,20));

    walls.append(QRect(470,95,60,40));
    walls.append(QRect(350,95,80,40));
    walls.append(QRect(470,175,60,20));

    walls.append(QRect(290,50,20,85));

    // Center shapes
    walls.append(QRect(170,175,20,140));
    walls.append(QRect(190,235,60,20));
    walls.append(QRect(170,355,20,80));

    walls.append(QRect(410,175,20,140));
    walls.append(QRect(350,235,60,20));
    walls.append(QRect(410,355,20,80));

    walls.append(QRect(230,175,140,20));
    walls.append(QRect(290,195,20,60));
    walls.append(QRect(230,415,140,20));
    walls.append(QRect(290,435,20,60));

    // Bottom shapes
    walls.append(QRect(70,475,60,20));
    walls.append(QRect(110,495,20,60));
    walls.append(QRect(170,475,80,20));
    walls.append(QRect(70,595,180,20));
    walls.append(QRect(170,535,20,60));
    walls.append(QRect(25,535,45,20));

    walls.append(QRect(470,475,60,20));
    walls.append(QRect(470,495,20,60));
    walls.append(QRect(350,475,80,20));
    walls.append(QRect(350,595,180,20));
    walls.append(QRect(410,535,20,60));
    walls.append(QRect(530,535,45,20));

    walls.append(QRect(230,535,140,20));
    walls.append(QRect(290,555,20,60));
}

void GameWidget::fillIntersections() {
    intersections.append(QPoint(50,75));
    intersections.append(QPoint(150,75));
    intersections.append(QPoint(270,75));
    intersections.append(QPoint(330,75));
    intersections.append(QPoint(450,75));
    intersections.append(QPoint(550,75));
    intersections.append(QPoint(50,155));
    intersections.append(QPoint(150,155));
    intersections.append(QPoint(210,155));
    intersections.append(QPoint(270,155));
    intersections.append(QPoint(330,155));
    intersections.append(QPoint(390,155));
    intersections.append(QPoint(450,155));
    intersections.append(QPoint(550,155));
    intersections.append(QPoint(50,215));
    intersections.append(QPoint(150,215));
    intersections.append(QPoint(210,215));
    intersections.append(QPoint(270,215));
    intersections.append(QPoint(330,215));
    intersections.append(QPoint(390,215));
    intersections.append(QPoint(450,215));
    intersections.append(QPoint(550,215));
    intersections.append(QPoint(210,275));
    intersections.append(QPoint(270,275));
    intersections.append(QPoint(300,275));
    intersections.append(QPoint(330,275));
    intersections.append(QPoint(390,275));
    intersections.append(QPoint(150,335));
    intersections.append(QPoint(210,335));
    intersections.append(QPoint(390,335));
    intersections.append(QPoint(450,335));
    intersections.append(QPoint(210,395));
    intersections.append(QPoint(390,395));
    intersections.append(QPoint(50,455));
    intersections.append(QPoint(150,455));
    intersections.append(QPoint(210,455));
    intersections.append(QPoint(270,455));
    intersections.append(QPoint(330,455));
    intersections.append(QPoint(390,455));
    intersections.append(QPoint(450,455));
    intersections.append(QPoint(550,455));
    intersections.append(QPoint(50,515));
    intersections.append(QPoint(150,515));
    intersections.append(QPoint(210,515));
    intersections.append(QPoint(270,515));
    intersections.append(QPoint(330,515));
    intersections.append(QPoint(390,515));
    intersections.append(QPoint(450,515));
    intersections.append(QPoint(550,515));
    intersections.append(QPoint(50,575));
    intersections.append(QPoint(90,575));
    intersections.append(QPoint(150,575));
    intersections.append(QPoint(210,575));
    intersections.append(QPoint(270,575));
    intersections.append(QPoint(330,575));
    intersections.append(QPoint(390,575));
    intersections.append(QPoint(450,575));
    intersections.append(QPoint(510,575));
    intersections.append(QPoint(550,575));
    intersections.append(QPoint(50,635));
    intersections.append(QPoint(270,635));
    intersections.append(QPoint(330,635));
    intersections.append(QPoint(550,635));

}

void GameWidget::paintEvent(QPaintEvent *event) {

    Q_UNUSED(event);
    doDrawing();
}

void GameWidget::doDrawing() {

    QPainter painter(this);
    drawWalls(painter);
    drawPacgums(painter);
    painter.drawImage(pacman->getX()-Character::SIZE/2,pacman->getY()-Character::SIZE/2,pacman->getIcon());
    for (int i(0);i<4;i++) {
        painter.drawImage(ghosts[i]->getX()-Character::SIZE/2,ghosts[i]->getY()-Character::SIZE/2,ghosts[i]->getIcon());
    }


    QString score = "Score: "+QString::number((pacman->getScore()));
    QString time = "Time: "+QString::number(gameTimer/1000);
    QFont font("Courier", 15, QFont::DemiBold);
    painter.setPen(QColor("#ffffff"));
    painter.setBrush(QBrush("#ffffff"));
    painter.setFont(font);
    painter.drawText(10,30,score);
    painter.drawText(300,30,time);
}


void GameWidget::drawWalls(QPainter &painter) {
    painter.setPen(QColor("#0000ff"));
    painter.setBrush(QBrush("#000000"));
    int radius = 10;

    for (int i(0);i<outline.length();i++) {
        painter.drawRect(outline[i]);
    }

    for (int i(0);i<walls.length();i++) {
        painter.drawRoundedRect(walls[i],radius,radius);
    }
}

void GameWidget::drawPacgums(QPainter &painter) {

    painter.setPen(QColor("#ffffff"));
    painter.setBrush(QBrush("#ffffff"));

    int basicRadius = 2;
    for (int i(0);i<pacgums.length();i++) {
        int radius = pacgums[i].isSuperPacgum() ? basicRadius*8 : basicRadius;
        painter.drawEllipse(pacgums[i].getX()-radius/2,pacgums[i].getY()-radius/2,radius,radius);
    }
}

void GameWidget::timerEvent(QTimerEvent *e) {

    Q_UNUSED(e);

    if (inGame) {
        gameTimer+=DELAY;
        move();

        if (pacgums.isEmpty()) {
            gameWon();
        }

    }



    repaint();
}

void GameWidget::move() {

    /* Pacman */
    Direction desiredDirection = pacman->getDirection();
    QRect coords = pacman->getRect(desiredDirection);
    // Check if movement is possible
    if (!checkCollision(coords)) {
        pacman->move(desiredDirection);
    } else {
        Direction lastDirection = pacman->getLastDirection();
        coords = pacman->getRect(lastDirection);

        if (!checkCollision(coords)) {
            pacman->move(lastDirection);
        }
    }
    checkTeleport(pacman);

    /* Ghosts */
    for (int i(0);i<4;i++) {

        int numberOfMoves = ghosts[i]->getState()==State::EATEN ? SPEED_MULTIPLICATOR_FOR_EATEN_GHOST : 1;

        for (int j(0);j<numberOfMoves;j++) {

            Direction desiredDirection;
            QRect coords;
            bool collision = true;
            do {
                desiredDirection = ghosts[i]->getDirection(pacman->getX(),pacman->getY(),difficulty);

                coords = ghosts[i]->getRect(desiredDirection);
                collision = checkCollision(coords);
                if (collision) {
                    ghosts[i]->resetKeepDirection();
                }
            } while (collision);
            ghosts[i]->move(desiredDirection);

            checkTeleport(ghosts[i]);

            if ((ghosts[i]->getState()==State::EATEN) && (GHOST_SPAWNER.contains(coords))) {
                ghosts[i]->setState(State::NORMAL);
            }

            for (int k(0);k<intersections.length();k++) {
                if ((intersections[k].x()==ghosts[i]->getX()) && (intersections[k].y()==ghosts[i]->getY())) {

                    if (ghosts[i]->getState()==State::EATEN && !ghosts[i]->hasPathToSpawner()) {
                        ghosts[i]->setPathToSpawner(findPathTo(ghosts[i]));
                        ghosts[i]->resetKeepDirection();
                    }

                    if (ghosts[i]->hasWaited()) {
                        ghosts[i]->stopWaiting();
                        ghosts[i]->resetKeepDirection();
                    } else {
                        ghosts[i]->waitAtIntersection();
                    }
                    break;
                }
            }
        }

    }

    /* Check pacgums */
    checkPacgums();

    /* Character collision */
    int minSurfaceAreaOfCollision = pow(Character::SIZE,2)*PERCENTAGE_OF_INTERSECTION_FOR_COLLISION/100;
    QRect pacmanCoords = pacman->getRect();
    for (int i(0);i<4;i++) {
        QRect ghostCoords = ghosts[i]->getRect();
        QRect intersection = ghostCoords.intersected(pacmanCoords);

        if (intersection.width()*intersection.height()>minSurfaceAreaOfCollision) {
            switch (ghosts[i]->getState()) {
            case State::NORMAL:
                gameOver();
                break;
            case State::EATABLE:
                pacman->increaseScore(200*pow(2,pacman->getNGhostEaten()));
                pacman->increaseNGhostEaten();
                ghosts[i]->setState(State::EATEN);
                ghosts[i]->resetKeepDirection();
                break;
            case State::EATEN:
                break;
            default:
                break;
            }
        }
    }
}

void GameWidget::checkTeleport(Character* chara) {
    if ((chara->getX()<20) && (chara->getLastDirection()==Direction::LEFT)) {
        chara->teleport(Direction::LEFT);
    } else if ((chara->getX()>580) && (chara->getLastDirection()==Direction::RIGHT)) {
        chara->teleport(Direction::RIGHT);
    }
}


void GameWidget::checkPacgums() {
    // Check if pacman is on a pacgum
    int i(0);
    for (i;i<pacgums.length();i++) {
        if ((pacgums[i].getX()==pacman->getX()) && (pacgums[i].getY()==pacman->getY())) {
            break;
        }
    }
    if (i<pacgums.length()) {
        int points = Pacgum::points;
        if (pacgums[i].isSuperPacgum()) {
            onSuperPacgum();
            points*=5;
        }
        pacman->increaseScore(points);
        pacgums.remove(i);
    }

    // Check end of super pacgum
    if (timeSuper>0) {
       timeSuper-=DELAY;
       if (timeSuper<=2000) {
           for (int i(0);i<4;i++) {
               ghosts[i]->setIcon(true);
           }
       }
       if (timeSuper<=0) {
           pacman->resetNGhostEaten();
           for (int i(0);i<4;i++) {
               if (ghosts[i]->getState()==State::EATABLE) {
                   ghosts[i]->setState(State::NORMAL);
                   ghosts[i]->resetKeepDirection();
               }
           }
       }
    }
}

void GameWidget::onSuperPacgum() {
    timeSuper = SUPER_PACGUM_DURATION;
    for (int i(0);i<4;i++){
        ghosts[i]->setState(State::EATABLE);
        ghosts[i]->resetKeepDirection();
    }
    pacman->resetNGhostEaten();
}

bool GameWidget::checkCollision(QRect const&coords) {
    for (int i(0);i<outline.length();i++) {
        if (outline[i].intersects(coords)) {
            return true;
        }
    }

    for (int i(0);i<walls.length();i++) {
        if (walls[i].intersects(coords)) {
            return true;
        }
    }

    return false;
}

void GameWidget::keyPressEvent(QKeyEvent* event) {
    int key = event->key();
    QTextStream out(stdout);

    switch (key) {
    case Qt::Key_Z:
    case Qt::Key_Up:
        pacman->setDesiredDirection(Direction::UP);
        break;
    case Qt::Key_S:
    case Qt::Key_Down:
        pacman->setDesiredDirection(Direction::DOWN);
        break;
    case Qt::Key_Q:
    case Qt::Key_Left:
        pacman->setDesiredDirection(Direction::LEFT);
        break;
    case Qt::Key_D:
    case Qt::Key_Right:
        pacman->setDesiredDirection(Direction::RIGHT);
        break;
    case Qt::Key_P:
        out << pacman->getX() << ";" << pacman->getY()<< Qt::endl;
        out << ghosts[0]->getX() << ";" << ghosts[0]->getY()<< Qt::endl;
        out << ghosts[1]->getX() << ";" << ghosts[1]->getY()<< Qt::endl;
        out << ghosts[2]->getX() << ";" << ghosts[2]->getY()<< Qt::endl;
        out << ghosts[3]->getX() << ";" << ghosts[3]->getY()<< Qt::endl;
        break;
    default:
        break;
    }

    QWidget::keyPressEvent(event);
}

void GameWidget::gameOver() {
    inGame=false;
    emit endGame();

}

void GameWidget::gameWon() {
    inGame = false;

    QThread::sleep(2);

    createPacgums();

    pacman->resetForNextGame();
    ghosts[0]->resetForNextGame(260,335);
    ghosts[1]->resetForNextGame(300,335);
    ghosts[2]->resetForNextGame(300,305);
    ghosts[3]->resetForNextGame(340,335);

    inGame = true;
    difficulty++;

}

QVector<Direction> GameWidget::findPathTo(Ghost *ghost,QPoint const&target) const{

    QPoint start = convertCoordinatesToMatrix(ghost->getX(),ghost->getY());
    QPoint targetInMatrix = convertCoordinatesToMatrix(target.x(),target.y());

    /*QTextStream out(stdout);
    out << ghost->getName() << Qt::endl;
    out << "(" << ghost->getX() << "," << ghost->getY() << ") - ";
    out << "(" << start.x() << "," << start.y() << ") ; ";
    out << "(" << target.x() << "," << target.y() << ") - ";
    out << "(" << targetInMatrix.x() << "," << targetInMatrix.y() << ") ; ";*/

    QHash<QPoint,QPoint> pathHash = findPathInMatrix(start,targetInMatrix);
    QVector<QPoint> path = returnPath(pathHash,start,targetInMatrix);

    /*for (int i = 0; i < path.length(); ++i) {
        out << "(" << path[i].x() << "," << path[i].y() << ") - ";
    }
    out << " ; ";*/

    QVector<Direction> directions = convertPathToDirections(path);

    /*for (int i = 0; i < directions.length(); ++i) {
        out << directions[i] << "-";
    }
    out << Qt::endl;*/

    return directions;
}


QHash<QPoint,QPoint> GameWidget::findPathInMatrix(QPoint const&start,QPoint const&target) const{


    int M = mapMatrix.length();
    int N = mapMatrix[0].length();

    // Find path in matrix
    QQueue<QPoint> priorityQueue;
    priorityQueue.enqueue(start);

    QHash<QPoint,QPoint> path; // The value is the QPoint that allows to go to the key QPoint;

    bool pathFound = false;
    QPoint directions[4] = {QPoint(0,-1),QPoint(0,1),QPoint(-1,0),QPoint(1,0)};

    while ((!priorityQueue.isEmpty()) && (!pathFound)) {

        QPoint currentNode = priorityQueue.dequeue();

        for (int i(0);i<std::size(directions);i++) {
            QPoint newNode = QPoint(currentNode.x()+directions[i].x(),currentNode.y()+directions[i].y());

            // Going outisde of the matrix is forbidden
            if ((newNode.x()>N-1) || (newNode.x()<0) || (newNode.y()>M-1) || (newNode.y()<0) ) {
                continue;
            }
            // Going on a wall is forbidden
            if (mapMatrix[newNode.y()][newNode.x()]==1) {
                continue;
            }
            // Going back on an already explored path is forbidden
            if (path.contains(newNode)) {
                continue;
            }

            path[newNode] = currentNode;

            if (newNode==target) {
                pathFound = true;
                break;
            }

            priorityQueue.enqueue(newNode);
        }
    }
    if (!pathFound) {
        throw;
    }
    return path;
}

QVector<QPoint> GameWidget::returnPath(QHash<QPoint,QPoint> const&path, QPoint const&start, QPoint const&target) const{
    QPoint currentNode = target;
    QVector<QPoint> realPath;

    while (currentNode!=start) {
        realPath.prepend(currentNode);
        currentNode = path[currentNode];
    }
    realPath.prepend(start);

    return realPath;

}

QVector<Direction> GameWidget::convertPathToDirections(QVector<QPoint> const&path) const{

    QVector<Direction> directions;
    if (path[1].x()>path[0].x()) {
        directions.append(Direction::RIGHT);
    } else if (path[1].x()<path[0].x()) {
        directions.append(Direction::LEFT);
    } else if (path[1].y()>path[0].y()) {
        directions.append(Direction::DOWN);
    } else if (path[1].y()<path[0].y()) {
        directions.append(Direction::UP);
    }


    for (int i(1);i<path.length()-1;i++) {

        QPoint realCoords = convertMatrixToCoordinates(path[i].x(),path[i].y());

        if (intersections.contains(realCoords)) {
            if (path[i+1].x()>path[i].x()) {
                directions.append(Direction::RIGHT);
            } else if (path[i+1].x()<path[i].x()) {
                directions.append(Direction::LEFT);
            } else if (path[i+1].y()>path[i].y()) {
                directions.append(Direction::DOWN);
            } else if (path[i+1].y()<path[i].y()) {
                directions.append(Direction::UP);
            }
        }
    }

    return directions;
}


QPoint GameWidget::convertCoordinatesToMatrix(int x, int y) const {
    int X = (x-10)/20 + ((x>=300) ? 1 : 0);
    int Y = (y-75)/20;

    return QPoint(X,Y);
}

QPoint GameWidget::convertMatrixToCoordinates(int X, int Y) const {
    int x = (X>15) ? 10 + 20*(X-1) :
            (X<15) ? 10 + 20*X :
                     300;
    int y = 75 + 20*Y;
    return QPoint(x,y);
}
