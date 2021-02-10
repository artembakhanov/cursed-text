from googletrans import Translator
from random import choice

translator = Translator()
cursed_langs = ['af', 'sq', 'am', 'hy', 'az', 'eu', 'bn', 'bs', 'bg', 'ca', 'ceb', 'ny', 'zh-cn', 'zh-tw', 'co', 'tl',
                'fy',
                'gl', 'ka', 'gu', 'ht', 'ha', 'hi', 'hmn', 'is', 'ig', 'id', 'kn', 'kk', 'km', 'ku', 'ky', 'lo', 'la',
                'lb',
                'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'or', 'ps', 'pa', 'sm', 'st', 'sn', 'sd',
                'si',
                'so', 'su', 'tg', 'ta', 'te', 'ur', 'ug', 'uz', 'cy', 'xh', 'yi', 'yo', 'zu']


def make_text_cursed(text, trans_num=8):
    src = translator.detect(text).lang
    seq = [src]
    for i in range(trans_num):
        dest = choice(cursed_langs)
        seq.append(dest)
        text = translator.translate(text, dest=dest).text
        print(text)

    seq.append(src)
    return translator.translate(text, dest=src).text, seq


if __name__ == '__main__':
    print(make_text_cursed("Тестовое сообщение", 10)[0], sep='\n')
