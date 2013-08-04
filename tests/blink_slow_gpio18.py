import mmio

mmio.mmio_write(0x18040000, 0x00046cff)

while True:
  mmio.mmio_write(0x1804000C, 0x00042605)
  mmio.mmio_write(0x18040010, 0x00042605)
