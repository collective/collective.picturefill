

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
    for width in widths:
        if width > 128 and not noscript:
            noscript = base_url + name
        name = names[str(width)]
        image = {'src': base_url + name, 'media': "(max-width: %spx)" % width}
        pictures.append(image)
    image = {'src': base_url[:-1], 'media': "(min-width: %spx)" % widths[-1]}
    pictures.append(image)

    #try to find a width > 128px for the noscript image
    return pictures, noscript
