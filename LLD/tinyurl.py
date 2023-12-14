# Problem Link : https://leetcode.com/problems/encode-and-decode-tinyurl/description/

class Codec:
    def __init__(self):
        self.encode_dict = {}
        self.decode_dict = {}
        self.base_url = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        if longUrl not in self.encode_dict:
            shortUrl = self.base_url+str(len(self.encode_dict)+1)
            self.encode_dict[longUrl]=shortUrl
            self.decode_dict[shortUrl]=longUrl
        return self.encode_dict[longUrl]

     
    def decode(self, shortUrl: str) -> str:
        return self.decode_dict[shortUrl]
 