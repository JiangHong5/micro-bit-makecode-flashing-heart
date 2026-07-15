interval = 200
music.ring_tone(1320)
basic.pause(interval)
music.ring_tone(262 * 4)
basic.pause(interval)
music.ring_tone(1320)
basic.pause(interval)
music.ring_tone(262 * 4)
basic.pause(interval)
music.stop_all_sounds()

def on_forever():
    basic.show_leds("""
        . # # # #
        # . . . .
        . # # # .
        . . . . #
        # # # # .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        # # # # .
        # . . . #
        # # # # .
        # . . . #
        # # # # .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
basic.forever(on_forever)
