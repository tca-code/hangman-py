def gray(txt):
    (start, end) = init(90, 39)
    return start + txt + end

def red(txt):
    (start, end) = init(31, 39)
    return start + txt + end

def black(txt):
    (start, end) = init(30, 39)
    return start + txt + end

def cyan(txt):
    (start, end) = init(36, 39)
    return start + txt + end

def yellow(txt):
    (start, end) = init(33, 39)
    return start + txt + end

def magenta(txt):
    (start, end) = init(35, 39)
    return start + txt + end

def bg_white(txt):
    (start, end) = init(47, 49)
    return start + txt + end

def italic(txt):
    (start, end) = init(3, 23)
    return start + txt + end

def init(start, end):
    return ("\x1b[" + str(start) + "m", "\x1b[" + str(end) + "m")