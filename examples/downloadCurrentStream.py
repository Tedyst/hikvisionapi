import hikvisionapi
import hikvisionapi.System
import hikvisionapi.Streaming
import hikvisionapi.RTSPutils

server = hikvisionapi.HikVisionServer("192.168.1.239", "admin", "password")

dicti = hikvisionapi.xml2dict(hikvisionapi.Streaming.getChannels(server))

for channel in dicti['StreamingChannelList']['StreamingChannel']:
    # Primary channel
    if (int(channel['id']) % 10 == 1):
        url = hikvisionapi.Streaming.getChannelRTSP(server, channel['id'])
        print(url)
        hikvisionapi.RTSPutils.downloadRTSP(url, channel['id'] + ".mp4", seconds=5,  debug=True)
