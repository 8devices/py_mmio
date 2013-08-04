py_mmio
=======
Python mmio package for Carambola2

Make binaries
=============
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
wget https://github.com/Lukse/py_mmio/raw/master/src/mmio.py
wget https://github.com/Lukse/py_mmio/raw/master/src/_mmio.so
wget https://github.com/Lukse/py_mmio/raw/master/tests/blink_gpio18.py
python blink_gpio18.py
</pre>

Speed comparison
================
Test scenario:
* Written in C main() <b>freq = 7.6 MHz</b>
* Python slow example <b>freq = 4 Khz</b>
* Python fast example <b>freq = 26 kHz</b>
 
Manual toggle GPIO18
====================
Read current values

<pre>
io -4 -r 0x18040000 -> 18040000:  00006cff
io -4 -r 0x1804000C -> 1804000c:  00002605
io -4 -r 0x18040010 -> 18040010:  00002605
</pre>

Toggle led
<pre>
io -4  0x18040000 0x00046cff <- setup out
io -4  0x1804000C 0x00042605 <- set
io -4  0x18040010 0x00042605 <- clr
</pre>

