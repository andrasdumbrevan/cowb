#!/usr/bin/python3

import os
import sys
import time
import ctypes
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
from datetime import datetime
from kivy.config import Config

Window.size = (1024, 600)

class GamePage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 5
        self.rows = 5
        fastest = []

        #self.cnbtn = ToggleButton(text='Connect', group='connect')

        #we draw the game board and treat them as "tiles(widgets)"
        for n in range(0,15):
        	self.tiles = Image(source="2.png",allow_stretch=True, size_hint_y=None, size_hint_x=None, height=150, width=200)
        	#self.cnbtn.bind(on_press=self.task_fastest) 
        	self.add_widget(self.tiles)

        #controls area
        #self.cbar_1 = Label(text="Info 1", size_hint_y=None , height=150)
        self.cbar_1=Image(source='tenor.gif',allow_stretch=True,anim_delay=0.1)
        #self.cbar.btn.bind(on_press=self.act)
        self.add_widget(self.cbar_1)
        self.cbar_1 = Label(text="....\n....\n....\n....", size_hint_y=None , height=150)
        #self.cbar.btn.bind(on_press=self.act)
        self.add_widget(self.cbar_1)

        #cotrol buttons
        self.directions=GridLayout(size_hint_y=None, height=150)
        self.directions.cols=3
        self.directions.rows=2

        #up bar
        self.directions.spot = Label(text="")
        #self.cbar.btn.bind(on_press=self.act)
        self.directions.add_widget(self.directions.spot)

        self.directions.up = Button(text="Up")
        self.directions.up.bind(on_press=self.mup)
        self.directions.add_widget(self.directions.up)

        self.directions.spot = Label(text="")
        #self.cbar.btn.bind(on_press=self.act)
        self.directions.add_widget(self.directions.spot)

        #down bar
        self.directions.left = Button(text="Left")
        self.directions.left.bind(on_press=self.mleft)
        self.directions.add_widget(self.directions.left)

        self.directions.down = Button(text="Down")
        self.directions.down.bind(on_press=self.mdown)
        self.directions.add_widget(self.directions.down)

        self.directions.mright = Button(text="Right")
        self.directions.mright.bind(on_press=self.mright)
        self.directions.add_widget(self.directions.mright)

        self.add_widget(self.directions)

        #right data info
        self.cbar_1 = Label(text="....\n....\n....\n....", size_hint_y=None , height=150)
        #self.cbar.btn.bind(on_press=self.act)
        self.add_widget(self.cbar_1)
        self.cbar_1=Image(source='spin.gif',allow_stretch=True,anim_delay=0.09)
        #self.cbar.btn.bind(on_press=self.act)
        self.add_widget(self.cbar_1)

        self.player = Image(source="unit1.gif", allow_stretch=True,size_hint_y=None , height=150,anim_delay=0.09)
        self.add_widget(self.player)

        Clock.schedule_once(self.update_player, 2)

    def update_player(self,_):
    	self.player.y=150

    def mup(self,button):
    	if self.player.y<450:
        	self.player.y+=150
    def mdown(self,button):
    	if self.player.y>150:
        	self.player.y-=150
    def mright(self,button):
    	if self.player.x<800:
        	self.player.x+=200
    def mleft(self,button):
    	if self.player.x>0:
        	self.player.x-=200



class InfoPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.message = Label(halign="center", valign="middle", font_size=30)
        self.add_widget(self.message)


class CBoxApp(App):
    def build(self):
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


def show_error(message):
    ibvpn_app.info_page.update_info(message)
    ibvpn_app.screen_manager.current = "Info"
    Clock.schedule_once(sys.exit, 10)


if __name__ == "__main__":

    ibvpn_app = CBoxApp()
    ibvpn_app.run()

sys.exit()