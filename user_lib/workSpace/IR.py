# More details can be found in TechToTinker.blogspot.com 
# George Bantique | tech.to.tinker@gmail.com

from machine import Pin
from ir_tx import NEC

nec = NEC(Pin(26, Pin.OUT, value = 0))

#nec.transmit(<addr>, <data>)

