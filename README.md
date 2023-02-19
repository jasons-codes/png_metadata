# png_metadata.py
png_metadata.py is implemented using [Pillow](https://pillow.readthedocs.io/en/stable/index.html)

<br />

Supported features
-------------
* Support for reading/writing 'tEXt' and 'zTXt' chunks of PNG files.

* Support command line interface.
<image src="./commandline.png" width="50%" height="50%">

* Support import png_metadata in Python.
  - add_metadata, remove_metadata, clear_metadata, print_metadata functions are provided.
  - It can be used if the import path matches properly.

<br />

Requirements
-------------
* [Python3](https://www.python.org/downloads/)

* [Pillow](https://pillow.readthedocs.io/en/stable/)

<br />

Limitations
-------------
* 'iTXt' editing and function to insert special cid chunk are not provided.
  - You can implement it through [PIL.PngImagePlugin.PngInfo](https://pillow.readthedocs.io/en/stable/PIL.html#pngimageplugin-pnginfo-class) if needed.
