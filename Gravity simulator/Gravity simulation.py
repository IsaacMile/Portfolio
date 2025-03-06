from vpython import * #importing Vpython, the main module used in this code
import math #importing math library for trig functions
import time

#-----Variable Declaration----------------------------------------------------------------------------------------
userzoom = True #allows the user to zoom in
userspin = True #allows the user to spin the camera 
userpan = False # allows the user to pan the camera
scene.autoscale = True  #sets the autoscaling to true to automatically control the camera position 
radScaling = 5*10**2
trailScaling = 0.5

sun = sphere(name = "Sun", pos=vector(0,0,0), color = vector(0.91, 0.51, 0), radius = 69.634*10**8, mass = 1.9885*10**30, 
             velocity = vector(0,0,0))
#creating a sphere to represent the sun, no orbital incline as sun is an orbital center not orbiting object
mercury = sphere(name = "Mercury", pos=vector(0,0,0), color=vector(0.9,0.7,0.2), radius = radScaling*2.4397*10**6, mass = 0.3285*10**24, velocity = vector(0,0,0), 
                 orbitIncline = 7.004*math.pi/180, aphelion = 69.818*10**9, perihelion = 46*10**9, aphelionAngle=math.pi*3/4, 
                 make_trail = False, trail_radius = radScaling*trailScaling*2.4397*10**6, retain = 10**3, orbiting = sun)
#creating a sphere to represent mercury
venus = sphere(name = "Venus", pos=vector(0,0,0), color=vector(1,0.8,0.4), radius = radScaling*6.0518*10**6, mass = 4.867*10**24, velocity = vector(0,0,0), 
              orbitIncline = 3.395*math.pi/180, aphelion = 108.941*10**9, perihelion = 107.480*10**9, aphelionAngle=math.pi/6,
              make_trail = False, trail_radius = radScaling*trailScaling*6.0518*10**6, retain = 10**3, orbiting = sun)
#creating a sphere to represent venus 
earth = sphere(name = "Earth", pos=vector(0,0,0), color = vector(0, 0.8, 0.9), radius = radScaling*6.371*10**6, mass = 5.972*10**24, 
               velocity = vector(0,0,0), orbitIncline = 0, aphelion = 152.1*10**9, perihelion = 147.095*10**9, aphelionAngle=0, 
               make_trail = False, trail_radius = radScaling*trailScaling*6.371*10**6, retain = 10**3, orbiting = sun)
#creating a sphere to represent the earth
mars = sphere(name = "Mars", pos=vector(0,0,0), color = vector(0.8, 0.4, 0.2), radius = radScaling*3.3895*10**6, mass = 0.639*10**24, 
               velocity = vector(0,0,0), orbitIncline = 1.85*math.pi/180, aphelion = 249.261*10**9, perihelion = 206.650*10**9, aphelionAngle=math.pi/3, 
               make_trail = False, trail_radius = radScaling*trailScaling*3.3895*10**6, retain = 10**3, orbiting = sun)
#creating a sphere to represent mars
jupiter = sphere(name = "Jupiter", pos=vector(0,0,0), color = vector(0.8, 0.4, 0.2), radius = radScaling*69.911*10**6, mass = 1898.13*10**24, 
               velocity = vector(0,0,0), orbitIncline = 1.304*math.pi/180, aphelion = 816.363*10**9, perihelion = 740.595*10**9, aphelionAngle=math.pi*3/8, 
               make_trail = False, trail_radius = radScaling*trailScaling*69.911*10**6, retain = 10**3, orbiting = sun)
#creating a sphere to represent jupiter
saturn = sphere(name = "Saturn", pos=vector(0,0,0), color = vector(1, 0.8, 0.4), radius = radScaling*58.232*10**6, mass = 568.32*10**24, 
               velocity = vector(0,0,0), orbitIncline = 2.486*math.pi/180, aphelion = 1506.527*10**9, perihelion = 1357.554*10**9, aphelionAngle=math.pi*5/4, 
               make_trail = False, trail_radius = radScaling*trailScaling*58.232*10**6, retain = 10**3, orbiting = sun)
