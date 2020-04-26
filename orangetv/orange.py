from urllib.request import urlopen
import json

def urlretrieve(url):
    return json.load(urlopen(url))

class OrangeTV():
    """
    Class to manipulate a Orange TV Decoder
    """
    number_keys = {str(i) : 512+i for i in range(10)} #512 is 0, then numbers are on sequence. 

    def __init__(self, ip, port=8080):
        self.ip = ip
        self.port = port
        self.url = f"http://{self.ip}:{self.port}/remoteControl/cmd"

    def get_info(self):
        return urlretrieve(f"{self.url}?operation=10")

    def switch_over_epg(self, epg):
        """ 
        Switch to a channel using its epg id.

        You can retrieve the epg id of a channel calling get_info when on it.
        tv.get_info()["result"]["data"]["playedMediaId"] will give the epg id.
        Some channels do not have an epg id.
        """
        epg = f"{epg}".rjust(10, "*")
        return urlretrieve(f"{self.url}?operation=09&epg_id={epg}&uui=1")

    def press_key(self, key):
        """
        Press the key as directly interpreted by the decoder.
        key is an int that correspond to a key. (i.e. 512 is equivalent to type 0 on your tv remote.)
        Other remote keys are also possible.
        """
        return urlretrieve(f"{self.url}?operation=01&key={key}&mode=0")

    def switch_on(self):
        state = self.get_info()["result"]["data"]["activeStandbyState"]
        if state == "1":
            self.press_key(116)

    def switch_off(self):
        state = self.get_info()["result"]["data"]["activeStandbyState"]
        if state == "0":
            self.press_key(116)

    def type_channel_id(self, channel):
        """
        Type the sequence of numbers indicated by channel.
        """
        ch = str(channel)
        for c in ch:
            self.press_key(OrangeTV.number_keys[c])
        return