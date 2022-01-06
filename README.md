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

Default destination folder is `<repository>/data`.
You can change it by specifying `DEFAULT_DIR` in `config.py`.


## App (For MacOS)
You can also applicationize this script.
```
python setup.py py2app
```
If you generate an app, you must set `DEFAULT_DIR` and it must be an absolute path.
