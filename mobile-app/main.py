from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from datetime import datetime
import json

Builder.load_file('design.kv')

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current= "Sign_up_Screen"

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

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()