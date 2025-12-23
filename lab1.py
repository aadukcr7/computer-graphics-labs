from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def draw_A(x):
    glBegin(GL_POLYGON)
    glVertex2f(x, 100)
    glVertex2f(x + 20, 200)
    glVertex2f(x + 40, 100)
    glVertex2f(x + 30, 100)
    glVertex2f(x + 25, 130)
    glVertex2f(x + 15, 130)
    glVertex2f(x + 10, 100)
    glEnd()


def draw_D(x):
    glBegin(GL_POLYGON)
    glVertex2f(x, 100)
    glVertex2f(x, 200)
    glVertex2f(x + 30, 180)
    glVertex2f(x + 30, 120)
    glEnd()


def draw_I(x):
    glBegin(GL_POLYGON)
    glVertex2f(x, 100)
    glVertex2f(x + 15, 100)
    glVertex2f(x + 15, 200)
    glVertex2f(x, 200)
    glEnd()


def draw_T(x):
    glBegin(GL_POLYGON)
    glVertex2f(x, 180)
    glVertex2f(x + 40, 180)
    glVertex2f(x + 40, 200)
    glVertex2f(x, 200)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(x + 15, 100)
    glVertex2f(x + 25, 100)
    glVertex2f(x + 25, 180)
    glVertex2f(x + 15, 180)
    glEnd()


def draw_Y(x):
    glBegin(GL_POLYGON)
    glVertex2f(x, 200)
    glVertex2f(x + 20, 160)
    glVertex2f(x + 40, 200)
    glVertex2f(x + 30, 200)
    glVertex2f(x + 20, 180)
    glVertex2f(x + 10, 200)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(x + 18, 100)
    glVertex2f(x + 22, 100)
    glVertex2f(x + 22, 160)
    glVertex2f(x + 18, 160)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    
    glColor3f(0.1, 0.5, 0.9)   
    draw_A(50)
    draw_A(110)
    glColor3f(0.0, 0.0, 0.0)
    draw_D(170)
    draw_I(230)
    glColor3f(1.0, 1.0, 0.0)

    draw_T(260)
    draw_Y(320)
    glColor3f(0.6, 0.0, 0.6)
    draw_A(380)

    glFlush()


def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)   # White background
    gluOrtho2D(0, 500, 0, 300)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(700, 300)
    glutCreateWindow(b"Name Using OpenGL Polygons")

    init()
    glutDisplayFunc(display)
    glutMainLoop()


main()
