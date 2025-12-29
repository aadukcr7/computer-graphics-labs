from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Bresenham's Line Algorithm
def bresenham(x1, y1, x2, y2):
    x_points, y_points = [], []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x2 >= x1 else -1
    sy = 1 if y2 >= y1 else -1

    x, y = x1, y1

    if dx > dy:   # |m| < 1
        p = 2 * dy - dx
        for _ in range(dx + 1):
            x_points.append(x)
            y_points.append(y)
            x += sx
            if p >= 0:
                y += sy
                p += 2 * (dy - dx)
            else:
                p += 2 * dy
    else:         # |m| >= 1
        p = 2 * dx - dy
        for _ in range(dy + 1):
            x_points.append(x)
            y_points.append(y)
            y += sy
            if p >= 0:
                x += sx
                p += 2 * (dx - dy)
            else:
                p += 2 * dx

    return x_points, y_points

# OpenGL display function
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)  # White color

    x, y = bresenham(50, 100, 300, 100)

    glBegin(GL_POINTS)  # Draw individual pixels
    for i in range(len(x)):
        glVertex2i(x[i], y[i])
    glEnd()

    glFlush()

# Main setup
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"Bresenham Line Drawing Algorithm")

glClearColor(0.0, 0.0, 0.0, 0.0)  # Black background
gluOrtho2D(0, 500, 0, 500)        # Coordinate system

glutDisplayFunc(display)
glutMainLoop()
