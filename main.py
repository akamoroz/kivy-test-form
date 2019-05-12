#!/usr/bin/env python3.6
# -*- coding: utf-8

from kivy import require as require_version
require_version('1.10.1')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder

from kivymd.theming import ThemeManager

var = '''
#: kivy 1.10.1
#:import Anchorlayout kivy.uix.anchorlayout.AnchorLayout
#:import MDRaisedButton kivymd.button.MDRaisedButton
#:import MDTextField kivymd.textfields.MDTextField
#:import GridLayout kivy.uix.gridlayout.GridLayout
#:import MDSpinner kivymd.spinner.MDSpinner

<MySpinner@RelativeLayout>

    MDSpinner:
        id: spinner
        size_hint: None, None
        size: dp(46), dp(46)
        pos_hint: {'center_x': .5, 'center_y': .7}
        active: False


<AauthForm>
    name: 'Auth Form'

    MySpinner:
        id: update_spinner_layout

    BoxLayout:
        orientation: 'vertical'
        padding: dp(app.padding), dp(app.padding)
        spacing: dp(30)
        size_hint_y: 1
        size_hint_x: 1


        AnchorLayout:
            anchor_x: 'center'
            anchor_y: 'center'
            size_hint_y: 1
            size_hint_x: 1

            BoxLayout:
                orientation: 'vertical'
                size_hint_y: .2
                size_hint_x: .5
                spacing: 20

                BoxLayout:
                    size_hint_y: .5
                    size_hint_x: 1

                    MDTextField:
                        id: token_input
                        hint_text: "Enter your Token"
                        pos_hint: {'center_y': .5, 'center_x': .5}

                BoxLayout:
                    size_hint_y: .4
                    size_hint_x: .4
                    pos_hint: {'center_y': .5, 'center_x': .5}

                    MDRaisedButton:
                        id: login_button
                        text: 'Login'
                        size_hint_x: .4
                        size_hint_y: .9
'''


class AauthForm(Screen):
    pass


class StockApp(App):
    # Theme Manager
    theme_cls = ThemeManager()
    title = 'Test Form'
    # Screen Manager object
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(StockApp, self).__init__(**kwargs)

        # Spinner .KV
        Builder.load_string(var)

        # Set Theme Style
        self.theme_cls.theme_style = 'Light'
        # set Theme Color
        self.theme_cls.primary_palette = 'Teal'
        self.padding = 20

    def build(self):
        """
        Render window method
        :return:
        """
        self.sm.add_widget(AauthForm())
        self.sm.current = 'Auth Form'
        return self.sm


if __name__ == '__main__':
    StockApp().run()