#creating a sphere to represent saturn
uranus = sphere(name = "Uranus", pos=vector(0,0,0), color = vector(0.6, 0.8, 0.9), radius = radScaling*25.362*10**6, mass = 86.81*10**24, 
               velocity = vector(0,0,0), orbitIncline = 0.770*math.pi/180, aphelion = 3001.390*10**9, perihelion = 2732.696*10**9, aphelionAngle=math.pi*5/4, 
               make_trail = False, trail_radius = radScaling*trailScaling*25.362*10**6, retain = 10**3, orbiting = sun)
#creating a sphere to represent uranus
neptune = sphere(name = "Neptune", pos=vector(0,0,0), color = vector(0, 0.2, 0.8), radius = radScaling*24.622*10**6, mass = 102.4*10**24, 
               velocity = vector(0,0,0), orbitIncline = 1.770*math.pi/180, aphelion = 4558.857*10**9, perihelion = 4471.05*10**9, aphelionAngle=math.pi/2,
               make_trail = False, trail_radius = radScaling*trailScaling*24.622*10**6, retain = 10**3, orbiting = sun)
#creating a sphere to represent neptune
moon = sphere(name = "Moon", pos=vector(0,0,0), color=vector(0.8,0.8,0.8), radius = radScaling*1.7374*10**6, mass = 0.0734767309*10**24, velocity = vector(0,0,0), 
              orbitIncline = 5.1*math.pi/180, aphelion = 405.696*10**6, perihelion =363.3*10**6, aphelionAngle=math.pi,
              make_trail = False, trail_radius = radScaling*trailScaling*6.371*10**6, retain = 10**3, orbiting = earth)
#creating a sphere to represent the moon

'''Vpython attributes: (standard physics units)
name: tells the program the name of the object
color: RGB, controls colour of object
pos: position vector of object, initial assigned later 
radius: controls the radius of the sphere, all increased by a factor of 10^2 apart from sun which is 10^1 due to its real size
mass: mass of the object, used in calculations
velocity: velocity of the object
orbitInlcine: inclination of orbit in radians, relative to the earth
aphelion: the furthest point of a elliptical orbit
perihelion: the closest point of an elliptical orbit
aphelionAngle: controls where on the xy plane the aphelion of a planet is in radians
make_trail: Vpython attribute telling the object to make a trail as it moves
trail_radius: controls the radius of the trail made
retain: controls how many trail points are retained at any one time
orbiting: holds a reference to the object that this object is orbiting. 
'''
#creating a label for all of the objects 
sunLabel = label(pos=sun.pos, text="Sun", xoffset=20, yoffset=20)
mercuryLabel = label(pos=mercury.pos, text="Mercury", xoffset=20, yoffset=20)
venusLabel = label(pos=venus.pos, text="Venus", xoffset=20, yoffset=20)
earthLabel = label(pos=earth.pos, text="Earth", xoffset=20, yoffset=20)
marsLabel = label(pos=mars.pos, text="Mars", xoffset=20, yoffset=20)
jupiterLabel = label(pos=jupiter.pos, text="Jupiter", xoffset=20, yoffset=20)
saturnLabel = label(pos=saturn.pos, text="Saturn", xoffset=20, yoffset=20)
uranusLabel = label(pos=uranus.pos, text="Uranus", xoffset=20, yoffset=20)
neptuneLabel = label(pos=neptune.pos, text="Neptune", xoffset=20, yoffset=20)
moonLabel = label(pos=moon.pos, text="Moon", xoffset=20, yoffset=20)

OrbitingObjects = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, moon] #array to store all objects that orbit, 
#must be in order of orbatal priority (e.g. earth before moon)
astralBodies = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, moon] #array to store all objects
objectLabels = [sunLabel, mercuryLabel, venusLabel, earthLabel, marsLabel, jupiterLabel, saturnLabel, uranusLabel, neptuneLabel, moonLabel]
#array of all labels to allow their positons to be updated
astralBodiesString = ["sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Moon"]
#array of all the items in astral bodies as strings for user interaction

G = 6.67*10**-11    #gravitational constant
focus = sun        #Camera focus
timeConstant = 100   #controls how many seconds per cycle
pathLength = 5*10**7 #controls the length of the paths 
changingObject = earth

