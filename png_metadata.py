from PIL import Image
from PIL.PngImagePlugin import PngInfo


def _write_text(metadata, args, exclude=None):
    if not args:
        return

    for key, item in args.items():
        if exclude and key in exclude:
            continue

        value = ''
        zip_ = False
        if isinstance(item, dict):
            value = item['value']
            if 'zip' in item: zip_ = item['zip']
        else:
            value = item
        metadata.add_text(key, value, zip=zip_)


def add_metadata(filename, keyValues, output=None):
    image = Image.open(filename)
    if not image:
        raise Exception('add_metadata: cannot open \'' + str(filename) + '\'')

    if not keyValues:
        raise Exception('add_metadata: \'keyValues\' is null or empty')

    metadata = PngInfo()
    
    _write_text(metadata, image.text)
    _write_text(metadata, keyValues)

    if not output:
        output = filename

    image.save(output, pnginfo=metadata)


def remove_metadata(filename, keys, output=None):
    image = Image.open(filename)
    if not image:
        raise Exception('remove_metadata: cannot open \'' + str(filename) + '\'')

    if not keys:
        raise Exception('remove_metadata: \'keys\' is null or empty')

    metadata = PngInfo()
    
    _write_text(metadata, image.text, exclude=keys)

    if not output:
        output = filename

    image.save(output, pnginfo=metadata)


def clear_metadata(filename, output=None):
    image = Image.open(filename)
    if not image:
        raise Exception('clear_metadata: cannot open \'' + str(filename) + '\'')

    metadata = PngInfo()

    if not output:
        output = filename

    image.save(output, pnginfo=metadata)


def print_metadata(filename):
    image = Image.open(filename)
    if not image:
        raise Exception('print_metadata: cannot open \'' + str(filename) + '\'')

    print(image.text)


# -------------------------------------------------------------------
# COMMAND
# -------------------------------------------------------------------
if __name__ == '__main__': 
    # NOTE: check args

    def help():
        print('=========================================')
        print('usage: python png_metadata.py MODE FILENAME [METADATAS and --OPTIONS...]')
        print('-----------------------------------------')
        print('PARAMETERS')
        print('')
        print('\tMODE: a | r | c | p')
        print('\t\ta: Add metadata')
        print('\t\tr: Remove metadata')
        print('\t\tc: Clear metadata')
        print('\t\tp: Print metadata')
        print('')
        print('\tFILENAME: PNG filename')
        print('')
        print('-----------------------------------------')
        print('METADATAS')
        print('')
        print('\t\tAdd mode:\t"KEY=VALUE"')
        print('\t\tRemove mode:\t"KEY" only')
        print('\t\tClear mode:\tunused')
        print('\t\tPrint mode:\tunused')
        print('')
        print('-----------------------------------------')
        print('--OPTIONS')
        print('')
        print('\t(-o) --output=OUTPUT_FILENAME (default: None)')
        print('\t\tPrint mode:\tignored')
        print('')
        print('\t(-z) --zip (default: False)')
        print('\t\tClear mode:\tignored')
        print('\t\tPrint mode:\tignored')
        print('')
        print('\t(-v) --verbose (default: False)')
        print('')
        print('=========================================')
        print('')
        exit()

    def error():
        print('Try -h (or --help) for more information.')
        exit()

    import sys
    argIndex = 0
    argCount = len(sys.argv)

    if argCount < 3 or '-h' == sys.argv[1] or '--help' == sys.argv[1] or '--h' == sys.argv[1] or '-help' == sys.argv[1]:
        help()

    argIndex += 1
    MODE = sys.argv[argIndex].lower()
    if 'a' != MODE and 'r' != MODE and 'c' != MODE and 'p' != MODE:
        help()

    argIndex += 1
    FILENAME = sys.argv[argIndex]


    # NOTE: metadatas and options

    METADATAS = {}
    OUTPUT = None
    ZIP = False
    VERBOSE = False

    argIndex += 1
    for n in range(argIndex, argCount):
        argIndex = n
        arg = sys.argv[argIndex]

        if -1 != arg.find('='):
            key, value = arg.split('=')
        else:
            key = arg
            value = None

        if '-' != arg[0]:

            if 'a' == MODE:
                if '\\n' in value:
                    value = value.replace('\\n', '\n')
                METADATAS[key] = value
            
            elif 'r' == MODE:
                METADATAS[key] = None

        else:
            keylower = key.lower()

            if '-o' == key or '--output' == keylower:
                OUTPUT = value

            elif '-z' == key or '--zip' == keylower:
                ZIP = True

            elif '-v' == key or '--verbose' == keylower:
                VERBOSE = True

            else:
                print('ERROR!!!')
                print('UNKNOWN_OPTION:' + key)
                error()


    # NOTE: execute

    if ZIP:
        METADATAS_OLD = METADATAS
        METADATAS = {}
        for key, item in METADATAS_OLD.items():
            METADATAS[key] = {'value': item, 'zip': True}

    if VERBOSE:
        print('MODE:' + str(MODE))
        print('FILENAME:' + str(FILENAME))
        print('METADATAS:' + str(METADATAS))
        print('OUTPUT:' + str(OUTPUT))
        print('ZIP:' + str(ZIP))

    if 'a' == MODE: add_metadata(filename=FILENAME, keyValues=METADATAS, output=OUTPUT)
    elif 'r' == MODE: remove_metadata(filename=FILENAME, keys=METADATAS, output=OUTPUT)
    elif 'c' == MODE: clear_metadata(filename=FILENAME, output=OUTPUT)
    elif 'p' == MODE: print_metadata(filename=FILENAME)
