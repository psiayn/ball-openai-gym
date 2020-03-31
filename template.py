import arcade
import os
import sys

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Starting Template"

CIRCLE_RADIUS = 20

GRAVITY_CONST = 0.3

BOUNCINESS = 0.9


class Bouncy:

    """
    
    Parameters
    -------------------------------
    screen_height: height of the screen, set to 800 if omitted
    screen_width: width of the screen, set to 600 if omitted
    screen_title: the title of the window, set to "Starting Template" if omitted
    radius: radius of the circle, set to 20 if omitted
    gravity: gravity factor that affects the ball (0-1), set to 0.3 if omitted
    bounciness: bounciness factor that affects the ball (0-1), set to 0.8 if omitted
    delta_x: the default value x changes by, set to 2 if omitted
    delta_y: the default value y changes by, set to 0 if omitted
    
    """

    def __init__(self,screen_height=SCREEN_HEIGHT,screen_width=SCREEN_WIDTH,screen_title=SCREEN_TITLE,radius=CIRCLE_RADIUS,gravity=GRAVITY_CONST,bounciness=BOUNCINESS,delta_x=2,delta_y=0):


        # initialize the variables for using across class simpler
        self.scrHeight = screen_height
        self.scrWidth = screen_width
        self.radius = radius
        self.gravity = gravity
        self.bounciness = bounciness
        self.title = screen_title        
        
        #initial co-ordinates and change in 
        self.x = self.radius
        self.y = self.scrHeight - self.radius
        self.delta_x = delta_x
        self.delta_y = delta_y


    def draw(self,_delta_time):
        """
        
        Draws everything on the screen

        """

        # start the render . must happen before any thing 
        arcade.start_render()

        # drawing the circle
        arcade.draw_circle_filled(self.x,self.y,self.radius,arcade.color.BLIZZARD_BLUE)

        # update the values of the circle
        self.x += self.delta_x
        self.y += self.delta_y

        # bring the ball down due to gravity
        self.delta_y -= self.gravity

        # reverse directions if hits the boundaries
        if self.x < self.radius and self.delta_x < 0:
            self.delta_x *= -self.bounciness
        elif self.x > self.scrWidth - self.radius and self.delta_x>0:
            self.delta_x *= -self.bounciness

        # checking if the ball hits the floor
        if self.y < self.radius and self.delta_y < 0:
            # if the ball bounces with a decent velocity, do a normal bounce.
            # otherwise the ball won't have enough time resolution to accurately represent
            # the bounce and it will bounce forever. so we'll divide the bounciness
            # by half to let it settle out.
            if self.delta_y * -1 > self.gravity * 15:
                self.delta_y *= -self.bounciness 
            else:
                self.delta_y *= -self.bounciness/2


    def renderDisplay(self):
        """
        
        Opens the window and refreshes the window at a certain refresh rate
        and renders everything

        """

        # open window with the set screen size , title, and set background
        arcade.open_window(self.scrWidth,self.scrHeight,self.title)
        arcade.set_background_color(arcade.color.WHITE)

        # tell arcade to draw every 1/80 second
        arcade.schedule(self.draw,1/120)

        arcade.run()

        #arcade.close_window()

        
test = Bouncy()
test.renderDisplay()
