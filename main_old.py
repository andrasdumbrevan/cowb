#!/usr/bin/python3

import os
import sys
import time
import math
from datetime import datetime
from threading import Thread
from sys import exit
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.progressbar import ProgressBar
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.config import Config
from kivy.graphics import Rectangle, Color, Rotate, PushMatrix, Line, PopMatrix
from kivy.graphics import Rotate
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.animation import Animation
from kivy.uix.image import AsyncImage
from random import seed
from random import randint
from kivy.core.audio import SoundLoader
import random
from kivy.utils import platform

print("Platform",platform)

if platform == 'android':
    print("Running on Android")
else:
    Config.set('graphics', 'resizable', False)
    Config.write()
    Window.size = (1280, 768)

os=platform

random.seed(time.time())
resolution=Window.size
print(resolution)
resx=int(resolution[0])
resy=int(resolution[1])
#Config.set('graphics', 'fullscreen', 'auto')
#Window.size = (1366, 768)
#Window.fullscreen = True
#Window.fullscreen = 'auto'

def get_ctime():

    now = datetime.now()

    current_time = now.strftime("%H%M%S")
    print("Current Time =", current_time)
    ctime=int(current_time)

p = SoundLoader.load("md/3.wav")
p.loop=True

def play_music(cmd):
    if p and cmd=="play":
        #print("Sound found at %s" % sound.source)
        #print("Sound is %.3f seconds" % sound.length)
        p.play()

    if p and cmd=="stop":
        p.stop()
    
    

#handle the touch / mouse events
class TouchInput(Widget):
    def __init__(self, **kwargs):
            super().__init__(**kwargs)

    def on_touch_down(self, touch):
        #print(touch)

        if os=='android':
            if (touch.pos[0]<500):
                mx=touch.pos[0]
                my=touch.pos[1]
                GamePage.mx=mx
                GamePage.my=my
            else:
                GamePage.tact="right"
                mx=touch.pos[0]
                my=touch.pos[1]
                GamePage.mx=mx
                GamePage.my=my
        else:
            #we assume we are running on a pc with mouse input that has buttons
            GamePage.tact=touch.button

            if (touch.button!="right"):
                mx=touch.pos[0]
                my=touch.pos[1]
                GamePage.mx=mx
                GamePage.my=my
 

    def on_touch_move(self, touch):
        print(touch)
    def on_touch_up(self, touch):
        print("RELEASED!",touch)

    def on_motion(self, etype, motionevent):
        # will receive all motion events.
        mx=motionevent.pos[0]
        my=motionevent.pos[1]
        #print("mx: ",mx," my: ",my)
        GamePage.mx=mx
        GamePage.my=my

    def on_click(self, etype, on_touch_down):
        # will receive all motion events.
        mx=motionevent.pos[0]
        my=motionevent.pos[1]
        #print("mx: ",mx," my: ",my)
        GamePage.mx=mx
        GamePage.my=my


