import os

import PySimpleGUI as sg
from pytube import YouTube

from config import DEFAULT_DIR

# Set save directory
if DEFAULT_DIR == "":
    default_dir = os.getcwd() + "/data"
else:
    default_dir = DEFAULT_DIR

# Set window layout
sg.theme("LightGreen5")
layout = [
    [sg.Text("Video URL"), sg.InputText(key="link", size=(40, 1))],
    [
        sg.Text("Resolution"),
        sg.Combo(["360p", "480p", "720p", "1080p"], default_value="720p", key="res"),
    ],
    [
        sg.Text("Save Folder"),
        sg.Input(key="save_dir", default_text=default_dir, size=(39, 1)),
        sg.FolderBrowse("Browse", initial_folder=default_dir),
    ],
    [sg.Button("Download", key="download"), sg.Cancel()],
]

window = sg.Window("Video Downloader", layout)

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, "Cancel"):
        break

    elif event == "download":
        link = values["link"]
        res = values["res"]
        save_dir = values["save_dir"]

        try:
            yt = YouTube(link)
            videos = yt.streams.filter(res=res, file_extension="mp4")

        except Exception as e:
            sg.popup(
                f"Invalid URL. Please try again.\nError message: {e}", title="Error"
            )
            continue

        if save_dir == "":
            save_dir = default_dir

        videos = videos.first()
        videos.download(save_dir)

        _continue = sg.popup_yes_no(
            "Download Complete!\n\nDo you want to download another video?",
            title="Success",
        )
        if _continue == "No":
            break
        else:
            continue
