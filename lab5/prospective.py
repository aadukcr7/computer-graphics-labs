from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# ---------------- AXES ----------------
def draw_axes():
    glBegin(GL_LINES)

    # X-axis (Red)
    glColor3f(1, 0, 0)
    glVertex3f(-5, 0, 0)
    glVertex3f(5, 0, 0)

    # Y-axis (Green)
    glColor3f(0, 1, 0)
    glVertex3f(0, -5, 0)
    glVertex3f(0, 5, 0)

    # Z-axis (Blue)
    glColor3f(0, 0, 1)
    glVertex3f(0, 0, -5)
    glVertex3f(0, 0, 5)

    glEnd()

# ---------------- DISPLAY ----------------
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Camera position (Perspective View)
    gluLookAt(5, 5, 8,   # Eye position
              0, 0, 0,   # Look-at point
              0, 1, 0)   # Up direction

    draw_axes()

    # Cube nearer to camera
    glPushMatrix()
    glTranslatef(-1.5, 0, 0)
    glColor3f(0, 1, 1)
    glutSolidCube(1.5)
    glPopMatrix()

    # Cube farther from camera
    glPushMatrix()
    glTranslatef(2, 0, -4)
    glColor3f(1, 0, 0)
    glutWireCube(1.5)
    glPopMatrix()

    glutSwapBuffers()

# ---------------- INIT ----------------
def init():
    glClearColor(0, 0, 0, 1)
    glEnable(GL_DEPTH_TEST)

    # Perspective Projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 1, 50)
    glMatrixMode(GL_MODELVIEW)

# ---------------- MAIN ----------------
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Perspective Projection - PyOpenGL")
    init()
    glutDisplayFunc(display)
    glutMainLoop()

main()
