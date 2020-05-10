import re

def getAlbum(filename: str):
    pattern = r'[A-Za-z]{3,}[-_]?\d{3,}'
    return re.findall(pattern, filename)[-1]


samples = [
    "01.ama046_hd",
    "793.(PRESTIGE)(ABP-228)最高のセックス。鈴村あいり",
    "abp-122",
    "abp623_hdMP4",
    "AMA-039.HD",
    "FIV-047.HD",
    "hjd2048.com-0426stars065-h264",
    "one2048.com-0115sqte280-FHD",
    "第一會所新片@SIS001@(200GANA)(200GANA-1856)それでもめげずに懇願し、どうにかこうにかSEX開始したら、潮吹きまくりのイキまくり！ねね_19歳"
    ""]

if __name__ == "__main__":
    for text in samples:
        print(getAlbum(text))
