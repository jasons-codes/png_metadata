# png_metadata.py
png_metadata.py is implemented using [Pillow](https://pillow.readthedocs.io/en/stable/index.html)

Supported features
-------------
- Support reading/writing 'tEXt' and 'zTXt'

- Support command line interface
(using: python png_metadata.py -h)

- Support import png_metadata in Python (path must be correct)


Limitations
-------------
- 'iTXt' editing and function to insert special cid chunk are not provided. (You can implement it through [PIL.PngImagePlugin.PngInfo](https://pillow.readthedocs.io/en/stable/PIL.html#pngimageplugin-pnginfo-class) if needed)
