import random

import requests
from tkinter import *

eight_ball_api_url = 'https://eightballapi.com/api'

# parameters = {
#     'question': 'Will I Get A 4.0',
#     'lucky': 'True',
#     'biased': 'True'
# }

TEXT_COLORS = [
    "#ff6eff", "#ff4d4d", "#ffaa1d", "#39ff14", "#15f4ee",
    "#ff00ff", "#00ffff", "#ffff00", "#00ff00", "#ff0000"
]

class EightBallApp():

    def __init__(self):
        self.window = Tk()
        self.window.title('Magic Eight Ball')
        self.window.config(bg='black', pady=30, padx=30)

        eight_ball_image = PhotoImage(file='8ball.png')
        self.display = Canvas(height=610, width=595, bg='purple', highlightthickness=0)
        self.display.create_image(290, 300, image=eight_ball_image)
        self.display.grid(column=0, row=0, pady=20, padx=20)
        self.readout = self.display.create_text(300, 265, text=f'Decide your fate.', font=('Arial', 12, 'bold'))

        self.shake_btn = Button(text='Shake Ball', bg='gray', fg='purple', highlightthickness=0, font=('Arial', 14, 'bold'), command=self.shake_eight_ball)
        self.shake_btn.grid(column=0, row=1)

        self.window.mainloop()

    def shake_eight_ball(self):
        eight_ball = requests.get(eight_ball_api_url)
        eight_ball.raise_for_status()
        roll_ball = eight_ball.json()
        self.display.itemconfig(self.readout, text=f'{roll_ball['reading']}')
        self.display.config(bg=random.choice(TEXT_COLORS))
        print(roll_ball)

EightBallApp()