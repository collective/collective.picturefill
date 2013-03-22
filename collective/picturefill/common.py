

def getPictures(base_url, sizes):
    """Return a list of pictures.
    A picture: {'src': base_url/thumb, 'media': "(max-width: 300px)"}
    """
    pictures = []
    widths = []
    names = {}
    for name in sizes:
        width = sizes[name][0]
        widths.append(width)
        names[str(width)] = name
    widths.sort()
    noscript = ""
    previous = None
    for width in widths:
        name = names[str(width)]
        if width >= 128 and not noscript:
            noscript = base_url + name
            previous = width
            continue
        if not previous:
            continue
        media = "(min-width: %spx)" % (previous + 1)
#        media = "(min-width: %spx)" % width
#        media = "(max-width: %spx)" % width
        image = {'src': base_url + name, 'media': media}
        pictures.append(image)
        previous = width
    media = "(min-width: %spx)" % (widths[-1] + 1)
    image = {'src': base_url[:-1], 'media': media}
    pictures.append(image)

    #try to find a width > 128px for the noscript image
    return pictures, noscript
