# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

#Data Bit等の設定
DB4 = 7
DB5 = 22
DB6 = 23
DB7 = 24
RS = 17
EN = 25




STR_TABLE = {
            " ":32,
            "!":33,
            '"':34,
            "#":35,
            "$":36,
            "%":37,
            "&":38,
            "'":39,
            "(":40,
            ")":41,
            "*":42,
            "+":43,
            ",":44,
            "-":45,
            ".":46,
            "/":47,
            "0":48,
            "1":49,
            "2":50,
            "3":51,
            "4":52,
            "5":53,
            "6":54,
            "7":55,
            "8":56,
            "9":57,
            ":":58,
            ";":59,
            "<":60,
            "=":61,
            ">":62,
            "?":63,
            "@":64,
            "A":65,
            "B":66,
            "C":67,
            "D":68,
            "E":69,
            "F":70,
            "G":71,
            "H":72,
            "I":73,
            "J":74,
            "K":75,
            "L":76,
            "M":77,
            "N":78,
            "O":79,
            "P":80,
            "Q":81,
            "R":82,
            "S":83,
            "T":84,
            "U":85,
            "V":86,
            "W":87,
            "X":88,
            "Y":89,
            "Z":90,
            "[":91,
            "]":93,
            "^":94,
            "_":95,
            "`":96,
            "a":97,
            "b":98,
            "c":99,
            "d":100,
            "e":101,
            "f":102,
            "g":103,
            "h":104,
            "i":105,
            "j":106,
            "k":107,
            "l":108,
            "m":109,
            "n":110,
            "o":111,
            "p":112,
            "q":113,
            "r":114,
            "s":115,
            "t":116,
            "u":117,
            "v":118,
            "w":119,
            "x":120,
            "y":121,
            "z":122,
            "{":123,
            "|":124,
            "}":125,
            u"→":126,
            u"←":127,
            u"ｦ":166,
            u"ｧ":167,
            u"ｨ":168,
            u"ｩ":169,
            u"ｪ":170,
            u"ｫ":171,
            u"ｬ":172,
            u"ｭ":173,
            u"ｮ":174,
            u"ｯ":175,
            u"ｰ":176,
            u"ｱ":177,
            u"ｲ":178,
            u"ｳ":179,
            u"ｴ":180,
            u"ｵ":181,
            u"ｶ":182,
            u"ｷ":183,
            u"ｸ":184,
            u"ｹ":185,
            u"ｺ":186,
            u"ｻ":187,
            u"ｼ":188,
            u"ｽ":189,
            u"ｾ":190,
            u"ｿ":191,
            u"ﾀ":192,
            u"ﾁ":193,
            u"ﾂ":194,
            u"ﾃ":195,
            u"ﾄ":196,
            u"ﾅ":197,
            u"ﾆ":198,
            u"ﾇ":199,
            u"ﾈ":200,
            u"ﾉ":201,
            u"ﾊ":202,
            u"ﾋ":203,
            u"ﾌ":204,
            u"ﾍ":205,
            u"ﾎ":206,
            u"ﾏ":207,
            u"ﾐ":208,
            u"ﾑ":209,
            u"ﾒ":210,
            u"ﾓ":211,
            u"ﾔ":212,
            u"ﾕ":213,
            u"ﾖ":214,
            u"ﾗ":215,
            u"ﾘ":216,
            u"ﾙ":217,
            u"ﾚ":218,
            u"ﾛ":219,
            u"ﾜ":220,
            u"ﾝ":221,
            }

#行番号保持変数
now_row = 0



def send_by_4bit(data,rs = False):
    GPIO.output(RS,rs)
    GPIO.output(EN,True)
    GPIO.output(DB7,data >= 8)
    data %= 8
    GPIO.output(DB6,data >= 4)
    data %= 4
    GPIO.output(DB5,data >= 2)
    data %= 2
    GPIO.output(DB4,data >= 1)
    GPIO.output(EN,False)
    time.sleep(0.001)

def send(data,rs = False):
    send_by_4bit(data >> 4,rs)
    send_by_4bit(data & 0x0f,rs)


def oled_init():
    time.sleep(0.5)
    send(8)
    send(0x13)
    for i in (0,1,2,3,4):
        send_by_4bit(0)
    send_by_4bit(2)
    send(0x28)
    send(0x0b)
    send(0x06)
    send(0x01)
    time.sleep(0.006)
    send(0x02)
    send(0x17)
    send(0x0f)

def gpio_init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DB4, GPIO.OUT)
    GPIO.setup(DB5, GPIO.OUT)
    GPIO.setup(DB6, GPIO.OUT)
    GPIO.setup(DB7, GPIO.OUT)
    GPIO.setup(RS, GPIO.OUT)
    GPIO.setup(EN, GPIO.OUT)


def oled_locate(row=0,col=0):
    """
    128~
    192~
    """
    if row == 0:
        send(128 + col)
    elif row == 1:
        send(192 + col)



def send_str(_str):
    for s in _str:
        d = STR_TABLE.get(s,0)
        if d:
            send(d,True)


if __name__ == "__main__":
    GPIO.setwainings(False)
    gpio_init()
    oled_init()
    
    send_str("WinStar OLED")
    oled_locate(1, 0)
    send_str("Display!")

    GPIO.cleanup()

