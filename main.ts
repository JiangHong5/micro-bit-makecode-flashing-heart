let interval = 200
music.ringTone(1320)
basic.pause(interval)
music.ringTone(262 * 4)
basic.pause(interval)
music.ringTone(1320)
basic.pause(interval)
music.ringTone(262 * 4)
basic.pause(interval)
music.stopAllSounds()
basic.pause(300)
basic.forever(function () {
    basic.showLeds(`
        . # # # #
        # . . . .
        . # # # .
        . . . . #
        # # # # .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        # # # # .
        # . . . #
        # # # # .
        # . . . #
        # # # # .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
})
