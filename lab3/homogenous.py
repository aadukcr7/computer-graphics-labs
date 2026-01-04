from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Rectangle (Homogeneous Coordinates)
rect = [
    [20, 20, 1],
    [50, 20, 1],
    [50, 35, 1],
    [20, 35, 1]
]

# Center of rectangle for rotation
rect_center = [35, 27.5]

choice = 0
params = {}

# ---------- Matrix Multiplication ----------
def multiply_matrix(M, P):
    result = []
    for point in P:
        x = M[0][0]*point[0] + M[0][1]*point[1] + M[0][2]*point[2]
        y = M[1][0]*point[0] + M[1][1]*point[1] + M[1][2]*point[2]
        result.append([x, y, 1])
    return result

# ---------- Reshape Callback ----------
def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-200, 200, -100, 100)
    glMatrixMode(GL_MODELVIEW)

# ---------- Render Text ----------
def render_text(x, y, text):
    glRasterPos2f(x, y)
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

# ---------- Draw Axes ----------
def draw_axes():
    # Draw axis lines
    glColor3f(1, 1, 1)
    glBegin(GL_LINES)
    glVertex2f(-200, 0)
    glVertex2f(200, 0)
    glVertex2f(0, -100)
    glVertex2f(0, 100)
    glEnd()
    
    # Draw tick marks and labels for X-axis
    glBegin(GL_LINES)
    for i in range(-200, 201, 20):
        glVertex2f(i, -2)
        glVertex2f(i, 2)
    glEnd()
    
    # Draw tick marks and labels for Y-axis
    glBegin(GL_LINES)
    for i in range(-100, 101, 10):
        glVertex2f(-2, i)
        glVertex2f(2, i)
    glEnd()
    
    # Draw number labels on X-axis
    glColor3f(0.8, 0.8, 0.8)
    for i in range(-200, 201, 50):
        if i != 0:
            render_text(i - 5, -12, str(i))
    
    # Draw number labels on Y-axis
    for i in range(-100, 101, 20):
        if i != 0:
            render_text(-15, i - 4, str(i))
    
    # Draw origin label
    glColor3f(0.8, 0.8, 0.8)
    render_text(-10, -12, "O")

# ---------- Draw Rectangle ----------
def draw_shape(points, color):
    glColor3f(*color)
    glBegin(GL_POLYGON)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()

