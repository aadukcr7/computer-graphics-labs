from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Window boundaries
xmin, ymin, xmax, ymax = -100, -100, 100, 100

INSIDE, LEFT, RIGHT, BOTTOM, TOP = 0, 1, 2, 4, 8

def compute_code(x, y):
    code = INSIDE
    if x < xmin: code |= LEFT
    elif x > xmax: code |= RIGHT
    if y < ymin: code |= BOTTOM
    elif y > ymax: code |= TOP
    return code

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

def cohen_sutherland(x1, y1, x2, y2):
    code1 = compute_code(x1, y1)
    code2 = compute_code(x2, y2)

    while True:
        if code1 == 0 and code2 == 0:
            glColor3f(0, 1, 0)
            glBegin(GL_LINES)
            glVertex2f(x1, y1)
            glVertex2f(x2, y2)
            glEnd()
            break

        elif code1 & code2:
            break

        else:
            code_out = code1 if code1 else code2

            if code_out & TOP:
                if y2 != y1:
                    x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                else:
                    x = x1
                y = ymax
            elif code_out & BOTTOM:
                if y2 != y1:
                    x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                else:
                    x = x1
                y = ymin
            elif code_out & RIGHT:
                if x2 != x1:
                    y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                else:
                    y = y1
                x = xmax
            else:
                if x2 != x1:
                    y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                else:
                    y = y1
                x = xmin

            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_axes()
    draw_window()

    # Original line
    glColor3f(1, 0, 0)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

    cohen_sutherland(x1, y1, x2, y2)
    glFlush()

def main():
    global x1, y1, x2, y2
    
    print("=" * 50)
    print("COHEN-SUTHERLAND LINE CLIPPING ALGORITHM")
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
    glutCreateWindow(b"Cohen Sutherland Line Clipping")
    gluOrtho2D(-300, 300, -300, 300)
    glutDisplayFunc(display)
    glutMainLoop()

x1, y1, x2, y2 = 0, 0, 0, 0
main()
