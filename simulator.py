from vpython import sphere, vector, color, scene, rate, curve

# Set up the VPython scene
scene.title = "Spacetime Warping Simulation"
scene.width = 800
scene.height = 600
scene.background = color.black

# Parameters for the spheres
spheres = [
    {"radius": 0.2, "position": vector(-1, 0, 0), "color": color.red},    # Sphere 1
    {"radius": 0.4, "position": vector(0, 0, 0), "color": color.green},   # Sphere 2
    {"radius": 0.6, "position": vector(1, 0, 0), "color": color.blue},    # Sphere 3
]

# Create spheres with varying radii and positions
sphere_objects = []
for sphere_params in spheres:
    s = sphere(
        pos=sphere_params["position"],
        radius=sphere_params["radius"],
        color=sphere_params["color"],
        emissive=True,
    )
    sphere_objects.append(s)

# Create a spacetime grid
grid_size = 20  # Number of lines in the grid
grid_spacing = 0.1  # Spacing between grid lines
grid_lines = []

# Create the grid lines for spacetime visualization
for i in range(-grid_size, grid_size + 1):
    grid_lines.append(
        curve(color=color.white, radius=0.01)
    )  # Add horizontal lines
    grid_lines.append(
        curve(color=color.white, radius=0.01)
    )  # Add vertical lines

# Update function for spacetime deformation
def update_spacetime(t):
    for j, line in enumerate(grid_lines):
        if j % 2 == 0:  # Horizontal lines
            z = grid_spacing * (j // 2 - grid_size)
            line.clear()
            for x in range(-grid_size, grid_size + 1):
                deformation = sum(
                    -s.radius / ((x - s.pos.x) ** 2 + z ** 2 + 0.1)
                    for s in sphere_objects
                )
                line.append(vector(grid_spacing * x, deformation, z))
        else:  # Vertical lines
            x = grid_spacing * ((j - 1) // 2 - grid_size)
            line.clear()
            for z in range(-grid_size, grid_size + 1):
                deformation = sum(
                    -s.radius / ((x - s.pos.x) ** 2 + z ** 2 + 0.1)
                    for s in sphere_objects
                )
                line.append(vector(x, deformation, grid_spacing * z))

# Animation loop
t = 0
while True:
    rate(30)  # Limit to 30 frames per second
    t += 0.1
    update_spacetime(t)