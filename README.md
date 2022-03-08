This repo has now been migrated to the HikLoad project.

Find it there: https://github.com/Tedyst/HikLoad


# A Python library for HikVision ISAPI

This library does not yet include all the ISAPI functions, but you can feel free to add some more!

## Usage

```python
import hikvisionapi

server = hikvisionapi.HikVisionServer("192.168.1.239", "admin", "password")

channelsXML = hikvisionapi.Streaming.getChannels(server)
dicti = hikvisionapi.xml2dict(channelsXML)

print(dicti['StreamingChannelList']['StreamingChannel'])
```

Using `xml2dict` and `dict2xml` you can interface using the ISAPI using a Python-native way. You can look at more examples [here](https://github.com/Tedyst/hikvisionapi/tree/master/examples)

## Licence

HIKVISION is a trademark of Hangzhou Hikvision Digital Technology Co., Ltd. 
