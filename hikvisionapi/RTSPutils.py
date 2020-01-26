import ffmpeg
import os


def downloadRTSP(url, videoName, seconds=9999999, debug=False, force=False):
    """
    Downloads an RTSP livestream from url to videoName.

    Parameters:
        url (str): the RTSP link to a stream
        videoName (str): the filename of the downloaded stream
        seconds (int): the maximum number of seconds that should be recorded
    """
    if debug:
        print("Starting download from: " + url)
    stream = ffmpeg.output(ffmpeg.input(url),
                           videoName, vcodec="copy",
                           reorder_queue_size=0, acodec="copy",
                           timeout=1000, stimeout=1000, t=seconds,
                           rtsp_flags="listen", rtsp_transport="tcp")
    if os.path.exists(videoName):
        if force is False:
            raise Exception("File already exists")
        os.remove(videoName)
    if debug is False:
        return ffmpeg.run(stream, capture_stdout=True, capture_stderr=True)
    return ffmpeg.run(stream, capture_stdout=False, capture_stderr=False)
