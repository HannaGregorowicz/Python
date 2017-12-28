def hex_na_rgb(h):
    h = h.lstrip('#')
    rgb = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    return rgb
def rgb_na_hex(r, g, b):
    x = hex(r)+hex(g)+hex(b)
    x = x.replace('0x', '')
    y = "#"+x
    return y

