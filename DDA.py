from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def DDA(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    steps = max(abs(dx), abs(dy))
    
    Xinc = dx / steps
    Yinc = dy / steps
    x = x0
    y = y0

    glBegin(GL_POINTS)
    for i in range(steps + 1):
        glVertex2f(round(x), round(y))
        x += Xinc
        y += Yinc
    glEnd()

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0, 0)
    DDA(50, 50, 200, 200)  # Example line
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"DDA Line")
glClearColor(0, 0, 0, 0)
gluOrtho2D(0, 500, 0, 500)
glutDisplayFunc(draw)
glutMainLoop()
