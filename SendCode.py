def my_function():
    radio.send_number(8)
gamerbit.on_event(GamerBitPin.P8, GamerBitEvent.UP, my_function)

def my_function2():
    radio.send_number(2)
gamerbit.on_event(GamerBitPin.P0, GamerBitEvent.UP, my_function2)

# ---

def my_function3():
    radio.send_number(3)
gamerbit.on_event(GamerBitPin.P1, GamerBitEvent.DOWN, my_function3)

def my_function4():
    radio.send_number(6)
gamerbit.on_event(GamerBitPin.P2, GamerBitEvent.UP, my_function4)

def my_function5():
    radio.send_number(4)
gamerbit.on_event(GamerBitPin.P1, GamerBitEvent.UP, my_function5)

# --

def my_function6():
    radio.send_number(7)
gamerbit.on_event(GamerBitPin.P8, GamerBitEvent.DOWN, my_function6)

# --

def my_function7():
    radio.send_number(5)
gamerbit.on_event(GamerBitPin.P2, GamerBitEvent.DOWN, my_function7)

# ---

def my_function8():
    radio.send_number(1)
gamerbit.on_event(GamerBitPin.P0, GamerBitEvent.DOWN, my_function8)

radio.set_group(15)

def on_forever():
    pass
basic.forever(on_forever)
