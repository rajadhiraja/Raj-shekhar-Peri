from vpython import *

rocket_parts = []

#create an empty list to store rocket parts
height = 0.5

#set the height of the rocket
rocket_parts.append(cylinder(pos=vector(0,0,0), color=color.red, size=vector(height,0.1,0.1), axis=vector(0,1,0), make_trail=True))

#add a cylinder to the list of the rocket parts
rocket_parts.append(cone(pos=rocket_parts[0].pos + rocket_parts[0].axis * rocket_parts[0].size.x, color=color.red, size=vector(rocket_parts[0].size.y, rocket_parts[0].size.y, rocket_parts[0].size.y), axis=vector(0,1,0)))

#add a cone to the list of rocket parts
rocket_parts.append(triangle(v0=vertex(pos=rocket_parts[0].pos + 0.5*rocket_parts[0].size.y*vector(1,0,0), color=color.red),
                            v1=vertex(pos=rocket_parts[0].pos + 1.5*rocket_parts[0].size.y*vector(1,0,0), color=color.red),
                            v2=vertex(pos=rocket_parts[0].pos + 0.5*rocket_parts[0].size.y*vector(1,2,0), color=color.red)))

#add a triangular face to the list of rocket parts
rocket_parts.append(triangle(v0=vertex(pos=rocket_parts[0].pos + 0.5*rocket_parts[0].size.y*vector(-1,0,0), color=color.red),
                            v1=vertex(pos=rocket_parts[0].pos + 1.5*rocket_parts[0].size.y*vector(-1,0,0), color=color.red),
                            v2=vertex(pos=rocket_parts[0].pos + 0.5*rocket_parts[0].size.y*vector(-1,2,0), color=color.red)))

#add another triangular face to the list of rocket parts
rocket_parts.append(triangle(v0=vertex(pos=rocket_parts[0].pos + 0.5*rocket_parts[0].size.y*vector(0,0,1), color=color.red),
                            v1=vertex(pos=rocket_parts[0].pos + 1.5*rocket_parts[0].size.y*vector(0,0,1), color=color.red),
                            v2=vertex(pos=rocket_parts[0].pos + 1.5*rocket_parts[0].size.y*vector(0,2,1), color=color.red)))

#add another triangular face to the list of rocket parts
rocket_parts.append(triangle(v0=vertex(pos=rocket_parts[0].pos + 0.5*rocket_parts[0].size.y*vector(0,0,-1), color=color.red),
                            v1=vertex(pos=rocket_parts[0].pos + 1.5*rocket_parts[0].size.y*vector(0,0,-1), color=color.red),
                            v2=vertex(pos=rocket_parts[0].pos + 0.5*rocket_parts[0].size.y*vector(0,2,-1), color=color.red)))

#add another triangular face to the list of rocket parts
rocket = compound(rocket_parts, pos=vector(0,0,0))

#create a compound object from the list of rocket parts
rocket.velocity = vector(0,0,0)
#set the initial velocity of the rocket

rocket.mass = 100.0
#set the mass of the rocket

rocket.fuel_mass = 10.0
#set the mass of the fuel

rocket.angle = 0
#set the initial angle of the rocket

attach_trail(rocket)
#attach a trail to the rocket to show its path

initial_mass = rocket.mass + rocket.fuel_mass
#calculate the initial total mass of the fuel for later use

graph(fast=True)
#create a graph to show the altitude of the rocket
r_pos = gcurve(color=color.red)
#graph for position of the rocket

exhaust_velocity = vector(0,100,0)
#velocity of the expelled exhaust gases

mdot = 1.0
#rate of mass loss per time

dt = 0.001
#time step for simulation

t = 0
#initial time

scene.camera.follow(rocket)
#set camera to follow the rocket

earth = sphere(pos=vector(0,-height*100,0), radius=10, color=color.blue)
earth.mass = 1000

ground = box(pos=vector(0,-height/2-0.05,0), color=vector(0.8,0.8,0.8), size=vector(2,0.01,2))

grav = -1 * earth.mass / earth.pos.y**2
#create a planet object to simulate gravity

while rocket.fuel_mass > 0:
    rate(10000)
    
    dm = mdot * dt
    #Amount of mass loss in time dt.
    
    if rocket.pos.y > 0:
        force = (rocket.mass + rocket.fuel_mass) * vector(0, grav, 0)
    else:
        force = vector(0, 0, 0)
    
    rocket.velocity = rocket.velocity + dm / (rocket.mass + rocket.fuel_mass) * (-exhaust_velocity) + force / (rocket.mass + rocket.fuel_mass) * dt
    rocket.pos = rocket.pos + rocket.velocity * dt
    rocket.fuel_mass = rocket.fuel_mass - dm
    rocket.opacity = rocket.fuel_mass / initial_mass
    t = t + dt
    r_pos.plot(pos=(t, rocket.pos.y))

percentage_decrease = (1 - rocket.velocity.y / (mag(exhaust_velocity) * log(initial_mass / rocket.mass))) * 100
print(f"{percentage_decrease}% decrease in speed due to external forces during ascent")