#-----Calculation based functions--------------------------------------------------------------------------------
def initialVelocity(G, OrbitingObject):
    if OrbitingObject.aphelion != OrbitingObject.perihelion: #if statement to avoid /0
        speed = sqrt((G*OrbitingObject.orbiting.mass)* 
                (2/(mag(OrbitingObject.orbiting.pos-OrbitingObject.pos))-1/((OrbitingObject.aphelion + OrbitingObject.perihelion)/2))) 
            #declared the velocity magnitude using v =root(GM(2/r - 1/a))
    else:   #if aphelion and perihelion are equal
        speed = sqrt(G*OrbitingObject.orbiting.mass/OrbitingObject.aphelion) #calculation for circular orbit 
    direction = norm(cross((OrbitingObject.pos - OrbitingObject.orbiting.pos), vector(0,0,1))) #finding unit vector of direction of initial velocity 
    InitialVelocity = (vector(math.cos(OrbitingObject.orbitIncline)*speed*direction.x, 
                             math.cos(OrbitingObject.orbitIncline)*speed*direction.y, math.sin(OrbitingObject.orbitIncline)*speed)
                       +OrbitingObject.orbiting.velocity)
                            #the components of the initial velocity accounting for magnitude, orbital inclination and direction 
    return InitialVelocity

def accelerating(G, time, ActingObject, MovingObject): 
    #function for acceleration due to the graviational force of acting object on moving object
    forceMag = (G*ActingObject.mass*MovingObject.mass)/(mag(ActingObject.pos-MovingObject.pos))**2 #F=Gm1m2/r^2 equation
    direction = norm(ActingObject.pos - MovingObject.pos) #calculate the unit vector for the direction of the force
    MovingObject.velocity += (time*forceMag*direction/MovingObject.mass) #multiplied by time due to v=a/t 
    #calculating the velocity of the Moving object by adding it to the accelration from a=f/m
    return MovingObject.velocity

def dynamicPathLength(Object, pathLength): #used to calculate the path length while the program is running 
    Object.retain = pathLength/mag(Object.velocity) 
    #the retain should be proportional to the pathLength but inversely proportional to the objects velocity
    return Object.retain

def startup(OrbitingObjects, G):
    for i in range(len(OrbitingObjects)): #for loop for all objects that orbit another object
        OrbitingObjects[i].pos = (vector(math.cos(OrbitingObjects[i].aphelionAngle)*OrbitingObjects[i].aphelion, 
                                        math.sin(OrbitingObjects[i].aphelionAngle)*OrbitingObjects[i].aphelion, 0) 
                                        + OrbitingObjects[i].orbiting.pos)
                                    #calculating initial position using aphelionAngle
        time.sleep(0.1) #small time delay to prevent trails from 0,0,0
        OrbitingObjects[i].velocity = initialVelocity(G, OrbitingObjects[i]) #calling initialVelocity for every planet
        OrbitingObjects[i].make_trail = True #enabling trails once object is in the correct position
        OrbitingObjects[i].clear_trail()

#-----User interactivity - changable variable functions--------------------------------------------------------
def focusChange(menu): #procedure to change 
    global focus #variables used in procedure
    focus = astralBodies[menu.index] #the new focus = the astral bodies item in the index position of the 

def timeChange(slider): #procedure to change the time variable using the slider
    global timeConstant #passing the time varibale into the procedure  
    timeConstant = slider.value #setting the time constant to the slider value 
    
def pathLengthChange(slider): #procedure to change the path length variable 
    global pathLength #passing the path length variabe into the procedure 
    pathLength = slider.value*10**6 #assigning the path length variable to the slider variable, 
                                    #multiplied by 10^6 for the correct order of magnitude
    
def radiusScalingChange(slider): #procedure to change the radius scaling for all the planets 
    global radScaling, astralBodies #passing variables into procedure
    radScalingBefore = radScaling #storing the previous value for radius scaling to be used in for loop
    radScaling = slider.value*10**1 #assiging new value of the radScaling 
    for i in range(len(astralBodies)): #for every planet, using i as index
        astralBodies[i].radius = astralBodies[i].radius*radScaling/radScalingBefore 
        #changed the radius. divide by the rad scaling before to avoid the radius growing every time the procedure is run 
        astralBodies[i].trail_radius = astralBodies[i].trail_radius*radScaling/radScalingBefore
        #changing the trail radius to maintain the ration between the trail radius and radius