# ---------- Display ----------
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_axes()

    # Original Shape
    draw_shape(rect, (0, 1, 0))

    # Transformation Matrix
    if choice == 1:   # Translation
        tx, ty = params["tx"], params["ty"]
        T = [[1, 0, tx], [0, 1, ty], [0, 0, 1]]

    elif choice == 2: # Rotation (around object center)
        a = math.radians(params["angle"])
        cx, cy = rect_center
        # Translate to origin, rotate, translate back
        T1 = [[1, 0, -cx], [0, 1, -cy], [0, 0, 1]]
        T2 = [[math.cos(a), -math.sin(a), 0],
              [math.sin(a),  math.cos(a), 0],
              [0, 0, 1]]
        T3 = [[1, 0, cx], [0, 1, cy], [0, 0, 1]]
        
        temp = multiply_matrix(T1, rect)
        temp = multiply_matrix(T2, temp)
        transformed = multiply_matrix(T3, temp)
        draw_shape(transformed, (1, 0, 0))
        glFlush()
        return

    elif choice == 3: # Scaling (around object center)
        sx, sy = params["sx"], params["sy"]
        if sx == 0 or sy == 0:
            print("Warning: Scaling factor cannot be zero. Using 1.0")
            sx = sx if sx != 0 else 1.0
            sy = sy if sy != 0 else 1.0
        cx, cy = rect_center
        # Translate to origin, scale, translate back
        T1 = [[1, 0, -cx], [0, 1, -cy], [0, 0, 1]]
        T2 = [[sx, 0, 0], [0, sy, 0], [0, 0, 1]]
        T3 = [[1, 0, cx], [0, 1, cy], [0, 0, 1]]
        
        temp = multiply_matrix(T1, rect)
        temp = multiply_matrix(T2, temp)
        transformed = multiply_matrix(T3, temp)
        draw_shape(transformed, (1, 0, 0))
        glFlush()
        return

    elif choice == 4: # Reflection (X-axis, Y-axis, or origin)
        axis = input("Reflect on X-axis (x), Y-axis (y), or origin (o)? ").lower()
        if axis == 'x':
            T = [[1, 0, 0], [0, -1, 0], [0, 0, 1]]
        elif axis == 'y':
            T = [[-1, 0, 0], [0, 1, 0], [0, 0, 1]]
        elif axis == 'o':
            T = [[-1, 0, 0], [0, -1, 0], [0, 0, 1]]
        else:
            print("Invalid choice. Using X-axis reflection.")
            T = [[1, 0, 0], [0, -1, 0], [0, 0, 1]]

    elif choice == 5: # Shearing
        shx = params["shx"]
        T = [[1, shx, 0], [0, 1, 0], [0, 0, 1]]

    elif choice == 6: # Composite (Translate to origin -> Scale -> Rotate -> Translate back -> Translate -> Shear)
        tx, ty = params["tx"], params["ty"]
        sx, sy = params["sx"], params["sy"]
        shx = params["shx"]
        a = math.radians(params["angle"])
        
        if sx == 0 or sy == 0:
            print("Warning: Scaling factor cannot be zero. Using 1.0")
            sx = sx if sx != 0 else 1.0
            sy = sy if sy != 0 else 1.0

        cx, cy = rect_center
        # Correct order: Translate to origin -> Scale -> Rotate -> Translate back -> Translate -> Shear
        T_trans_to_origin = [[1, 0, -cx], [0, 1, -cy], [0, 0, 1]]
        T_scale = [[sx, 0, 0], [0, sy, 0], [0, 0, 1]]
        T_rotate = [[math.cos(a), -math.sin(a), 0],
                    [math.sin(a),  math.cos(a), 0],
                    [0, 0, 1]]
        T_trans_back = [[1, 0, cx], [0, 1, cy], [0, 0, 1]]
        T_translate = [[1, 0, tx], [0, 1, ty], [0, 0, 1]]
        T_shear = [[1, shx, 0], [0, 1, 0], [0, 0, 1]]

        temp = multiply_matrix(T_trans_to_origin, rect)
        temp = multiply_matrix(T_scale, temp)
        temp = multiply_matrix(T_rotate, temp)
        temp = multiply_matrix(T_trans_back, temp)
        temp = multiply_matrix(T_translate, temp)
        transformed = multiply_matrix(T_shear, temp)

        draw_shape(transformed, (1, 0, 0))
        glFlush()
        return

    transformed = multiply_matrix(T, rect)
    draw_shape(transformed, (1, 0, 0))
    glFlush()

# ---------- Main ----------
def main():
    global choice, params

    print("\n2D TRANSFORMATIONS (HOMOGENEOUS COORDINATES)")
    print("1. Translation")
    print("2. Rotation")
    print("3. Scaling")
    print("4. Reflection (x / y / origin)")
    print("5. Shearing")
    print("6. Composite Transformation")

    try:
        choice = int(input("Enter choice (1-6): "))
        if choice < 1 or choice > 6:
            print("Invalid choice. Using translation by default.")
            choice = 1
    except ValueError:
        print("Invalid input. Using translation by default.")
        choice = 1

    try:
        if choice == 1:
            params["tx"] = float(input("Enter tx: "))
            params["ty"] = float(input("Enter ty: "))
        elif choice == 2:
            params["angle"] = float(input("Enter angle (degrees): "))
        elif choice == 3:
            params["sx"] = float(input("Enter sx: "))
            params["sy"] = float(input("Enter sy: "))
        elif choice == 5:
            params["shx"] = float(input("Enter shear factor: "))
        elif choice == 6:
            params["tx"] = float(input("Enter tx: "))
            params["ty"] = float(input("Enter ty: "))
            params["angle"] = float(input("Enter angle (degrees): "))
            params["sx"] = float(input("Enter sx: "))
            params["sy"] = float(input("Enter sy: "))
            params["shx"] = float(input("Enter shear factor: "))
    except ValueError:
        print("Invalid input. Using default parameters.")

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"2D Transformations using Homogeneous Coordinates")
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(-200, 200, -100, 100)
    glMatrixMode(GL_MODELVIEW)
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()

main()
