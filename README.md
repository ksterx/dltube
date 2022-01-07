# Download YouTube Video from URL
---

![app](images/ui.png)

## Prerequisites
```
pip install pytube pysimplegui
```

## Usage
```
python get_video.py
```

Default destination folder is `~/Downloads/`.
You can change it by specifying `DEFAULT_DIR` in `config.py`.


## App (for MacOS)
<img src="images/icon.png" width="30%">

You can also build an app. `py2app` is required.
```
python setup.py py2app
```
If you generate an app, you must set `DEFAULT_DIR` and it must be an absolute path.
