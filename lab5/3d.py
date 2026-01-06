from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

angle = 0
transform_mode = "all"

# Choose which transformation pipeline to run
def choose_mode():
    global transform_mode
    menu = (
        "1) translation",
        "2) rotation",
        "3) scaling",
        "4) shearing",
        "5) all combined",
    )
    print("Select a transformation mode:")
    for line in menu:
        print(line)
    choice = input("Enter 1-5 (default 5): ").strip() or "5"
    mapping = {
        "1": "translate",
        "2": "rotate",
        "3": "scale",
        "4": "shear",
        "5": "all",
    }
    transform_mode = mapping.get(choice, "all")
    print(f"Running mode: {transform_mode}")

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
    global angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Camera position
    gluLookAt(6, 6, 6, 0, 0, 0, 0, 1, 0)

    draw_axes()

    # ---------- ORIGINAL CUBE ----------
    glPushMatrix()
    glColor3f(1, 1, 1)
    glutWireCube(2)
    glPopMatrix()

    # ---------- TRANSFORMED CUBE ----------
    glPushMatrix()

    if transform_mode in ("translate", "all"):
        glTranslatef(1.5, 0.5, 0)

    if transform_mode in ("rotate", "all"):
        glRotatef(angle, 1, 1, 0)

    if transform_mode in ("scale", "all"):
        glScalef(1.2, 0.8, 1)

    if transform_mode in ("shear", "all"):
        shear_matrix = [
            1, 0.4, 0, 0,
            0.4, 1, 0, 0,
            0, 0, 1, 0,
            0, 0, 0, 1
        ]
        glMultMatrixf(shear_matrix)

    glColor3f(0, 1, 1)
    glutSolidCube(2)
    glPopMatrix()

    angle += 0.5
    glutSwapBuffers()

# ---------------- INIT ----------------
def init():
    glClearColor(0, 0, 0, 1)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 1, 50)
    glMatrixMode(GL_MODELVIEW)

# ---------------- MAIN ----------------
def main():
    choose_mode()
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"3D Transformations using PyOpenGL")
    init()
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
