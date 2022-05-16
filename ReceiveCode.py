def on_received_number(receivedNumber):
    if(receivedNumber==1):
        motobit.enable(MotorPower.ON)
        motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 50)
        motobit.set_motor_speed(Motor.RIGHT, MotorDirection.FORWARD, 50)
    elif(receivedNumber==2):
        motobit.enable(MotorPower.OFF)
        motobit.enable(MotorPower.OFF)
        motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 0)
        motobit.set_motor_speed(Motor.RIGHT, MotorDirection.FORWARD, 0)
    elif(receivedNumber==3):
        motobit.enable(MotorPower.ON)
        motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 50)
        motobit.set_motor_speed(Motor.RIGHT, MotorDirection.FORWARD, 50)
    elif(receivedNumber==2):
        motobit.enable(MotorPower.OFF)
        motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 0)
        motobit.set_motor_speed(Motor.RIGHT, MotorDirection.FORWARD, 0)
    elif(receivedNumber==5):
        motobit.enable(MotorPower.ON)
        motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 50)
        motobit.set_motor_speed(Motor.RIGHT, MotorDirection.FORWARD, 50)
    elif(receivedNumber==6):
            motobit.enable(MotorPower.OFF)
            motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 0)
            motobit.set_motor_speed(Motor.RIGHT, MotorDirection.FORWARD, 0)
    elif(receivedNumber==7):
        motobit.enable(MotorPower.ON)
        motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 50)
        motobit.set_motor_speed(Motor.RIGHT, MotorDirection.FORWARD, 50)
    elif(receivedNumber==8):
        motobit.enable(MotorPower.OFF)
        motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 0)
        motobit.set_motor_speed(Motor.RIGHT, MotorDirection.FORWARD, 0)
radio.on_received_number(on_received_number)

def on_forever():
    pass
basic.forever(on_forever)
