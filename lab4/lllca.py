from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

xmin, ymin, xmax, ymax = -100, -100, 100, 100

def draw_axes():
    glColor3f(0.6, 0.6, 0.6)
    glBegin(GL_LINES)
    glVertex2f(-300, 0)
    glVertex2f(300, 0)
    glVertex2f(0, -300)
    glVertex2f(0, 300)
    glEnd()

def draw_window():
    glColor3f(1, 1, 1)
    glBegin(GL_LINE_LOOP)
    glVertex2f(xmin, ymin)
    glVertex2f(xmax, ymin)
    glVertex2f(xmax, ymax)
    glVertex2f(xmin, ymax)
    glEnd()

def liang_barsky(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    p = [-dx, dx, -dy, dy]
    q = [x1 - xmin, xmax - x1, y1 - ymin, ymax - y1]

    u1, u2 = 0, 1

    for i in range(4):
        if p[i] == 0 and q[i] < 0:
            return
        if p[i] != 0:
            t = q[i] / p[i]
            if p[i] < 0:
                u1 = max(u1, t)
            else:
                u2 = min(u2, t)

    if u1 <= u2:
        x1c = x1 + u1 * dx
        y1c = y1 + u1 * dy
        x2c = x1 + u2 * dx
        y2c = y1 + u2 * dy

        glColor3f(0, 1, 0)
        glBegin(GL_LINES)
        glVertex2f(x1c, y1c)
        glVertex2f(x2c, y2c)
        glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_axes()
    draw_window()

    glColor3f(1, 0, 0)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

    liang_barsky(x1, y1, x2, y2)
    glFlush()

def main():
    global x1, y1, x2, y2
    
    print("=" * 50)
    print("LIANG-BARSKY LINE CLIPPING ALGORITHM")
    print("=" * 50)
    print(f"Window Size: [{xmin}, {ymin}] to [{xmax}, {ymax}]")
    print(f"Window Width: {xmax - xmin}, Height: {ymax - ymin}")
    print("=" * 50)
    
    # Get user input
    x1 = float(input("Enter x1 coordinate: "))
    y1 = float(input("Enter y1 coordinate: "))
    x2 = float(input("Enter x2 coordinate: "))
    y2 = float(input("Enter y2 coordinate: "))
    
    print("\nLine clipping in progress...")
    
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Liang Barsky Line Clipping")
    gluOrtho2D(-300, 300, -300, 300)
    glutDisplayFunc(display)
    glutMainLoop()

x1, y1, x2, y2 = 0, 0, 0, 0
main()
