/*
The MIT License (MIT)
Copyright (c) 2015 Matthew Horrigan
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
 */

import ctypes, urllib.request, praw, time
r = praw.Reddit(user_agent='windows:org.horrgs.redditearthporn:v1.0.0 (by /u/Horrgs)')

blacklist = []
def on_blacklist(link):
    if ".jpg" not in link and ".png" not in link:
        return True
    for item in blacklist:
        if item == link:
            return True
    return False
def get_image():
    submissions = r.get_subreddit('earthporn').get_hot(limit=25)
    for submission in submissions:
        if on_blacklist(submission.url) is False:
            blacklist.append(submission.url)
            file_path = "C:\\images\\" + get_file_name(submission.url)
            urllib.request.urlretrieve(submission.url, file_path)
            return file_path

def get_file_name(file_name):
    spl = file_name.split("/")
    should_be = spl[len(spl) - 1]
    if ".jpg" in should_be or ".png" in should_be:
        return should_be
    else:
        import datetime
        name = datetime.datetime.now().strftime('%H%M%S')
        return name + ".jpg"

while True:
    SPI_SETDESKWALLPAPER = 0x14
    image = get_image()
    print(image)
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image, 0x2)
    time.sleep(60*15)