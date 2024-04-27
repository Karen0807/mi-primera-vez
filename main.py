basic.show_leds("""
    . . . . .
    . . . . .
    . . # . .
    . . . . .
    . . . . .
    """)
ax = 0

def on_forever():
    global ax
    ax += input.acceleration(Dimension.X)
    if ax > 818 and ax < 1023:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . #
            . . . . .
            . . . . .
            """)
    elif ax > 408 and ax < 818:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . # .
            . . . . .
            . . . . .
            """)
    elif ax > -409 and ax < 409:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
    elif ax > -818 and ax < -409:
        basic.show_leds("""
            . . . . .
            . . . . .
            . # . . .
            . . . . .
            . . . . .
            """)
    else:
        basic.show_leds("""
            . . . . .
            . . . . .
            # . . . .
            . . . . .
            . . . . .
            """)
basic.forever(on_forever)
