import string
import base64
import codecs
import os
import random
import sys
from time import time
import argparse
from textwrap import wrap
from lzma import compress
from marshal import dumps
from pystyle import *
from getpass import getpass
from requests import post
from random import choice as _choice, randint as _randint
from sys import argv as _argv

text = r"""


 ▄▀▀▄ █  ▄▀▀▄ ▄▀▀▄  ▄▀▀▄▀▀▀▄  ▄▀▀▀█▀▀▄  ▄▀▀█▄  
█  █ ▄▀ █   █    █ █   █   █ █    █  ▐ ▐ ▄▀ ▀▄ 
▐  █▀▄  ▐  █    █  ▐  █▀▀█▀  ▐   █       █▄▄▄█ 
  █   █   █    █    ▄▀    █     █       ▄▀   █ 
▄▀   █     ▀▄▄▄▄▀  █     █    ▄▀       █   ▄▀  
█    ▐             ▐     ▐   █         ▐   ▐   
▐                            ▐                 
                                                         
            [1] Kurta Obfuscator
            [2] Kurta Hastebin API
            [3] Exit
"""[:-1]

banner = """
                                                 ,::::.._
                                               ,':::::::::.
                                           _,-'`:::,::(o)::`-,.._
                                        _.', ', `:::::::::;'-..__`.
                                   _.-'' ' ,' ,' ,\:::,'::-`'''
                               _.-'' , ' , ,'  ' ,' `:::/
                         _..-'' , ' , ' ,' , ,' ',' '/::
                 _...:::'`-..'_, ' , ,'  , ' ,'' , ,'::|
              _`.:::::,':::::,'::`-:..'_',_'_,'..-'::,'|
      _..-:::'::,':::::::,':::,':,'::,':::,'::::::,':::;
        `':,'::::::,:,':::::::::::::::::':::,'::_:::,'/
        __..:'::,':::::::--''' `-:,':,':::'::-' ,':::/
   _.::::::,:::.-''-`-`..'_,'. ,',  , ' , ,'  ', `','
 ,::SSt:''''`                 \:. . ,' '  ,',' '_,'
                               ``::._,'_'_,',.-'
                                   \\ \\
                                    \\_\\
                                     \\`-`.-'_
                                  .`-.\\__`. ``
                                     ``-.-._
                                         `"""[1:]

banner = Add.Add(text, banner, center=True)

dark = Col.dark_gray
light = Col.light_gray
red = Colors.StaticMIX((Col.red, Col.blue))
bred = Colors.StaticMIX((Col.red, Col.purple, Col.blue))


def p(text):
    # sleep(0.05)
    return print(stage(text))


def stage(text: str, symbol: str = '...', col1=light, col2=None) -> str:
    if col2 is None:
        col2 = light if symbol == '...' else red
    return f""" {Col.Symbol(symbol, col1, dark)} {col2}{text}{Col.reset}"""

