from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

choice = 0
params = {}

# ---------------- Draw Axis ----------------
def draw_axes():
    glColor3f(1, 1, 1)
    glBegin(GL_LINES)
    glVertex2f(-500, 0)
    glVertex2f(500, 0)
    glVertex2f(0, -500)
    glVertex2f(0, 500)
    glEnd()

# ---------------- Draw Square ----------------
def draw_square():
    glBegin(GL_POLYGON)
    glVertex2f(50, 50)
    glVertex2f(150, 50)
    glVertex2f(150, 150)
    glVertex2f(50, 150)
    glEnd()

# ---------------- Display ----------------
def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw axes
    draw_axes()

    # Original object
    glColor3f(0, 1, 0)
    draw_square()

    # Transformed object
    glPushMatrix()
    glColor3f(1, 0, 0)

    if choice == 1:   # Translation
        glTranslatef(params["tx"], params["ty"], 0)

    elif choice == 2: # Rotation
        glTranslatef(100, 100, 0)
        glRotatef(params["angle"], 0, 0, 1)
        glTranslatef(-100, -100, 0)

    elif choice == 3: # Scaling
        glScalef(params["sx"], params["sy"], 1)

    elif choice == 4: # Reflection
        if params["axis"] == 'x':
            glScalef(1, -1, 1)
        elif params["axis"] == 'y':
            glScalef(-1, 1, 1)
        else:  # origin
            glScalef(-1, -1, 1)

    elif choice == 5: # Shearing
        shx = params["shx"]
        shy = params["shy"]
        shear_matrix = [
            1,  shy, 0, 0,
            shx, 1,   0, 0,
            0,   0,   1, 0,
            0,   0,   0, 1
        ]
        glMultMatrixf(shear_matrix)

    elif choice == 6: # Composite
        glTranslatef(params["tx"], params["ty"], 0)
        glRotatef(params["angle"], 0, 0, 1)
        glScalef(params["sx"], params["sy"], 1)
        shx = params["shx"]
        shy = params["shy"]
        shear_matrix = [
            1,  shy, 0, 0,
            shx, 1,   0, 0,
            0,   0,   1, 0,
            0,   0,   0, 1
        ]
        glMultMatrixf(shear_matrix)

    draw_square()
    glPopMatrix()
    glFlush()

# ---------------- Main ----------------
def main():
    global choice, params

    print("\nUSER-DRIVEN 2D TRANSFORMATIONS")
    print("1. Translation")
    print("2. Rotation")
    print("3. Scaling")
    print("4. Reflection")
    print("5. Shearing")
    print("6. Composite Transformation")

    choice = int(input("Enter choice (1-6): "))

    if choice == 1:
        params["tx"] = float(input("Enter translation in X: "))
        params["ty"] = float(input("Enter translation in Y: "))

    elif choice == 2:
        params["angle"] = float(input("Enter rotation angle (degrees): "))

    elif choice == 3:
        params["sx"] = float(input("Enter scaling factor in X: "))
        params["sy"] = float(input("Enter scaling factor in Y: "))

    elif choice == 4:
        params["axis"] = input("Reflect about x / y / origin: ").lower()

    elif choice == 5:
        params["shx"] = float(input("Enter shear factor in X: "))
        params["shy"] = float(input("Enter shear factor in Y: "))

    elif choice == 6:
        params["tx"] = float(input("Enter translation in X: "))
        params["ty"] = float(input("Enter translation in Y: "))
        params["angle"] = float(input("Enter rotation angle: "))
        params["sx"] = float(input("Enter scaling factor in X: "))
        params["sy"] = float(input("Enter scaling factor in Y: "))
        params["shx"] = float(input("Enter shear factor in X: "))
        params["shy"] = float(input("Enter shear factor in Y: "))

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"User Driven 2D Transformations")
    glClearColor(0, 0, 0, 0)
    gluOrtho2D(-300, 300, -300, 300)
    glutDisplayFunc(display)
    glutMainLoop()

main()
