py_mmio
=======
Python mmio package for Carambola2. With this module you can access all internal registers. You can do some magic with this tool, but it's very easy to do something very wrong if you don't know what are you doing. Be warned!

Make binaries
=============
* You need to have carambola2 build environment installed and precompilled prior to building this package
* You might need to edit Makefile first line to meet your environment
<pre>
CROSS_COMPILE = ~/carambola2/staging_dir/toolchain-mips_r2_gcc-4.7-linaro_uClibc-0.9.33.2/bin/mips-openwrt-linux-
</pre>

Also some packages should be selected from
<pre>make menuconfig</pre>
  * Languages
    * Pyton
      * python
      * python-mini


Build python package
<pre>make python</pre>

Build test program - main()
<pre>make test</pre>

Perform quick test run on Carambola2
=======================================
Note: you need wget with SSL support

<pre>
cd /tmp/py_mmio
rm mmio.py
rm _mmio.so
wget https://github.com/8devices/py_mmio/raw/master/src/mmio.py
wget https://github.com/8devices/py_mmio/raw/master/src/_mmio.so
wget https://github.com/8devices/py_mmio/raw/master/tests/blink_gpio18.py
python blink_gpio18.py
</pre>

Speed/Jitter comparison
=======================
* C main() <b>freq = 7.6 MHz</b> NOTE: my logic analyzer is not fast enough to capture waveform
![1](/tests/images/mmio_fast.png)

* C main(), usleep(10) <b>freq = 7.13 KHz</b>
![2](/tests/images/c_usleep\(10\).png)

* Python slow example <b>freq = 4 Khz</b>
![3](/tests/images/python_slow.png)

* Python fast example <b>freq = 26 kHz</b>
![4](/tests/images/python_fast.png)

 
Manual toggle GPIO18
====================
Read current values:
<pre>
io -4 -r 0x18040000 -- 18040000:  00006cff
io -4 -r 0x1804000C -- 1804000c:  00002605
io -4 -r 0x18040010 -- 18040010:  00002605
</pre>

Toggle led:
<pre>
io -4  0x18040000 0x00046cff -- setup out
io -4  0x1804000C 0x00042605 -- set
io -4  0x18040010 0x00042605 -- clr
</pre>

Control GPIO using simple python functions
==========================================
<pre>
import gpio

register = gpio.read(18)
print "Read: 0x%08X" % register

gpio.write(18, 1)
</pre>
