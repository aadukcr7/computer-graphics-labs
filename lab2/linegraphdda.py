from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# -------- Config --------
WIDTH, HEIGHT = 800, 600
PADDING_X, PADDING_Y = 60, 50

data = [20, 60, 40, 80, 30, 70]

def dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))

    # Handle zero-length segment to avoid division by zero
    if steps == 0:
        return [round(x1)], [round(y1)]

    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x1, y1
    xp, yp = [], []

    for _ in range(steps + 1):
        xp.append(round(x))
        yp.append(round(y))
        x += x_inc
        y += y_inc

    return xp, yp

def map_to_screen(x_idx, y_val, n_points, y_min, y_max):
    # Map x index [0..n-1] to screen X with padding
    x_min_screen = PADDING_X
    x_max_screen = WIDTH - PADDING_X
    y_min_screen = PADDING_Y
    y_max_screen = HEIGHT - PADDING_Y

    # Linear mapping for X
    if n_points <= 1:
        sx = (x_min_screen + x_max_screen) // 2
    else:
        sx = x_min_screen + (x_idx / (n_points - 1)) * (x_max_screen - x_min_screen)

    # Linear mapping for Y (data range to screen range)
    if y_max == y_min:
        sy = (y_min_screen + y_max_screen) / 2
    else:
        t = (y_val - y_min) / (y_max - y_min)
        sy = y_min_screen + t * (y_max_screen - y_min_screen)

    return int(round(sx)), int(round(sy))

def draw_axes(y_min, y_max):
    glColor3f(0.6, 0.6, 0.6)
    glLineWidth(1.0)

    # X axis
    glBegin(GL_LINES)
    glVertex2i(PADDING_X, PADDING_Y)
    glVertex2i(WIDTH - PADDING_X, PADDING_Y)
    glEnd()

    # Y axis
    glBegin(GL_LINES)
    glVertex2i(PADDING_X, PADDING_Y)
    glVertex2i(PADDING_X, HEIGHT - PADDING_Y)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    n = len(data)
    y_min, y_max = min(data), max(data)

    # Draw axes
    draw_axes(y_min, y_max)

    # Draw lines using DDA per segment (white pixels)
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(2.0)
    glBegin(GL_POINTS)
    for i in range(n - 1):
        x1, y1 = map_to_screen(i,     data[i],     n, y_min, y_max)
        x2, y2 = map_to_screen(i + 1, data[i + 1], n, y_min, y_max)
        xp, yp = dda(x1, y1, x2, y2)
        for j in range(len(xp)):
            glVertex2i(xp[j], yp[j])
    glEnd()

    # Optionally: overlay a smooth line strip for visual clarity
    glColor3f(0.2, 0.7, 1.0)
    glLineWidth(2.0)
    glBegin(GL_LINE_STRIP)
    for i in range(n):
        sx, sy = map_to_screen(i, data[i], n, y_min, y_max)
        glVertex2i(sx, sy)
    glEnd()

    # Draw scatter points (red)
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(6.0)
    glBegin(GL_POINTS)
    for i in range(n):
        sx, sy = map_to_screen(i, data[i], n, y_min, y_max)
        glVertex2i(sx, sy)
    glEnd()

    glFlush()

def reshape(w, h):
    # Keep projection consistent if window is resized
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, WIDTH, 0, HEIGHT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Line Graph using DDA")

    glClearColor(0.0, 0.0, 0.0, 0.0)

    # Set up 2D orthographic projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, WIDTH, 0, HEIGHT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()

if __name__ == "__main__":
    main()
