from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def midpoint_circle(cx, cy, r):
    x = 0
    y = r
    d = 1 - r

    x_points, y_points = [], []

    while x <= y:
        points = [
            (cx + x, cy + y), (cx - x, cy + y),
            (cx + x, cy - y), (cx - x, cy - y),
            (cx + y, cy + x), (cx - y, cy + x),
            (cx + y, cy - x), (cx - y, cy - x)
        ]
        for px, py in points:
            x_points.append(px)
            y_points.append(py)

        x += 1
        if d < 0:
            d += 2 * x + 1
        else:
            y -= 1
            d += 2 * (x - y) + 1

    return x_points, y_points

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)  # White circle

    x, y = midpoint_circle(250, 250, 100)

    glBegin(GL_POINTS)
    for i in range(len(x)):
        glVertex2i(x[i], y[i])
    glEnd()

    glFlush()

# Setup OpenGL window
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"Midpoint Circle Drawing Algorithm")

glClearColor(0.0, 0.0, 0.0, 0.0)  # Black background
gluOrtho2D(0, 500, 0, 500)        # Coordinate system

glutDisplayFunc(display)
glutMainLoop()