class Obfuscator:
    def __init__(self, code, outpath):
        self.code = code.encode()
        self.outpath = outpath
        self.varlen = 3
        self.vars = {}

        self.marshal()
        self.encrypt1()
        self.encrypt2()
        self.finalize()

    def generate(self, name):
        res = self.vars.get(name)
        if res is None:
            res = "_" + "".join(["_" for _ in range(self.varlen)])
            self.varlen += 1
            self.vars[name] = res
        return res

    def encryptstring(self, string, config={}, func=False):
        b64 = list(b"base64")
        b64decode = list(b"b64decode")
        __import__ = config.get("__import__", "__import__")
        getattr = config.get("getattr", "getattr")
        bytes = config.get("bytes", "bytes")
        eval = config.get("eval", "eval")
        if not func:
            return f'{getattr}({__import__}({bytes}({b64}).decode()),{bytes}({b64decode}).decode())({bytes}({list(base64.b64encode(string.encode()))})).decode()'
        else:
            attrs = string.split(".")
            base = self.encryptstring(attrs[0], config)
            attrs = list(map(lambda x: self.encryptstring(x, config, False), attrs[1:]))
            newattr = ""
            for i, val in enumerate(attrs):
                if i == 0:
                    newattr = f'{getattr}({eval}({base}),{val})'
                else:
                    newattr = f'{getattr}({newattr},{val})'
            return newattr

    def encryptor(self, config):
        def func_(string, func=False):
            return self.encryptstring(string, config, func)
        return func_

    def compress(self):
        self.code = compress(self.code)

    def marshal(self):
        self.code = dumps(compile(self.code, "<string>", "exec"))

    def encrypt1(self):
        code = base64.b64encode(self.code).decode()
        partlen = int(len(code) / 4)
        code = wrap(code, partlen)
        var1 = self.generate("a")
        var2 = self.generate("b")
        var3 = self.generate("c")
        var4 = self.generate("d")
        init = [f'{var1}="{codecs.encode(code[0], "rot13")}"', f'{var2}="{code[1]}"', f'{var3}="{code[2][::-1]}"', f'{var4}="{code[3]}"']

        random.shuffle(init)
        init = ";".join(init)
        self.code = f'''
{init};__import__({self.encryptstring("builtins")}).exec(__import__({self.encryptstring("marshal")}).loads(__import__({self.encryptstring("base64")}).b64decode(__import__({self.encryptstring("codecs")}).decode({var1}, __import__({self.encryptstring("base64")}).b64decode("{base64.b64encode(b'rot13').decode()}").decode())+{var2}+{var3}[::-1]+{var4})))
'''.strip().encode()

    def encrypt2(self):
        self.compress()
        var1 = self.generate("e")
        var2 = self.generate("f")
        var3 = self.generate("g")
        var4 = self.generate("h")
        var5 = self.generate("i")
        var6 = self.generate("j")
        var7 = self.generate("k")
        var8 = self.generate("l")
        var9 = self.generate("m")

        conf = {
            "getattr" : var4,
            "eval" : var3,
            "__import__" : var8,
            "bytes" : var9
        }
        encryptstring = self.encryptor(conf)

        self.code = f'''
{var3} = eval({self.encryptstring("eval")});{var4} = {var3}({self.encryptstring("getattr")});{var8} = {var3}({self.encryptstring("__import__")});{var9} = {var3}({self.encryptstring("bytes")});{var5} = lambda {var7}: {var3}({encryptstring("compile")})({var7}, {encryptstring("<string>")}, {encryptstring("exec")});{var1} = {self.code}
{var2} = {encryptstring('__import__("builtins").list', func= True)}({var1})
try:
    {encryptstring('__import__("builtins").exec', func= True)}({var5}({encryptstring('__import__("lzma").decompress', func= True)}({var9}({var2})))) or {encryptstring('__import__("os")._exit', func= True)}(0)
except {encryptstring('__import__("lzma").LZMAError', func= True)}:...
'''.strip().encode()

    def encrypt3(self):
        self.compress()
        data = base64.b64encode(self.code)
        self.code = f'import base64, lzma; exec(compile(lzma.decompress(base64.b64decode({data})), "<string>", "exec"))'.encode()

    def finalize(self):
        build_folder = "build"
        if not os.path.exists(build_folder):
            os.makedirs(build_folder)

        out_file_path = os.path.join(build_folder, os.path.basename(self.outpath))
        with open(out_file_path, "w", encoding="utf-8") as file:
            file.write(self.code.decode())

        print(f"Obfuscated file saved to: {out_file_path}")

def clear_screen():
    if os.name == 'nt':  
        os.system('cls')
    else:  
        os.system('clear')


def main():
    System.Size(150, 47)
    System.Title("Kurta")
    Cursor.HideCursor()
    print()
    
    while True:
        clear_screen() 
        print(Colorate.Diagonal(Colors.DynamicMIX((red, dark)), Center.XCenter(banner)))
        print('\n')

        user_choice = input(stage(f"Choose Option: {dark}-> {Col.reset}", "X", col2=bred)).replace('"', '').replace("'", "")
        print('\n')

        if user_choice == '1':
            print('\n')
            file = input(stage(f"Drag the file you want to obfuscate {dark}-> {Col.reset}", "?", col2=bred)).replace('"', '').replace("'", "")
            print('\n')

            try:
                with open(file, mode='rb') as f:
                    script = f.read().decode('utf-8')
                filename = file.split('\\')[-1]
            except:
                input(f" {Col.Symbol('!', light, dark)} {Col.light_red}Invalid file!{Col.reset}")
                continue

            print('\n')

            now = time()
            Kura = Obfuscator(script, f'obf-{filename}')
            now = round(time() - now, 2)

            print('\n')
            getpass(stage(f"Obfuscation completed successfully in {light}{now}s{bred}.{Col.reset}", "?", col2=bred))
            clear_screen() 

        elif user_choice == '2':
            # Opción 2:
            pass

        elif user_choice == '3':
            print("Exiting the script.")
            break

if __name__ == '__main__':
    main()
