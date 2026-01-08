import sys

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
# Explicitly import the bitmap font constant so Pylance recognizes it
from OpenGL.GLUT import GLUT_BITMAP_HELVETICA_12

xmin, ymin, xmax, ymax = -100, -100, 100, 100
polygon = []

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


def draw_text(x, y, text):
    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(ch))

def inside(p, edge):
    x, y = p
    if edge == 'left': return x >= xmin
    if edge == 'right': return x <= xmax
    if edge == 'bottom': return y >= ymin
    return y <= ymax

def intersect(p1, p2, edge):
    x1, y1 = p1
    x2, y2 = p2

    if edge == 'left':
        x = xmin
        if x2 != x1:
            y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
        else:
            y = y1
    elif edge == 'right':
        x = xmax
        if x2 != x1:
            y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
        else:
            y = y1
    elif edge == 'bottom':
        y = ymin
        if y2 != y1:
            x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
        else:
            x = x1
    else:
        y = ymax
        if y2 != y1:
            x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
        else:
            x = x1

    return (x, y)

def clip_polygon(poly):
    for edge in ['left', 'right', 'bottom', 'top']:
        new_poly = []
        for i in range(len(poly)):
            curr = poly[i]
            prev = poly[i - 1]

            if inside(curr, edge):
                if not inside(prev, edge):
                    new_poly.append(intersect(prev, curr, edge))
                new_poly.append(curr)
            elif inside(prev, edge):
                new_poly.append(intersect(prev, curr, edge))

        poly = new_poly
    return poly

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_axes()
    draw_window()

    # Original polygon
    glColor3f(1, 0, 0)
    glBegin(GL_LINE_LOOP)
    for p in polygon:
        glVertex2f(p[0], p[1])
    glEnd()

    if len(polygon) > 0:
        clipped = clip_polygon(list(polygon))

        # Clipped polygon
        if len(clipped) > 0:
            glColor3f(0, 1, 0)
            glBegin(GL_LINE_LOOP)
            for p in clipped:
                glVertex2f(p[0], p[1])
            glEnd()

    # Legend
    draw_text(-290, 280, "Red = input polygon | Green = clipped result")
    draw_text(-290, 260, "Keys: i=input polygon, q=quit")

    glFlush()

def get_polygon_input():
    global polygon
    print("=" * 50)
    print("SUTHERLAND-HODGMAN POLYGON CLIPPING ALGORITHM")
    print("=" * 50)
    print(f"Window Size: [{xmin}, {ymin}] to [{xmax}, {ymax}]")
    print(f"Window Width: {xmax - xmin}, Height: {ymax - ymin}")
    print("=" * 50)

    raw_count = input("Enter number of polygon vertices: ").strip()
    try:
        num_points = int(raw_count)
    except ValueError:
        print("Invalid number entered; polygon unchanged.")
        return

    poly = []
    for i in range(num_points):
        while True:
            try:
                x = float(input(f"Enter x{i+1} coordinate: "))
                y = float(input(f"Enter y{i+1} coordinate: "))
                poly.append((x, y))
                break
            except ValueError:
                print("Please enter numeric values for x and y.")

    polygon = list(poly)
    print("\nPolygon clipping in progress...")


def keyboard(key, x, y):
    global polygon
    if key in (b'q', b'Q', b'\x1b'):
        sys.exit(0)
    if key in (b'i', b'I'):
        get_polygon_input()
        glutPostRedisplay()

def main():
    get_polygon_input()
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Sutherland Hodgman Polygon Clipping")
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-300, 300, -300, 300)
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    print("Press i to input a polygon, q to quit.")
    glutMainLoop()

if __name__ == "__main__":
    main()
