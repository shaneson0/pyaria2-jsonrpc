
from pyaria2 import Jsonrpc
jsonrpc = Jsonrpc('localhost', 6800)
resp = jsonrpc.addUris('http://182.131.21.97:80/resource/music/music/jianggaranzuhe/320_jianggaranzuhelangsangguniang.mp3', options={"out": "aa.mp3"})
print resp

