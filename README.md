<p align="center">
  <img src="https://media.discordapp.net/attachments/972533899462836334/1135945103383482419/5DC7677E-4B7F-4486-9F0D-FCE8B73214D4.gif">
</p>

<p align="center">
  <a href="https://www.python.org">
    <img src="https://img.shields.io/badge/Python-3.11-blue">
    <img src="https://img.shields.io/badge/Version-1.0-success">
    <img src="https://img.shields.io/badge/License-MIT-important"> 
    <img src="https://img.shields.io/github/stars/23Savagee/Kurta-?style=flat&color=red">
  </a>
  <a href="https://github.com/23Savagee/Kurta-">
    <img src="https://visitor-badge.laobi.icu/badge?page_id=23Savagee.Kurta-" /></a>
    
  </a> 

## 🔐 〢 What is Kurta?
Kurta Obfuscator is a Python script that allows you to obfuscate Python code. Obfuscation is a technique used to make the code harder to read and understand while retaining its functionality. This can be useful for protecting your code from reverse engineering or for other security reasons.

## 📁 〢 Features

- Obfuscate Python code to make it more challenging to understand.
- Generates obfuscated code that retains functionality.
- Simple command-line interface.

## 📝 〢 Usage
1. Clone this repository or download the `main.py` script.
2. Run  `kurta.bat ` to install all libraries
3. Run the script using Python:

   ```bash
   python main.py
   ```
### 💥 〢 Key Features:
```diff
+ Option to obfuscate a Python script by providing the path to the script file you want to obfuscate.
+ The obfuscated code will be saved in a file with a "obf-" prefix in the "build" folder.

@@ Some Small Bugs can and do appear@@
```
## 🖤〢 Example

