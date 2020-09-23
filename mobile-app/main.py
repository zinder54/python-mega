from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from datetime import datetime
from pathlib import Path
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.core.window import Window
import json, glob, random

Builder.load_file('design.kv')
Window.clearcolor = (.20,0.20,.20,0.75)

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current= "Sign_up_Screen"

    def login(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)
        if uname in users and users[uname]['password'] == pword:
            self.manager.current = "Login_Screen_Success"
        else:
            self.ids.login_wrong.text = "Wrong username or password!"

class SignUpScreen(Screen):
    def add_user(self,uname,pword):
        with open("users.json") as file:
            users = json.load(file)
        
        users[uname]={"username": uname, "password": pword,
        "created": datetime.now().strftime("%Y, %m, %d,%H, %M, %S")}
        
        with open("users.json", "w") as file:
            json.dump(users, file)
        self.manager.current = "Sign_Up_Screen_Success"

class SignUpScreenSuccess(Screen):
    def back_login(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"

class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"

    def get_quote(self, feel):
        feel = feel.lower()
        available_feel = glob.glob("quotes/*txt")
        available_feel = [Path(filename).stem for filename in 
                            available_feel]
        if feel in available_feel:
            with open(f"quotes/{feel}.txt",encoding="utf-8") as file:
                Quotes = file.readlines()
            self.ids.quote.text = random.choice(Quotes)
        else:
            self.ids.quote.text = "Try another feeling!"
            
class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass


class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()