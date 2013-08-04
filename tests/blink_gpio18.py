import mmio

iomem = mmio.mmiof_init(0x18040000)
mmio.mmiof_write(iomem, 0x00, 0x00046cff)

while True:
  mmio.mmiof_write(iomem, 0x0C, 0x00042605)
  mmio.mmiof_write(iomem, 0x10, 0x00042605)
