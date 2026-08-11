
import tkinter as tk
from tkinter import ttk
import requests

class TelegramAlertStudio:
    def __init__(self, root):
        self.root = root
        self.root.title('Telegram Alert Studio')
        self.root.configure(bg='#2f2f2f')

        # Header frame
        self.header_frame = tk.Frame(self.root, bg='#2f2f2f')
        self.header_frame.pack(fill='x')
        self.title_icon = tk.Label(self.header_frame, text='🚀', font=('Arial', 24), bg='#2f2f2f', fg='white')
        self.title_icon.pack(side='left')
        self.subtitle = tk.Label(self.header_frame, text='Telegram Alert Studio', font=('Arial', 18), bg='#2f2f2f', fg='white')
        self.subtitle.pack(side='left', padx=10)

        # Input controls frame
        self.controls_frame = tk.Frame(self.root, bg='#2f2f2f')
        self.controls_frame.pack(fill='x', padx=10, pady=10)
        self.telegram_token_label = tk.Label(self.controls_frame, text='Telegram Token:', font=('Arial', 12), bg='#2f2f2f', fg='white')
        self.telegram_token_label.pack(side='left')
        self.telegram_token_entry = tk.Entry(self.controls_frame, width=50)
        self.telegram_token_entry.pack(side='left', padx=10)
        self.trigger_button = tk.Button(self.controls_frame, text='Trigger Alert', command=self.trigger_alert, bg='#4f4f4f', fg='white')
        self.trigger_button.pack(side='left', padx=10)

        # Visualization display frame
        self.display_frame = tk.Frame(self.root, bg='#2f2f2f')
        self.display_frame.pack(fill='both', expand=True, padx=10, pady=10)
        self.treeview = ttk.Treeview(self.display_frame)
        self.treeview['columns'] = ('Subscriber', 'Trigger')
        self.treeview.column('#0', width=0, stretch='no')
        self.treeview.column('Subscriber', anchor='w', width=200)
        self.treeview.column('Trigger', anchor='w', width=200)
        self.treeview.heading('#0', text='', anchor='w')
        self.treeview.heading('Subscriber', text='Subscriber', anchor='w')
        self.treeview.heading('Trigger', text='Trigger', anchor='w')
        self.treeview.pack(fill='both', expand=True)

        # Status message label
        self.status_label = tk.Label(self.root, text='', font=('Arial', 12), bg='#2f2f2f', fg='white')
        self.status_label.pack(fill='x', padx=10, pady=10)

    def trigger_alert(self):
        telegram_token = self.telegram_token_entry.get()
        if telegram_token:
            try:
                response = requests.post(f'https://api.telegram.org/bot{telegram_token}/getUpdates')
                if response.status_code == 200:
                    self.status_label['text'] = 'Alert triggered successfully!'
                    self.treeview.insert('', 'end', values=('Subscriber 1', 'Trigger 1'))
                else:
                    self.status_label['text'] = 'Failed to trigger alert.'
            except requests.exceptions.RequestException as e:
                self.status_label['text'] = 'Error: ' + str(e)
        else:
            self.status_label['text'] = 'Please enter Telegram token.'

if __name__ == '__main__':
    root = tk.Tk()
    app = TelegramAlertStudio(root)
    root.mainloop()
