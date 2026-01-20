from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Global variables for cube position
cube_z = -5.0
cube_size = 1.0

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
def draw_colored_cube(size):
    glBegin(GL_QUADS)
    
    # Front face (Red)
    glColor3f(1, 0, 0)
    glVertex3f(size, size, size)
    glVertex3f(-size, size, size)
    glVertex3f(-size, -size, size)
    glVertex3f(size, -size, size)
    
    # Back face (Green)
    glColor3f(0, 1, 0)
    glVertex3f(size, size, -size)
    glVertex3f(-size, size, -size)
    glVertex3f(-size, -size, -size)
    glVertex3f(size, -size, -size)
    
    # Top face (Blue)
    glColor3f(0, 0, 1)
    glVertex3f(size, size, size)
    glVertex3f(-size, size, size)
    glVertex3f(-size, size, -size)
    glVertex3f(size, size, -size)
    
    # Bottom face (Yellow)
    glColor3f(1, 1, 0)
    glVertex3f(size, -size, size)
    glVertex3f(-size, -size, size)
    glVertex3f(-size, -size, -size)
    glVertex3f(size, -size, -size)
    
    # Right face (Magenta)
    glColor3f(1, 0, 1)
    glVertex3f(size, size, size)
    glVertex3f(size, size, -size)
    glVertex3f(size, -size, -size)
    glVertex3f(size, -size, size)
    
    # Left face (Cyan)
    glColor3f(0, 1, 1)
    glVertex3f(-size, size, size)
    glVertex3f(-size, size, -size)
    glVertex3f(-size, -size, -size)
    glVertex3f(-size, -size, size)
    
    glEnd()

# Perspective Projection Display
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Camera position - Z-axis towards screen
    gluLookAt(0, 0, -10,   # Eye position (behind cube)
              0, 0, 0,     # Look-at point
              0, 1, 0)     # Up direction

    draw_axes()

    # Draw cube at user-specified Z position
    glPushMatrix()
    glTranslatef(0, 0, cube_z)
    draw_colored_cube(cube_size)
    glPopMatrix()

    glutSwapBuffers()

# ---------------- INIT ----------------
def init():
    glClearColor(0, 0, 0, 1)
    glEnable(GL_DEPTH_TEST)

    # Perspective Projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 0.1, 50)
    glMatrixMode(GL_MODELVIEW)

# Keyboard callback to move cube along Z axis
def keyboard(key, x, y):
    global cube_z
    if key == b'w' or key == b'W':
        cube_z -= 0.5  # Move closer (towards screen)
        glutPostRedisplay()
    elif key == b's' or key == b'S':
        cube_z += 0.5  # Move farther (away from screen)
        glutPostRedisplay()
    elif key == b'r' or key == b'R':
        cube_z = -5.0  # Reset position
        glutPostRedisplay()
    elif key == b'q' or key == b'Q':
        exit()

# ---------------- MAIN ----------------
def main():
    global cube_z
    
    print("\n=== Perspective Projection Visualization ===")
    print("Enter the starting Z position for the cube:")
    
    try:
        cube_z = float(input("Cube Z position (default -5): ") or "-5")
    except ValueError:
        cube_z = -5.0
    
    print(f"\nCube Z position: {cube_z}")
    print("\nKeyboard Controls:")
    print("  'W' - Move cube closer (positive Z, towards screen)")
    print("  'S' - Move cube farther (negative Z, away from screen)")
    print("  'R' - Reset to default position")
    print("  'Q' - Quit\n")
    
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Perspective Projection - PyOpenGL")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

main()
