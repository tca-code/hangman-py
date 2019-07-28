from color import black, yellow, cyan, magenta

def render_noose(count = 0):
    noose = " "
    head = " "
    left_arm = " "
    torso = " "
    right_arm = " "
    left_leg = " "
    right_left = " "

    if count > 0:
        noose = "|"
    if count > 1:
        head = magenta("0")
    if count > 2:
        left_arm = yellow("/")
    if count > 3:
        torso = yellow("|")
    if count > 4:
        right_arm = yellow("\\")
    if count > 5:
        left_leg = cyan("/")
    if count > 6:
        right_left = cyan("\\")
        head = magenta("X")

    top_row = "   +---+"
    noose_row = str.format("\n   %s   |" % noose)
    head_row = str.format("\n   %s   |" % head)
    torso_row = str.format("\n  %s%s%s  |" % (left_arm, torso, right_arm))
    leg_row = str.format("\n  %s %s  |" % (left_leg, right_left))
    bottom_row = "\n       |\n==========\n"
    
    print(top_row + noose_row + head_row + torso_row + leg_row + bottom_row)
    