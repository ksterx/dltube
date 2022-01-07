from os.path import expanduser

import PySimpleGUI as sg
from pytube import YouTube

from config import DEFAULT_DIR

# Set save directory
if DEFAULT_DIR == "":
    default_dir = expanduser("~") + "/Downloads"
else:
    default_dir = DEFAULT_DIR

# Set window layout
sg.theme("LightGreen5")
left_size = (10, 1)
layout = [
    [sg.Text("Video URL", size=left_size), sg.InputText(key="link", size=(40, 1))],
    [sg.Text("File Name", size=left_size), sg.InputText(key="filename", size=(40, 1))],
    [
        sg.Text("Resolution", size=left_size),
        sg.Combo(
            ["360p", "480p", "720p", "1080p"],
            default_value="720p",
            key="res",
            size=(5, 1),
        ),
    ],
    [
        sg.Text("File Type", size=left_size),
        sg.Combo(["mp4", "webm"], default_value="mp4", key="ext", size=(5, 1)),
    ],
    [
        sg.Text("Save Folder", size=left_size),
        sg.Input(key="save_dir", default_text=default_dir, size=(40, 1)),
        sg.FolderBrowse("Browse", initial_folder=default_dir),
    ],
    [sg.Text("")],
    [sg.Text("", size=(19, 1)), sg.Button("Download", key="download"), sg.Cancel()],
]

window = sg.Window("Video Downloader", layout)

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, "Cancel"):
        break

    elif event == "download":
        link = values["link"]
        ext = values["ext"]
        res = values["res"]
        save_dir = values["save_dir"]
        filename = values["filename"]

        try:
            yt = YouTube(link)
            videos = yt.streams.filter(res=res, file_extension=ext)

        except Exception as e:
            sg.popup(
                "Invalid URL. Please try again."
                # f"\nError message: {e}", title="Error"  # for debugging
            )
            continue

        if save_dir == "":
            save_dir = default_dir
        if filename == "":
            filename = yt.title + "." + ext
        else:
            filename = filename + "." + ext

        videos = videos.first()
        videos.download(save_dir, filename=filename)

        _continue = sg.popup_yes_no(
            "Download Complete!\nDo you want to download another video?",
            title="Success",
        )
        if _continue == "No":
            break
        else:
            continue
