from tkinter import filedialog
from tkinter import *
import pygame
import os

root = Tk()
root.title("Music Player")
root.geometry("600x400")

pygame.mixer.init()  # its help us in playing music with pygame

menubar = Menu(root)
root.config(menu=menubar)


#function for music player features
songs = []
current_song = ""
pause = False
def load_music():
    global current_song
    root.directory = filedialog.askdirectory()

    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == '.mp3':
            songs.append(song)

    for song in songs:
        songlist.insert("end", song)

    songlist.selection_set(0)
    current_song = songs[songlist.curselection()[0]]

def play_music():
    global current_song, pause

    if not pause:
        pygame.mixer.music.load(os.path.join(root.directory, current_song))
        pygame.mixer.music.play()

    else:
        pygame.mixer.music.unpause()
        pause = False

def pause_music():
    global pause
    pygame.mixer.music.pause()
    pause = True

def previous_music():
    global current_song, pause
    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song)-1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass

def next_music():
    global current_song, pause

    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song)+1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass


# setting up menubar
organise_menu = Menu(menubar,  tearoff=False)
organise_menu.add_command(label='Select Folder', command=load_music)
menubar.add_cascade(label='Load Music', menu=organise_menu)

# setting up songlist
songlist = Listbox(root, bg="AntiqueWhite4", fg="black", width=100, height=15, font=(
    'poppins', 14))  # its a box whichh will show the songs list
songlist.pack()  # it added the songlist to the window

# setting up buttons and their images
play_btn_image = PhotoImage(file='play.png')
pause_btn_image = PhotoImage(file='pause.png')
previous_btn_image = PhotoImage(file='previous.png')
next_btn_image = PhotoImage(file='next.png')

# now create a frame , a small section of tk.
control_frame = Frame(root)
control_frame.pack()

# putting buttons in control_frame and assigned with their respected functions
play_btn = Button(control_frame, image=play_btn_image,
                  borderwidth=0, command=play_music)
pause_btn = Button(control_frame, image=pause_btn_image,
                   borderwidth=0, command=pause_music)
previous_btn = Button(control_frame, image=previous_btn_image,
                      borderwidth=0, command=previous_music)
next_btn = Button(control_frame, image=next_btn_image,
                  borderwidth=0, command=next_music)

# layout of buttons and button order in rowise
previous_btn.grid(row=0, column=0, padx=7, pady=10)
play_btn.grid(row=0, column=1, padx=7, pady=10)
pause_btn.grid(row=0, column=2, padx=7, pady=10)
next_btn.grid(row=0, column=3, padx=7, pady=10)

# Call the mainloop of Tk.
root.mainloop()
