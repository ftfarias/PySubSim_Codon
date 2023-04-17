import math


def calculate_drag_force(drag_coefficient: float, radius: float, length: float, velocity: float, yaw_angle: float, pitch_angle: float) -> float:
    """
    Calculates the drag force on a submarine, modeled as a cylinder, based on the given parameters.

    Args:
        drag_coefficient (float): Drag coefficient of the submarine in water.
        radius (float): Radius of the submarine cylinder in meters.
        length (float): Length of the submarine cylinder in meters.
        velocity (float): Velocity of the submarine in m/s.
        yaw_angle (float): Yaw angle of the submarine in radians.
        pitch_angle (float): Pitch angle of the submarine in radians.

    Returns:
        float: Drag force on the submarine in Newtons.
    """

    angles_correction = math.cos(yaw_angle) * math.cos(pitch_angle)

    # Calculate the effective area of the submarine lateral, taking into account the yaw and pitch angles
    effective_area_side = radius * length * (1.0 - angles_correction)

    # Calculate the cross-sectional area of the submarine cylinder
    cross_sectional_area = math.pi * radius**2
    # Calculate the effective area of the submarine cylinder, taking into account the yaw and pitch angles
    effective_area_cylinder = cross_sectional_area * angles_correction

    # Calculate the drag force using the drag equation
    drag_force = 0.5 * drag_coefficient * \
        (effective_area_side + effective_area_cylinder) * velocity**2

    return drag_force


# class Submarine:
#     def __init__(self, mass, radius, drag_coefficient):
#         self.mass = mass # mass of the submarine in kg
#         self.radius = radius # radius of the submarine in meters
#         self.drag_coefficient = drag_coefficient # drag coefficient of the submarine in water
#         self.position = 0 # initial position of the submarine in meters
#         self.velocity = 0 # initial velocity of the submarine in m/s
#         self.acceleration = 0 # initial acceleration of the submarine in m/s^2
#         self.inertia = 0 # initial inertia of the submarine in kg*m^2/s
#         self.heading = 0 # initial heading of the submarine in radians

#     def update(self, time_step):
#         # Update acceleration based on turbine forward acceleration and drag
#         turbine_acceleration = self.acceleration
#         speed = abs(self.velocity)
#         drag_force = 0.5 * self.drag_coefficient * math.pi * self.radius**2 * speed * self.velocity
#         self.acceleration = turbine_acceleration - drag_force / self.mass

#         # Update velocity and position using Euler's method
#         self.velocity += self.acceleration * time_step
#         self.position += self.velocity * time_step

#         # Update heading based on velocity and acceleration
#         if speed > 0:
#             self.heading += math.atan2(self.acceleration, self.velocity) * time_step

#         # Update inertia based on acceleration
#         self.inertia = self.mass * self.velocity

#     def set_acceleration(self, value):
#         self.acceleration = value

#     def set_heading(self, angle):
#         self.heading = angle

#     def get_position(self):
#         return self.position

#     def get_velocity(self):
#         return self.velocity

#     def get_acceleration(self):
#         return self.acceleration

#     def get_inertia(self):
#         return self.inertia

#     def get_heading(self):
#         return self.heading

# # Example usage
# mass = 100000 # mass of the submarine in kg
# radius = 5 # radius of the submarine in meters
# drag_coefficient = 0.47 # drag coefficient of the submarine in water
# time_step = 1 # time step for discrete-time updates in seconds

# submarine = Submarine(mass, radius, drag_coefficient)

# # Set initial acceleration and heading
# submarine.set_acceleration(100) # set initial acceleration to 100 m/s^2
# submarine.set_heading(math.radians(30)) # set initial heading to 30 degrees

# # Simulate the motion of the submarine for 10 time steps
# for i in range(10):
#     submarine.update(time_step)
#     print("Time: {:.1f} s | Position: {:.2f} m | Velocity: {:.2f} m/s | Acceleration: {:.2f} m/s^2 | Inertia: {:.2f} kg*m^2/s | Heading: {:.2f} deg".format(i*time_step, submarine.get_position(), submarine.get_velocity(), submarine.get_acceleration(), submarine.get_inertia(), math.degrees(submarine.get_heading())))
