import mmio

gpio_base = 0x18040000

offset_gpio_oe    = 0x00
offset_gpio_read  = 0x04
offset_gpio_out   = 0x08
offset_gpio_set   = 0x0C
offset_gpio_clear = 0x10

def read(pin):
  oe_mask = mmio.mmio_read(gpio_base + offset_gpio_oe)
  oe_mask = oe_mask & ~(1 << pin)
  mmio.mmio_write(gpio_base + offset_gpio_oe, oe_mask)

  ret = mmio.mmio_read(gpio_base + offset_gpio_oe)
  ret2 = (ret and 1 << pin) >> pin
  return ret2


def write(pin, value):
  oe_mask = mmio.mmio_read(gpio_base + offset_gpio_oe)
  oe_mask = oe_mask | (1 << pin)
  mmio.mmio_write(gpio_base + offset_gpio_oe, oe_mask)

  if value==0:
    mmio.mmio_write(gpio_base + offset_gpio_clear, (1 << pin))
  elif value==1:
    mmio.mmio_write(gpio_base + offset_gpio_set, (1 << pin))
