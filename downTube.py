import customtkinter as ct
from tkinter import PhotoImage
from pytube import YouTube, exceptions
from time import sleep

def Download():
    try:
        link = inputs.get()
        yt = YouTube(link, on_progress_callback=progressBarr)
        download = yt.streams.get_highest_resolution()
        download.download('Video')
        sleep(1.2)
        noLinkError.configure(text='Successfully Downloaded ✔️', text_color='green')
    except exceptions.RegexMatchError:
        noLinkError.configure(text='Enter Video Link ❌', text_color='red')

def progressBarr(stream, _, bytes):
    sizeTotal = stream.filesize
    bytesDownload = sizeTotal - bytes
    percent = bytesDownload / sizeTotal * 100
    p = str(int(percent))
    noLinkError.configure(text=f'Downloading {p}' + '%...')
    noLinkError.update()

ct.set_appearance_mode('dark')

window = ct.CTk()
window.resizable(False, False)
window.geometry('600x420')
window.iconbitmap(r'assets\\images\\icon.ico')
window.title('DownTube')

image = PhotoImage(file=r'assets\\images\\icone2.png')

label_img = ct.CTkLabel(master=window, image=image)
label_img.place()

tela = ct.CTkLabel(window,
    text=None,
    height=100,
    image=image)
tela.pack(padx=10, pady=10)

inputs = ct.CTkEntry(
    master=window,
    border_color='cyan',
    width=200,
    placeholder_text='URL')
inputs.pack(padx=10, pady=10)

noLinkError = ct.CTkLabel(window, text='')
noLinkError.pack()

button = ct.CTkButton(
    master=window,
    text_color='#F8F8FF',
    fg_color='grey',
    hover_color='#40E0D0',
    width=110,
    text='Baixar',
    command=Download)
button.pack(padx=10, pady=10)

window.mainloop()


    