import random
import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# -------- Config --------
n = 6
cx, cy = 0.0, 0.0   # center
r = 0.8             # radius
steps = 100

data = [random.randint(5, 50) for _ in range(n)]
total = sum(data)

angles = [(360 * d) / total for d in data]

# Random colors for slices
colors = [(random.random(), random.random(), random.random()) for _ in range(n)]

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    start_angle = 0.0

    for i, angle in enumerate(angles):
        end_angle = start_angle + angle

        glColor3f(*colors[i])
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(cx, cy)  # center of pie

        for k in range(steps + 1):
            alpha = start_angle + (k / steps) * (end_angle - start_angle)
            rad = math.radians(alpha)
            x = cx + r * math.cos(rad)
            y = cy + r * math.sin(rad)
            glVertex2f(x, y)
        glEnd()

        start_angle = end_angle

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Pie Chart using OpenGL")

    glClearColor(1.0, 1.0, 1.0, 1.0)  # white background
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  # coordinate system

    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
