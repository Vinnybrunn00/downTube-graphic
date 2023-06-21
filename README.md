# DownTube

## Installing dependencies

```bash
> pip install -r requirements.txt
```

## Building executable

```bash
> pyinstaller --onedir --add-data "path Customtkinter" --noconsole --icon=icon.png downTube.py
```

## Path Customtkinter required

- You find the `path customtkinter` in the root folder of python in  `C:\Python311\Lib\site-packages\customtkinter`

```
> --add-data C:\Python311\Lib\site-packages\customtkinter
```
