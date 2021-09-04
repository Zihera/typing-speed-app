import tkinter as tk
from PIL import ImageTk, Image
import random

FONT_NAME = "Times New Roman"
HEIGHT = 750
WIDTH = 1000

word_list = []
with open('sample_text.txt', 'r') as f:
    # Remove the '\n' from each word and add to word_list
    word_list.append([word[:-2] for word in f])


class TypingSpeedTest(tk.Frame):
    """Class to create Typing Speed Test"""

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Typing Speed Test!')

        # Set Up Window Size
        self.master.minsize(WIDTH, HEIGHT)
        self.master.maxsize(WIDTH, HEIGHT)

        # Variables
        self.timer_length = 60
        self.timer = None
        self.word_list = []
        self.type_text = tk.StringVar()

        # Canvas
        self.canvas = tk.Canvas(height=HEIGHT, width=WIDTH)

        # Images
        self.background_image = ImageTk.PhotoImage(Image.open('images/marina-montoya-unsplash.jpg'))

        # Labels
        self.background_label = tk.Label(self.canvas, image=self.background_image)

        # Frames
        self.top_frame = tk.Frame(self.canvas, bg='#db4900', bd=2)
        self.frame = tk.Frame(self.canvas, bg='#db4900', bd=2)

        # Messages
        self.random_sample_text = tk.Message(self.top_frame, textvariable=self.type_text,
                                             font=(FONT_NAME, 14), bg='#db4900', anchor='n', pady=3)

        # Entry Variable
        self.entry = tk.Entry(self.frame, font=(FONT_NAME, 14), bg='#f57e42', justify='center')

        # Buttons
        self.start_button = tk.Button(text='Start Test', bg='#ffd8bd', highlightthickness=0, command=self.start_timer)
        self.generate_text_button = tk.Button(text='Generate Text', bg='#ffd8bd', highlightthickness=0, command=self.get_sample_text)

        # Widget Placement
        self.canvas.pack()
        self.background_label.place(relh=1, relw=1)
        self.top_frame.place(relx=0.5, rely=0.3, relw=0.5, relh=0.35, anchor='n')
        self.frame.place(relx=0.5, rely=0.65, relw=0.5, relh=0.1, anchor='n')
        self.random_sample_text.place(relw=1, relh=1)
        self.entry.place(relw=1, relh=1)
        self.entry.focus()
        self.start_button.place(relx=0.63, rely=0.75, relw=0.15, relh=0.05, anchor='n')
        self.generate_text_button.place(relx=0.37, rely=0.75, relw=0.15, relh=0.05, anchor='n')

    def get_sample_text(self):
        """Get 100 random words from word list"""
        for word in word_list:
            sample_text = random.choices(word, k=100)
            self.type_text.set(sample_text)

    def start_timer(self):
        """Start the Typing Speed Test timer and clear entry"""
        count = self.timer_length
        self.entry.config(state='normal')
        self.entry.delete(0, 'end')
        self.count_down(count)

    def count_down(self, count):
        """Timer that counts to 0, then it calls check_text and disables the user's entry"""
        if count > 0:
            self.timer = self.after(1000, self.count_down, count - 1)
            print(count)
        else:
            self.check_text(self.entry.get())
            self.entry.config(state='disabled')

    def check_text(self, entry):
        """Get user's entry and returns their CPM and WPM"""
        text_list = []
        text_entered = entry
        for text in text_entered:
            text_list.append(text)

        cpm = len(text_list)
        wpm = cpm / 5
        print(f'Your cpm is {cpm}, your wpm is {wpm}')


if __name__ == '__main__':
    root = tk.Tk()
    app = TypingSpeedTest(root)
    app.mainloop()
