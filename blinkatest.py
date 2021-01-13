import board
import digitalio
import busio

print("Hello blinka!")

#Try to create a Digital Input
pin = digitalio.DigitalInOut(board.D4)
print("Digiral IO ok!")

#try to create an I2C device
i2c = busio.I2C(board.SCL, board.SDA)
print("I2C ok!")

#try to create an SPI device
spi = busio.SPI(board.SCLK, board.MOSI, board.MISO)
print("SPI ok!")

print("done!")