def trailScalingChange(slider): #procedure to change the trail radius scaling for all planets 
    global astralBodies, trailScaling #passes the variables into the procedure
    trailScalingBefore = trailScaling #storing the previous value for trail radius scaling to be used in for loop
    trailScaling = slider.value*10**-2 #assigns the new value for trail Scaling, *10^-2 to get into correct order of magnitude
    for i in range(len(astralBodies)): #for every planet, using i as index
        astralBodies[i].trail_radius = astralBodies[i].trail_radius*trailScaling/trailScalingBefore
        #assigns new trail radius. divide by trail scaling before to avoid radius growing every time procedure is run 

def labelToggle(checkbox): #checkbox to toggle the lables of all planets
    global objectLabels #pass object labels array into procedure
    if checkbox.checked == True:
        for i in range(len(objectLabels)): #for every label: swap the boolean value visible
            objectLabels[i].visible = True
    elif  checkbox.checked == False:
        for i in range(len(objectLabels)): #for every label: swap the boolean value visible
            objectLabels[i].visible = False

def Gchange(input): #procedure to change the value for G
    global G #pass the value of G into the procedure
    if (type(input.number) == float or type(input.number) == int) and (input.number <= 100 and input.number >= 0.01): 
        #Validate data type of input.number and the size to stop the user from entering an extremely large number 
        G = input.number*10**-11 #change the value of G to the new value, user is prompted with *10^-11

def massChange(slider): #slider passes to massChange 
    global changingObject #variable used in procedure
    changingObject.mass = 10**slider.value # the value is logged then put as a power of 10 to convert back to normal mass

def redcolorChange(slider): #subroutine to change the objects red color 
    global changingObject #pass in the current object being changed
    changingObject.color.x = slider.value #change that objects red color component to the slider value 
    changingObject.trail_color = changingObject.color #set the trail color to the color of the object 

def greencolorChange(slider): #subroutine to change the objects green color 
    global changingObject #pass in the current object being changed
    changingObject.color.y = slider.value #change that objects green color component to the slider value 
    changingObject.trail_color = changingObject.color #set the trail color to the color of the object 

def bluecolorChange(slider): #subroutine to change the objects blue color 
    global changingfObject #pass in the current object being changed
    changingObject.color.z = slider.value #change that objects blue color component to the slider value 
    changingObject.trail_color = changingObject.color #set the trail color to the color of the object 

def radiusChange(slider): #slider passes to radiusChange 
    global changingObject #variable used in procedure
    changingObject.radius = slider.value*radScaling*10**6 
    #the value is timesed by the rad scaling and 10^6 to convert to the correct order of magnitude 
    changingObject.trail_radius = slider.value*radScaling*trailScaling*10**6
    #the value for the trail radius is also changed, this is multiplied by trailscaling as well as it is a trail

def trailRadiusChange(slider): #procedure to change the radius of the trail
    global changingObject
    changingObject.trail_radius = slider.value*radScaling*trailScaling*10**6

def changeOrbitalIncline(slider): #procedure to change the orbital incline of the planet
    global changingObject
    changingObject.orbitIncline = slider.value #updating the value for orbital incline
    startup(OrbitingObjects, G) 
    #restarting the program as the orbital incline is changed by effecting the starting parameters of the planet

def changeAphelionAngle(slider): #procedure to change the aphelion angle of the planet
    global changingObject
    changingObject.aphelionAngle = slider.value #updating the value for aphelion angle
    startup(OrbitingObjects, G) 
    #restarting the program as the aphelion angle is changed by effecting the starting parameters of the planet

def changeAphelion(input):
    global changingObject
    if (type(input.number) == float or type(input.number) == int) and (input.number <= 14 and input.number >= math.log(changingObject.orbiting.radius, 10)):
        #verification to make sure that the user has input a number within the allowed range, logatrithmic scale used (base 10)
        changingObject.aphelion = 10**input.number
        startup(OrbitingObjects, G) #restart program to allow the aphelion to change

def changePerihelion(input):
    global changingObject
    if (type(input.number) == float or type(input.number) == int) and (input.number <= 14 and input.number >= math.log(changingObject.orbiting.radius, 10)): 
        #verification to make sure that the user has input a number within the allowed range 
        changingObject.Perihelion = 10**input.number
        startup(OrbitingObjects, G) #restart program to allow perihelion to change 