class GamePage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 6
        self.rows = 5
        fastest = []
        GamePage.docked=True
        GamePage.move=False
        GamePage.tact=0

        self.bullet=SoundLoader.load("md/laser7.wav")
        self.bullet2=SoundLoader.load("md/laser4.wav")
        self.fail1=SoundLoader.load("md/objecthit.wav")

        #play_music("play")

        '''size_hint: None, None'''
        kv = '''
FloatLayout:
    angle: 180
    Image:
        source: "chars/guy1.zip"
        anim_delay: "0.09"
        
        size_hint_y: 0.7
        size_hint_x: 0.9
        allow_stretch: True
        keep_ratio: False
        pos_hint: {'center_x': .5, 'center_y': .5}
        canvas.before:
            PushMatrix
            Rotate:
                angle: root.angle
                origin: self.center
        canvas.after:
            PopMatrix
'''

        kv2 = '''
FloatLayout:
    angle: 260
    Image:
        source: "chars/guy1.zip"
        anim_delay: "0.09"
        
        size_hint_y: 0.7
        size_hint_x: 0.9
        allow_stretch: True
        keep_ratio: False
        pos_hint: {'center_x': .5, 'center_y': .5}
        canvas.before:
            PushMatrix
            Rotate:
                angle: root.angle
                origin: self.center
        canvas.after:
            PopMatrix
'''
        kv3 = '''
FloatLayout:
    angle: 90
    Image:
        source: "ast/bullet2.png"
        anim_delay: "0.09"
        
        size_hint_y: 0.3
        size_hint_x: 0.3
        allow_stretch: True
        keep_ratio: False
        pos_hint: {'center_x': .5, 'center_y': .5}
        canvas.before:
            PushMatrix
            Rotate:
                angle: root.angle
                origin: self.center
        canvas.after:
            PopMatrix
'''
        kv4 = '''
FloatLayout:
    angle: 90
    Image:
        source: "ast/bullet2.png"
        anim_delay: "0.09"
        
        size_hint_y: 0.3
        size_hint_x: 0.3
        allow_stretch: True
        keep_ratio: False
        pos_hint: {'center_x': .5, 'center_y': .5}
        canvas.before:
            PushMatrix
            Rotate:
                angle: root.angle
                origin: self.center
        canvas.after:
            PopMatrix
'''

        #tile randomizer
        tile_random=random.randint(0, 10)
        if tile_random==0:
            tile="bespin/u_floor04.jpg"
        if tile_random==1:
            tile="bespin/u_floor03.jpg"
        if tile_random==2:
            tile="bespin/floor3.jpg"
        if tile_random==3:
            tile="bespin/floor.jpg"
        if tile_random==4:
            tile="bespin/basic.jpg"
        if tile_random==5:
            tile="bespin/basic2.jpg"
        if tile_random==6:
            tile="bespin/newfloor.jpg"
        if tile_random==7:
            tile="bespin/tile1.jpg"
        if tile_random==8:
            tile="bespin/tile2.jpg"
        if tile_random==9:
            tile="bespin/3.png"
        if tile_random==10:
            tile="bespin/u_wall09.jpg"


        for n in range(0,(self.cols*self.rows)-self.cols):
            self.tiles = Image(source=tile,allow_stretch=True, keep_ratio=False,size_hint_y=None,height=resy/5)
            self.add_widget(self.tiles)


        ####################################################
        #               CRATES create and save             #
        ####################################################

        self.cratesx=""
        self.cratesy=""
        for n in range(0,random.randint(1,1)):
            #generate random possition of crates
            posx=random.randint(resx/2-200, resx/2)
            posy=random.randint(0+resy/3, resy-50)

            #save generated possitions to a list
            self.cratesx+=str(posx)+","
            self.cratesy+=str(posy)+","

            #add crates on screen
            with self.canvas:
                #Color(1., 0, 0)
                Rectangle(source="crate.png",pos=(posx, posy), size=(resx/10, resy/7))


        self.cratesx=self.cratesx.split(",")
        self.cratesy=self.cratesy.split(",")
        del self.cratesx[-1]
        del self.cratesy[-1]




        ####################################################
        #               Control area                       #
        ####################################################

        #  controls area #

        ###  savatar  ###
        #load_zipped_png_files = Image(source = 'explosion.zip', anim_delay = 0,allow_stretch = True, keep_ratio = False,keep_data = True)
        self.cbar_1=Image(source='tenor.zip',allow_stretch=True,anim_delay=0.1,mipmap= True)
        self.add_widget(self.cbar_1)

        ### PLAYER ###

        self.player=Builder.load_string(kv)
        self.add_widget(self.player)

        #cotrol buttons
        self.directions=GridLayout(size_hint_y=1, height=resy/5)
        self.directions.cols=2
        self.directions.rows=2

        #Button and bullet bar

        self.directions.undock = Button(text="Ready")
        self.directions.undock.bind(on_press=self.undock_ship)
        self.directions.add_widget(self.directions.undock)

        #### ENEMY bullet ###########################
        self.directions.e_bullet=Builder.load_string(kv3)
        self.directions.add_widget(self.directions.e_bullet)

        #### Player bullet ###########################
        self.directions.pl_bullet=Builder.load_string(kv3)
        self.directions.add_widget(self.directions.pl_bullet)

        self.add_widget(self.directions)

        # left data info #
        self.cbar_1 = Image(source='spin3.zip',allow_stretch=True,anim_delay=0.1) #size_hint_y=1 , height=200)
        #self.cbar.btn.bind(on_press=self.act)
        self.add_widget(self.cbar_1)


        #### ENEMY ###########################
        self.player2=Builder.load_string(kv2)
        self.add_widget(self.player2)

        #### ENEMY Avatar ####################
        self.cbar_1 = Image(source='enemy2.zip',allow_stretch=True,anim_delay=.12) #size_hint_y=1 , height=200)
        #self.cbar.btn.bind(on_press=self.act)
        self.add_widget(self.cbar_1)


        ev=Window.bind(on_touch_down=TouchInput.on_touch_down)
        #print(ev)

        Clock.schedule_interval(self.update_player, 0.1)
        Clock.schedule_interval(self.move_ship, 0.1)
        Clock.schedule_interval(self.move_enemy, 0.1)
        self.undock_enemy(self)

        # enemy variables #
        self.c=0
        self.direction=0
        self.distance_up=660 # 
        self.distance_down=190 #
        seed(1)
        self.e_speed=random.randint(10, 30)
        self.e_fire_trigger=random.randint(0,10)
        self.enemy_fire=False

        self.p_fire_trigger=False
        self.player_fire=False

        #this controls the players shoot sound time and trigger
        self.bullet_sound=True
        self.bullet2_sound=True

        self.ps=0

        # players lives (both)
        self.e_lives=5
        self.p_lives=5



    def check_crates_hit(self,who):
        hit=False

        for y in self.cratesy:
            if who=="enemy":
                if self.directions.e_bullet.y>=int(y) and self.directions.e_bullet.y<int(y)+resy/7:
                    print("enemy hit crate") 
                    self.fail1.play()            
                    hit=True

            if who=="player":  #remmember we are going 0 (down) to up + and also left 0 to right +
                if self.directions.pl_bullet.y>=int(y) and self.directions.pl_bullet.y<int(y)+resy/8:
                    print("player hit crate") 
                    self.fail1.play()            
                    hit=True
        
        return hit


    def check_players_hit(self,who):
        hit=False

        for y in self.cratesy:
            if who=="enemy":
                if self.directions.e_bullet.y>=self.player.y+50 and self.directions.e_bullet.y<self.player.y+100:
                    print("enemy hit player") 
                    self.fail1.play()            
                    hit=True

            if who=="player":
                if self.directions.pl_bullet.y>=self.player2.y+50 and self.directions.pl_bullet.y<self.player2.y+100:
                    print("player hit enemy") 
                    self.fail1.play()            
                    hit=True

        
        return hit


    def ready_ship(self,button):
        pass
        #anim=Animation(angle=0,duration=4)
        #anim.start(self.player)

    def undock_ship(self,button):
        anim=Animation(y=200,duration=2)
        anim.start(self.player)
        GamePage.docked=False

    def move_ship(self,button):

        if GamePage.move==True:
            self.player.anim_delay=0
            myradians = math.atan2(self.player2.y-self.player.y, self.player2.x-self.player.x)
            newangle = math.degrees(myradians)
            #print(newangle)

            anim=Animation(y=GamePage.my, duration=1)
            anim2=Animation(angle=newangle+90, duration=0.3)
            anim.start(self.player)
            anim2.start(self.player)

    def undock_enemy(self,button):

        anim=Animation(y=190,duration=2)
        anim.start(self.player2)      

    def move_enemy(self,button):

        if GamePage.move==True:
            self.player2.anim_delay=0

            myradians = math.atan2(self.player2.y-self.player.y, self.player2.x-self.player.x)
            newangle = math.degrees(myradians)
            #print(newangle)

            if self.player2.y>=self.distance_up:
                if self.direction!=1:
                    self.distance_up=random.randint(350, 660)
                    self.e_speed=random.randint(15, 30)
                self.direction=1

            if self.player2.y<=self.distance_down:
                if self.direction!=0:
                    self.distance_down=random.randint(190, 350)
                    self.e_speed=random.randint(15, 30)
                self.direction=0

            if self.direction==1:
                self.c-=self.e_speed
            else:
                self.c+=self.e_speed


            anim=Animation(y=self.c,duration=0.08)
            anim2=Animation(angle=newangle+280, duration=0.3)
            anim.start(self.player2)
            anim2.start(self.player2)


    def update_player(self,_):
        if GamePage.docked!=True:
            if self.player.y>=199:
                GamePage.move=True
                GamePage.docked=True
                #self.player.angle=90

        ########################################
        ############## Player Fire #############
        ########################################
        if GamePage.tact=="right":
            self.player_fire=True
            self.bullet_sound=True

        #set bullet to the enemy #checked at enemy Fire -if true then it means we shoot
        # and go to player1
        if self.player_fire==False:
            self.directions.pl_bullet.x=self.player.x+75
            self.directions.pl_bullet.y=self.player.y+50
            self.directions.pl_bullet.opacity=0
        else:
            if self.directions.pl_bullet.x<=self.player2.x-30:

                #play the player sound
                if self.bullet_sound==True:
                    if (self.directions.pl_bullet.x==self.player.x-75): 
                        self.bullet.play()
                        self.bullet_sound=False
                    else:
                        if self.directions.pl_bullet.x==self.player2.x:
                            self.bullet_sound=False
                else:
                    self.bullet_sound=False

                self.directions.pl_bullet.opacity=1
                p_bullet_radians = math.atan2(self.directions.pl_bullet.y-self.player2.y, self.directions.pl_bullet.x-self.player2.x)
                p_bullet_angle = math.degrees(p_bullet_radians)
                p_anim_bullet=Animation(x=self.player2.x+35, y=self.directions.pl_bullet.y, angle=0, duration=0.1)
                p_anim_bullet.start(self.directions.pl_bullet)

                if self.check_crates_hit("player")!=True:
                    print(self.check_players_hit("player"))
                    self.player_fire=False
                else:
                    self.directions.pl_bullet.opacity=0.3

                #this is revers variables to player not to player2 where player is user
                if self.directions.pl_bullet.x<=self.player2.x-10:
                    #self.directions.e_bullet.opacity=0
                    self.player_fire=False

            else:
                self.player_fire=False


        ########################################
        ############## ENEMY Fire ##############
        ########################################

        #print(self.e_fire_trigger)
        #trigger the enemy fire randomly

        self.e_fire_trigger=random.randint(0,10)
        
        if self.e_fire_trigger==1:
            self.enemy_fire=True
            self.bullet2_sound=True
            #self.bullet2.stop()
        else:
            #pass
            self.enemy_fire=False
            self.bullet2_sound=False
            #self.bullet2.stop()

        #set bullet to the enemy #checked at enemy Fire -if true then it means we shoot
        # and go to player1
        if self.enemy_fire==False:
            self.directions.e_bullet.x=self.player2.x+75
            self.directions.e_bullet.y=self.player2.y+50
            #self.directions.e_bullet.opacity=0
        else:
            if self.directions.e_bullet.x>=self.player.x-30:

                #play the enemy sound
                if self.bullet2_sound==True:
                    if (self.directions.e_bullet.x==self.player2.x+75): 
                        self.bullet2.play()
                        self.bullet2_sound=False
                    else:
                        if self.directions.e_bullet.x==self.player.x:
                            self.bullet2_sound=False
                else:
                    self.bullet2_sound=False

                self.directions.e_bullet.opacity=1
                e_bullet_radians = math.atan2(self.directions.e_bullet.y-self.player.y, self.directions.e_bullet.x-self.player.x)
                e_bullet_angle = math.degrees(e_bullet_radians)
                e_anim_bullet=Animation(x=self.player.x-35, y=self.directions.e_bullet.y, angle=0, duration=0.1)
                e_anim_bullet.start(self.directions.e_bullet)

                if self.check_crates_hit("enemy")!=True:
                    print(self.check_players_hit("enemy"))
                    self.enemy_fire=False
                else:
                    self.directions.e_bullet.opacity=0.3

                #this is revers variables to player not to player2 where player is user
                if self.directions.e_bullet.x<=self.player.x+10:
                    #self.directions.e_bullet.opacity=0
                    self.enemy_fire=False

            else:
                self.enemy_fire=False


class InfoPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.message = Label(halign="center", valign="middle", font_size=30)
        self.add_widget(self.message)


class CBoxApp(App):
    def build(self):

        #Window.bind(on_request_close=self.on_request_close)

        self.screen_manager = ScreenManager()

        self.game_page = GamePage()
        screen = Screen(name="Game")
        screen.add_widget(self.game_page)
        self.screen_manager.add_widget(screen)

        self.info_page = InfoPage()
        screen = Screen(name="Info")
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


    def on_request_close(self, *args):
        play_music("stop")
        CBoxApp.stop(self)
        CBoxApp.terminate(self)
        sys.exit()


def show_error(message):
    ibvpn_app.info_page.update_info(message)
    ibvpn_app.screen_manager.current = "Info"
    Clock.schedule_once(sys.exit, 10)


if __name__ == "__main__":

    ibvpn_app = CBoxApp()
    ibvpn_app.run()
    play_music("stop")
    sys.exit()

sys.exit()