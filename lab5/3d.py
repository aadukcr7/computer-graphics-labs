from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Rotation angle (fixed at 90 degrees)
angle = 90
transform_mode = "rotate"

# Choose which transformation to apply
def choose_mode():
    global transform_mode
    menu = (
        "1) Translation",
        "2) Rotation (90 degrees)",
        "3) Scaling",
        "4) Shearing",
    )
    print("\n=== 3D Transformations Menu ===")
    for line in menu:
        print(line)
    choice = input("Enter 1-4 (default 2): ").strip() or "2"
    mapping = {
        "1": "translate",
        "2": "rotate",
        "3": "scale",
        "4": "shear",
    }
    transform_mode = mapping.get(choice, "rotate")
    print(f"\nSelected transformation: {transform_mode}\n")

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

# Draw colored cube
def draw_colored_cube():
    glBegin(GL_QUADS)
    
    # Front face (Red)
    glColor3f(1, 0, 0)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, -1, 1)
    glVertex3f(1, -1, 1)
    
    # Back face (Green)
    glColor3f(0, 1, 0)
    glVertex3f(1, 1, -1)
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    
    # Top face (Blue)
    glColor3f(0, 0, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    
    # Bottom face (Yellow)
    glColor3f(1, 1, 0)
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    
    # Right face (Magenta)
    glColor3f(1, 0, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, 1)
    
    # Left face (Cyan)
    glColor3f(0, 1, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, -1, 1)
    
    glEnd()

# Display function
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Camera position
    gluLookAt(6, 6, 6, 0, 0, 0, 0, 1, 0)

    draw_axes()

    # Apply selected transformation
    glPushMatrix()

    if transform_mode == "translate":
        glTranslatef(1.5, 0.5, 0)

    elif transform_mode == "rotate":
        glRotatef(angle, 1, 1, 0)

    elif transform_mode == "scale":
        glScalef(1.2, 0.8, 1)

    elif transform_mode == "shear":
        shear_matrix = [
            1, 0.4, 0, 0,
            0.4, 1, 0, 0,
            0, 0, 1, 0,
            0, 0, 0, 1
        ]
        glMultMatrixf(shear_matrix)

    draw_colored_cube()
    glPopMatrix()

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
    glutMainLoop()

if __name__ == "__main__":
    main()
