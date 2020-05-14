# Physics Science Fair Project 2020
### "Electric Catapult"
A project aimed at exploring Projectile Motion with a Raspberry Pi and Servo Motor; easily controlled with a bare-bones website.

---

## Prerequisites
1. Raspberry Pi Model B (recommended)
2. Servo Motor
3. Mini jumper cables.

```bash 
pip3 install flask 
```
## Usage
1. Connect servo control Jumper to **PIN 3** (Board Numbering)
2. Make sure the Pi and Servo Motor along with the battery pack are commonly grounded.
3. Run the program.
```bash
python3 catapultSite.py
```

4. Open local web browser and navigate to localhost.

```
localhost:5000
```

## Contributing
Pull requests are welcome.

## License

MIT License

Copyright (c) 2020 Paul Biernat

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
