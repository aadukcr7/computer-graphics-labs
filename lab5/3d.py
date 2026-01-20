from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

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

# Draw cube wireframe (for original/before state)
def draw_wireframe_cube():
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glLineWidth(2.0)
    glColor3f(0.5, 0.5, 0.5)  # Gray wireframe
    
    glBegin(GL_QUADS)
    
    # Front face
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, -1, 1)
    glVertex3f(1, -1, 1)
    
    # Back face
    glVertex3f(1, 1, -1)
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    
    # Top face
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    
    # Bottom face
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    
    # Right face
    glVertex3f(1, 1, 1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, 1)
    
    # Left face
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, -1, 1)
    
    glEnd()
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glLineWidth(1.0)

# Display function
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Camera position
    gluLookAt(6, 6, 6, 0, 0, 0, 0, 1, 0)

    draw_axes()

    # Draw BEFORE: Original cube as wireframe
    glPushMatrix()
    draw_wireframe_cube()
    glPopMatrix()

    # Draw AFTER: Transformed cube with colors
    glPushMatrix()

    if transform_mode == "translate":
        # Translation matrix: move by (1.5, 0.5, 0)
        translation_matrix = [
            1, 0, 0, 0,
            0, 1, 0, 0,
            0, 0, 1, 0,
            1.5, 0.5, 0, 1
        ]
        glMultMatrixf(translation_matrix)

    elif transform_mode == "rotate":
        # Rotation matrix: 90 degrees around axis (1, 1, 0)
        # Normalize the axis
        ax, ay, az = 1, 1, 0
        length = math.sqrt(ax**2 + ay**2 + az**2)
        ax, ay, az = ax/length, ay/length, az/length
        
        # Convert angle to radians
        rad = math.radians(angle)
        c = math.cos(rad)
        s = math.sin(rad)
        t = 1 - c
        
        # Rodrigues' rotation formula in matrix form
        rotation_matrix = [
            t*ax*ax + c,    t*ax*ay + s*az, t*ax*az - s*ay, 0,
            t*ax*ay - s*az, t*ay*ay + c,    t*ay*az + s*ax, 0,
            t*ax*az + s*ay, t*ay*az - s*ax, t*az*az + c,    0,
            0,              0,              0,              1
        ]
        glMultMatrixf(rotation_matrix)

    elif transform_mode == "scale":
        # Scaling matrix: scale by (1.2, 0.8, 1)
        scaling_matrix = [
            2, 0, 0, 0,
            0, 1.8, 0, 0,
            0, 0, 1, 0,
            0, 0, 0, 1
        ]
        glMultMatrixf(scaling_matrix)

    elif transform_mode == "shear":
        # Shearing matrix
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