#-----User interactivity - Button functions--------------------------------------------------------------------
def GeneralSettings(B): #subroutine to change visable settings into general ones
    scene.caption = "General Settings: \n"
    scene.append_to_caption("Camera Focus:\n") #gives a title then moves onto next line
    menu(choices = astralBodiesString, bind=focusChange, selected = focus.name) #calls function focusChange when item is changed
    scene.append_to_caption("\n\nTime:") #gives slider a title so user knows what it does
    slider(bind = timeChange, min = 0, max = 200, value = timeConstant)
    scene.append_to_caption("\n\nRadius Scaling: ") #gives slider a title so user knows what it does
    slider(bind = radiusScalingChange, min = 1, max = 100, value = radScaling*10**-1)
    scene.append_to_caption("\n\nPath Length: ") #gives slider a title so user knows what it does
    slider(bind = pathLengthChange, min = 0, max = 100, value = pathLength*10**-6)
    scene.append_to_caption("\n\nTrail radius scaling: ") #gives slider a title so user knows what it does
    slider(bind = trailScalingChange, min = 1, max = 100, value = trailScaling*10**2)
    scene.append_to_caption("\n\nLabels: ") #gives checkbox a title that user can view
    checkbox(bind = labelToggle, checked = True) #calls label toggle procedure when checkbox clicked
    scene.append_to_caption("\n\nGravitational constant (x10^-11): ") #gives user a promt for the input box
    winput(bind=Gchange) #input value is passed to Gchange

def planetSettings(changingObject):
    scene.caption = (changingObject.name + ":\n\n") #outputs the object that is changing followed by two enters 
    scene.append_to_caption("Mass: ") #gives slider a title so user knows what it does
    slider(bind = massChange, min = math.log(changingObject.mass,10)-1, max = math.log(changingObject.mass,10)+1, 
    value = math.log(changingObject.mass,10)) 
    #will pass the value into massChange. the logs are used to make increments of slider equal regardless of order of magnitude
    scene.append_to_caption("\n\nRed: ")
    slider(bind = redcolorChange, min = 0, max = 1, value = changingObject.color.x)
    scene.append_to_caption("\n\nGreen: ")
    slider(bind = greencolorChange, min = 0, max = 1, value = changingObject.color.y)
    scene.append_to_caption("\n\nBlue: ")
    slider(bind = bluecolorChange, min = 0, max = 1, value = changingObject.color.z)
    scene.append_to_caption("\n\nRadius: ")
    slider(bind = radiusChange, min = 1, max = 100, value = changingObject.radius/(radScaling*10**6))
    scene.append_to_caption("\n\nTrail Radius: ")
    slider(bind = trailRadiusChange, min = 0, max = 100, value = changingObject.trail_radius/(radScaling*10**6*trailScaling))
    if changingObject in OrbitingObjects: #variables about the motion of the planet that only applies to moving bodies 
        scene.append_to_caption("\n\nAll of these settings require the program Sto restart itelf automatically:")
        #the program will need to reset as the motion of the planet is decided based on the initial variable of the planet
        scene.append_to_caption("\nOrbital Incline: ")
        slider(bind = changeOrbitalIncline, min = 0, max = 2*pi, value = changingObject.orbitIncline)        
        scene.append_to_caption("\nPoint of Aphelion(angle from earth aphelion): ")
        slider(bind = changeAphelionAngle, min = 0, max = 2*pi, value = changingObject.aphelionAngle)
        scene.append_to_caption("\nAphelion distance (10 to the power of, eg. 11 becomes 10^11. up to 14): ")
        winput(bind=changeAphelion) #the user should be able to get a sense of scale of the simulation
        scene.append_to_caption("\nPerihelion distance (10 to the power of, eg. 11 becomes 10^11. up to 14): ")
        winput(bind=changePerihelion) #the user should be able to get a sense of scale of the simulation
        

def sunSettings(B): #subroutine to change visible settings into the suns variables 
    global changingObject #variable changed to sun as the sun settings are now present 
    changingObject = sun
    planetSettings(changingObject) #running planetSettings to open all buttons

def mercurySettings(B): #subroutine to change visible settings into the mercury variables 
    global changingObject #variable changed to mercury as the mercury settings are now present 
    changingObject = mercury
    planetSettings(changingObject) #running planetSettings to open all buttons

