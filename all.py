from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Global variable for menu choice
choice = 0

# ------------------- DDA Line -------------------
def DDA(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    steps = max(abs(dx), abs(dy))
    Xinc = dx / steps
    Yinc = dy / steps
    x, y = x0, y0
    glBegin(GL_POINTS)
    for _ in range(steps + 1):
        glVertex2f(round(x), round(y))
        x += Xinc
        y += Yinc
    glEnd()

# ------------------- Bresenham Line -------------------
def Bresenham(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    glBegin(GL_POINTS)
    while True:
        glVertex2f(x0, y0)
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
    glEnd()

# ------------------- Midpoint Circle -------------------
def midpoint_circle(xc, yc, r):
    x, y = 0, r
    d = 1 - r
    glBegin(GL_POINTS)
    while x <= y:
        points = [
            (xc + x, yc + y), (xc - x, yc + y),
            (xc + x, yc - y), (xc - x, yc - y),
            (xc + y, yc + x), (xc - y, yc + x),
            (xc + y, yc - x), (xc - y, yc - x)
        ]
        for px, py in points:
            glVertex2f(px, py)
        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1
    glEnd()

# ------------------- Line Graph -------------------
def line_graph(data):
    glBegin(GL_LINE_STRIP)
    for i, val in enumerate(data):
        glVertex2f(50 + i*50, val)
    glEnd()

# ------------------- Pie Chart -------------------
def pie_chart(values):
    total = sum(values)
    start_angle = 0
    for val in values:
        end_angle = start_angle + (val / total) * 360
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(250, 250)  # center
        angle = start_angle
        while angle <= end_angle:
            rad = math.radians(angle)
            glVertex2f(250 + 150*math.cos(rad), 250 + 150*math.sin(rad))
            angle += 1
        glEnd()
        start_angle = end_angle

# ------------------- Display Function -------------------
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 1, 1)
    
    global choice
    if choice == 1:
        DDA(50, 50, 400, 400)
    elif choice == 2:
        Bresenham(50, 50, 400, 200)
        Bresenham(50, 50, 200, 400)
    elif choice == 3:
        midpoint_circle(250, 250, 100)
    elif choice == 4:
        line_graph([100, 200, 150, 300, 250])
    elif choice == 5:
        pie_chart([30, 40, 50, 80])
    
    glFlush()

# ------------------- Menu -------------------
def main():
    global choice
    print("Choose an option to display:")
    print("1: DDA Line")
    print("2: Bresenham Line")
    print("3: Midpoint Circle")
    print("4: Line Graph")
    print("5: Pie Chart")
    choice = int(input("Enter choice (1-5): "))

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"OpenGL Graphics")
    glClearColor(0, 0, 0, 0)
    gluOrtho2D(0, 500, 0, 500)
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
