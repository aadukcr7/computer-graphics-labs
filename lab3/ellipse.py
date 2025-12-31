from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def plot_ellipse_points(xc, yc, x, y):
    glVertex2f(xc + x, yc + y)
    glVertex2f(xc - x, yc + y)
    glVertex2f(xc + x, yc - y)
    glVertex2f(xc - x, yc - y)

def midpoint_ellipse(xc, yc, rx, ry):
    x = 0
    y = ry

    rx2 = rx * rx
    ry2 = ry * ry

    dx = 2 * ry2 * x
    dy = 2 * rx2 * y

    # Region 1
    p1 = ry2 - (rx2 * ry) + (0.25 * rx2)

    glBegin(GL_POINTS)
    while dx < dy:
        plot_ellipse_points(xc, yc, x, y)
        if p1 < 0:
            x += 1
            dx = dx + 2 * ry2
            p1 = p1 + dx + ry2
        else:
            x += 1
            y -= 1
            dx = dx + 2 * ry2
            dy = dy - 2 * rx2
            p1 = p1 + dx - dy + ry2

    # Region 2
    p2 = (ry2 * (x + 0.5) * (x + 0.5)) + \
         (rx2 * (y - 1) * (y - 1)) - (rx2 * ry2)

    while y >= 0:
        plot_ellipse_points(xc, yc, x, y)
        if p2 > 0:
            y -= 1
            dy = dy - 2 * rx2
            p2 = p2 + rx2 - dy
        else:
            x += 1
            y -= 1
            dx = dx + 2 * ry2
            dy = dy - 2 * rx2
            p2 = p2 + dx - dy + rx2
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 1, 1)
    midpoint_ellipse(250, 250, 150, 100)
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow(b"Midpoint Ellipse Drawing Algorithm")
glClearColor(0, 0, 0, 0)
gluOrtho2D(0, 500, 0, 500)
glutDisplayFunc(display)
glutMainLoop()