**Unobfuscated**:<br>
```python3
def add(a, b):
    result = a + b
    return result

def subtract(a, b):
    result = a - b
    return result

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operation = input("Select an operation (+ or -): ")

if operation == "+":
    result = add(num1, num2)
    print(f"The sum of {num1} and {num2} is equal to {result}")
elif operation == "-":
    result = subtract(num1, num2)
    print(f"The subtraction of {num1} and {num2} is equal to {result}")
else:
    print("Invalid operation")
```
**Obfuscated**:<br>
```python3
__________ = eval(getattr(__import__(bytes([98, 97, 115, 101, 54, 52]).decode()),bytes([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(bytes([90, 88, 90, 104, 98, 65, 61, 61])).decode());___________ = __________(getattr(__import__(bytes([98, 97, 115, 101, 54, 52]).decode()),bytes([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(bytes([90, 50, 86, 48, 89, 88, 82, 48, 99, 103, 61, 61])).decode());_______________ = __________(getattr(__import__(bytes([98, 97, 115, 101, 54, 52]).decode()),bytes([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(bytes([88, 49, 57, 112, 98, 88, 66, 118, 99, 110, 82, 102, 88, 119, 61, 61])).decode());________________ = __________(getattr(__import__(bytes([98, 97, 115, 101, 54, 52]).decode()),bytes([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(bytes([89, 110, 108, 48, 90, 88, 77, 61])).decode());____________ = lambda ______________: __________(___________(_______________(________________([98, 97, 115, 101, 54, 52]).decode()),________________([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(________________([89, 50, 57, 116, 99, 71, 108, 115, 90, 81, 61, 61])).decode())(______________, ___________(_______________(________________([98, 97, 115, 101, 54, 52]).decode()),________________([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(________________([80, 72, 78, 48, 99, 109, 108, 117, 90, 122, 52, 61])).decode(), ___________(_______________(________________([98, 97, 115, 101, 54, 52]).decode()),________________([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(________________([90, 88, 104, 108, 89, 119, 61, 61])).decode());________ = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3\xe0\n\x01\x04r]\x00/\xea\x0bDD\x93\x847\x10f\x1a\xc1Q/y\xed\xc8\x1ff\xb4\x82\xd5\x0eS\xed\xa1\xd5\x03\xa3>bio\x94@t\xe2$\x16jsv\xa2A\x00w\x9d{u46iD\x9f\xfa\xaf\\eb\xc2\xcf\xc3\xb8o\x0b\x83P\x8881\xb1\xd2\x19#n\x13\x19Qb\xc4\xe0N\x95\x8ac\xc3e\x14\xaf\xa5\xc9\xfd\xf2\xda#\xb1Z\xa9\xe8V(\xe4\xf0.P\xbck\x81k\xb3\xe9\x82\x11\nD\xed*P\\\x9b\x95\xf2\xbdJ\xac:g\xfd\xc0v\x91\xa5Ont\x8b\xddP\xe7\xbac\xa0\x04\x83\xbdH\x11\x02\xa9\xd1\x80\xea\x88,\n\x96\x9c\xbcr\x06\x0el\xd9\xb1\x92\x08\xa9\n\xcd\x1aZB\xe7`|f9\xe0\xa0\x9do\xf9t_s\x99\x16*(\xc5\xba\x0e\xd1\x8f;\x1bj7sc:\xce\xa7\t\xa2\xed\xaa\xf1\xad\x92\xd7\x15\xb2\x13\x8d!_\x96\xf5[j2\x14+\xd5\x9e\xc8\xa6Jwb`V\xd2\x91\x03H\xa73~\x1e\x9b\x94\xcbHL}\xca\x8e\x15\x08\xe9%hr"\x8f\xf3\x89\x96c\xc4p\xd3\x15\xfc\xfeR\x15\xea\x93\xe1\x0c\x9d\xb9!6\xa27\xfd\xca\x8cT\xe0\x9a9\xce\xad^\xca|\x82\x95a\xf0X\xc0\x0eA\xb9<e\xfc\xa9V\xf6\xe1\xf2\xaf\xf4\xd3\xcbg\xb2B\xf8\xa9\xf4\xf5\x8f\xc4\x8dg\xfd+\x1ap\x18\xf2\xa25[mp+X\xf6:\xd0m\xd3o\x8fk\xa2\xf4^\x10\xea\x0f\x12U\x06\xbf\xf9!\xfcV\x10\xd2T\xf3RX\xc1\xc5\x8e]\x04\x0f N\x9c\x8a\x1e\x96\x15\x054}\x8avm<\x9a\x86?Y\xa2\'\xa01\xb8\x9fes\x16?\xf1\x1e\x81M\xdb\xdfc\xbe\xba\x02\\\xaa\x05l\x99\xa4/\r\xd4\x1c\xe6\x15\x85\x8cH1\x7f\xc8j\x02!\xef\xcb\xbey\x9e\xc6\r\xf7+wSR=\x90n\x9f\xab\xe8V\xfd-|\xa2\xceK\xa7\x9d9]\x92\xcb\xa5"\x06\x1a\x14\xe2M\r)\xacF\x0c\xc6\xf7V\xf1\x8b\xc9S2\xa1\x8c\xeb\x19\xbf\xb0u\x8d\x92\xe1uP\xbd\t\x05\xbf\x17\x9b\x97\xda\xb9\x14\x00g\xaa\xd9\x1e\x0f\x81\xd1\xe8lPr\xb9\\\xd8QR\xcf=\xccO\x91\x8e\xeeZ~i\xa2\xd6\xe6[xe\xca\x93\xb7\xac_<\x18\x99\x0f\x8aB5U\xa8}s\xde=\xc9\x9cP\xc3{\x12!\xccM\x7f\x04j\x07f\x14\x1e\xf97\x1f*\x7f\xb8T4\x94;\xf3!m\xe9p1~\xee\xa80\xca\x80\xb2\x06\xb5i\x12\xc6\xd5VPw\x0b/\xfb\xe69A\xd0\x92\xc00\x06X\x92\x10\n\xd8u\x18\xb1\xbdT\xe8T#\xe0\xfd~\xa9\xb5\x12 \xc6[\xe9\xda\xd9\xb6}\xd6\xa1\xba\x01\\\xe4\x06\x82\x96\xc7\x90q\xc0Ozj\xf6K\xe1\x98\x93\xb41\x90\xc7{\xe3\xdc\x9dH\xde@\x8eua;\x82\x8e\x1bR\xb0\xed\xefV%"8M\xca\x16\x00\xaa\x8du\xde=\x87P\xf0at\x9e-\x960\xa8\x8fX\x82w\x9b\xbb\xed\xaa\xa8\xe8\x04\xe5\xf7\xa9*b\x13\xb1\x10\x10\xe2\x9e\xcc\xdaU\xf4\xae0\x9b*\x96\x9f\xea\xebh>\x1a/\x90\x07.\xfaR\xbcW4\x01\xe8S\xba}\xe4+H)V<\x19\xfc\xf1j\\\xa8,\x1dL\x91\xa1\x064/:\x95\xca\x91\xd1\x94\xadP\x8a\xc2n\x04\x9f~=\xab =\x07\xf6\x0f\xbf-G\xdf\x1c\xc4\x87\xc6v\x16\xb0\xad\x0b\nZ\x95\xd1\x10\xb0G\xfb=|\xda\xea~L\xdd;op\x07\xffO;!\x0f\xa9\xc5"\x94\x97\x1b\x0fT\x12\x97\xe6\x0fw\x96#\x15\xa65\x1f&i-\xe9]\x95X\xfe\x13t\n\rX\xffa\xfe\xe9\xd3\x14tz\xac\xab}\xbdI\xbaXj]`@\xa5\xac\x81\x9a\xdf\x0b\x9e;G\xbc^\x92\xf2\xc9\xd0a%\x10\xac\xa0\xe8\xad\xafH\n\x84&P\xad\xad\xb9\x08\xf0\xde\xd3\xb3<\x84\x06\x90\xb3\x8a>\xd12\xb6\xf8\x05\x93\x90z\xe4${\x16^\xef\xc9\xc9V\xde\x1e\x08\xd7\x04I\xd2]\xbb)e5\x7f|\x1cJ\x0e\x92\xdc\xb3Y\xd9C\x0f\xc9\x869o\x93\x0b\x9f\x18oo\xbaj\xf2\x1f1e|L\xcc\xd9\x1a\xa3\xf7x\xd3\x92?>\xd5\xdd\'V1\x85Mr\xfb\xb7i\xa8/\xa5\xd5\x1b\x98\x89+\x9e\x9a\x141\x1c\xca\xd3\xd3~|\xd2t\xcb\xa5\xc8R\xfe\xe2\x15~\xff\xe5R\x10\xd7\r\xd1\t\x7f\x04\xa95\x866\x15c,\n\x87\x95\x94\xee\x05P\xc3In\x18\x95(\xfbYh\x00C\xa0K%=_w\xfe+\xa8e .\xeaS\xa9!\x96\xd4P!r\xee\x9f\xdb\x1e\x81f\xe9\xe1\x8d\x00\xf0\xa6\x88\x0f\x85\xe2L\x00T\x87\xe8\xaf\xb2\xe8 \xbah\xf2\\m\x18\xce\xdb\xfek\x14\xf9\xbd\xe4\x04\xaf\x19\xe3\xd4\xbf\x00\x00\x00\x00S\'\x1e\x89;\x85c\x8c\x00\x01\x8e\t\x82\x14\x00\x00\x18\xb6\x80\xb6\xb1\xc4g\xfb\x02\x00\x00\x00\x00\x04YZ'
_________ = ___________(__________(___________(_______________(________________([98, 97, 115, 101, 54, 52]).decode()),________________([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(________________([88, 49, 57, 112, 98, 88, 66, 118, 99, 110, 82, 102, 88, 121, 103, 105, 89, 110, 86, 112, 98, 72, 82, 112, 98, 110, 77, 105, 75, 81, 61, 61])).decode()),___________(_______________(________________([98, 97, 115, 101, 54, 52]).decode()),________________([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(________________([98, 71, 108, 122, 100, 65, 61, 61])).decode())(________)
try:
    ___________(__________(___________(_______________(________________([98, 97, 115, 101, 54, 52]).decode()),________________([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(________________([88, 49, 57, 112, 98, 88, 66, 118, 99, 110, 82, 102, 88, 121, 103, 105, 89, 110, 86, 112, 98, 72, 82, 112, 98, 110, 77, 105, 75, 81, 61, 61])).decode()),___________(_______________(________________([98, 97, 115, 101, 54, 52]).decode()),________________([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(________________([90, 88, 104, 108, 89, 119, 61, 61])).decode())(____________(___________(__________(___________(_______________(________________([98, 97, 115, 101, 54, 52]).decode()),________________([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(________________([88, 49, 57, 112, 98, 88, 66, 118, 99, 110, 82, 102, 88, 121, 103, 105, 98, 72, 112, 116, 89, 83, 73, 112])).decode()),___________(_______________(________________([98, 97, 115, 101, 54, 52]).decode()),________________([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(________________([90, 71, 86, 106, 98, 50, 49, 119, 99, 109, 86, 122, 99, 119, 61, 61])).decode())(________________(_________)))) or ___________(__________(___________(_______________(________________([98, 97, 115, 101, 54, 52]).decode()),________________([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(________________([88, 49, 57, 112, 98, 88, 66, 118, 99, 110, 82, 102, 88, 121, 103, 105, 98, 51, 77, 105, 75, 81, 61, 61])).decode()),___________(_______________(________________([98, 97, 115, 101, 54, 52]).decode()),________________([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(________________([88, 50, 86, 52, 97, 88, 81, 61])).decode())(0)
except ___________(__________(___________(_______________(________________([98, 97, 115, 101, 54, 52]).decode()),________________([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(________________([88, 49, 57, 112, 98, 88, 66, 118, 99, 110, 82, 102, 88, 121, 103, 105, 98, 72, 112, 116, 89, 83, 73, 112])).decode()),___________(_______________(________________([98, 97, 115, 101, 54, 52]).decode()),________________([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(________________([84, 70, 112, 78, 81, 85, 86, 121, 99, 109, 57, 121])).decode()):...
```
## 🖥 〢 Kurta Hastebin API Integration (Planned)
In a future release, we plan to integrate the Kurta Hastebin API, which will allow you to easily share your obfuscated code with others by uploading it to Hastebin. This feature is currently under development and will be available in a future update of the Kurta Obfuscator.

Stay tuned for updates and new features!
## 🦇〢 Preview

![Image 1](https://i.imgur.com/vUdqCgV.png)
![Image 2](https://i.imgur.com/PpFbwCV.png)