def venusSettings(B): #subroutine to change visible settings into the venus variables 
    global changingObject #variable changed to venus as the venus settings are now present 
    changingObject = venus
    planetSettings(changingObject) #running planetSettings to open all buttons
    
def earthSettings(B): #subroutine to change visible settings into the earth variables 
    global changingObject #variable changed to earth as the earth settings are now present 
    changingObject = earth
    planetSettings(changingObject) #running planetSettings to open all buttons

def earthSettings(B): #subroutine to change visible settings into the earth variables 
    global changingObject #variable changed to earth as the earth settings are now present 
    changingObject = earth
    planetSettings(changingObject) #running planetSettings to open all buttons

def marsSettings(B): #subroutine to change visible settings into the mars variables 
    global changingObject #variable changed to mars as the mars settings are now present 
    changingObject = mars
    planetSettings(changingObject) #running planetSettings to open all buttons

def jupiterSettings(B): #subroutine to change visible settings into the jupiter variables 
    global changingObject #variable changed to jupiter as the jupiter settings are now present 
    changingObject = jupiter
    planetSettings(changingObject) #running planetSettings to open all buttons

def saturnSettings(B): #subroutine to change visible settings into the saturn variables 
    global changingObject #variable changed to saturn as the saturn settings are now present 
    changingObject = saturn
    planetSettings(changingObject) #running planetSettings to open all buttons
    
def uranusSettings(B): #subroutine to change visible settings into the uranus variables 
    global changingObject #variable changed to uranus as the uranus settings are now present 
    changingObject = uranus
    planetSettings(changingObject) #running planetSettings to open all buttons

def neptuneSettings(B): #subroutine to change visible settings into the neptune variables 
    global changingObject #variable changed to neptune as the neptune settings are now present 
    changingObject = neptune
    planetSettings(changingObject) #running planetSettings to open all buttons

def moonSettings(B): #subroutine to change visible settings into the moon variables 
    global changingObject #variable changed to moon as the moon settings are now present 
    changingObject = moon
    planetSettings(changingObject) #running planetSettings to open all buttons

button(pos=scene.title_anchor,text = "General", bind=GeneralSettings)#button that changes the settings to general variables
button(pos=scene.title_anchor,text = "Sun", bind=sunSettings)#button that changes settings to the Sun variables 
button(pos=scene.title_anchor, text =  "Mercury", bind=mercurySettings)#button that changes the settings to the mercury variables
button(pos=scene.title_anchor,text = "Venus", bind=venusSettings)#button that changes the settings to the venus variables
button(pos=scene.title_anchor,text = "Earth", bind=earthSettings)#button that changes settings to the earth variables 
button(pos=scene.title_anchor, text =  "Mars", bind=marsSettings)#button that changes the settings to the mars variables
button(pos=scene.title_anchor, text =  "Jupiter", bind=jupiterSettings)#button that changes the settings to the jupiter variables
button(pos=scene.title_anchor,text = "Saturn", bind=saturnSettings)#button that changes the settings to the saturn variables
button(pos=scene.title_anchor,text = "Uranus", bind=uranusSettings)#button that changes settings to the uranus variables 
button(pos=scene.title_anchor, text =  "Neptune", bind=neptuneSettings)#button that changes the settings to the neptune variables
button(pos=scene.title_anchor, text =  "Moon", bind=moonSettings)#button that changes the settings to the moon variables

#-----Program processes-----------------------------------------------------------------------------------------
startup(OrbitingObjects, G) #calls function startup to assign initial positions and velocities

while True: #loop forever due to it being a repeating program, every loop represents a second
    scene.center = focus.pos # sets the camera to focus on the cube
    a = 0
    b = 0
    for a in range(len(astralBodies)): #for every object
        for b in range(len(astralBodies)): #every object acts upon it
            if astralBodies[a] != astralBodies[b]: #removes error causing a planet to act upon itself causing div by 0
                astralBodies[a].velocity = accelerating(G, timeConstant, astralBodies[b], astralBodies[a]) 
                #calling accelerating with astralBodies b acting upon a
        astralBodies[a].pos += timeConstant*astralBodies[a].velocity
        objectLabels[a].pos = astralBodies[a].pos # assigns the position of a planets label to its new postion
        astralBodies[a].retain = dynamicPathLength(astralBodies[a], pathLength) 
        #calling path length function to change the retain value every loop
