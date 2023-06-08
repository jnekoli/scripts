# Converts mp3s, flacs, and other audio files into opus at 192K bitrate with an mkv container.
# Preserves the directory structure and exlcudes common non-audio files.
# Useful for decreasing size and maintaining high quality audio files for portability, e.g. for thumb drives or phones.
import os

in_dir = "F:\\in"
out_dir = "F:\\o"


def make_outpath(k: str) -> str:
    """helper function"""
    id = os.path.abspath(in_dir)
    od = os.path.abspath(out_dir)
    o = k.replace(id, od)
    return o


def do_something(p: str):
    """thread/process handler"""
    badexts = [".jpg", ".jpeg", ".gif", ".png", ".log", ".bmp", ".txt", ".cue",
               ".rar", ".zip", ".7z", ".m3u", ".sfv", ".cue", ".nfo", ".pdf"]
    if any(p.lower().endswith(e) for e in badexts):
        return
    p_out = make_outpath(p)
    future_dir = os.path.dirname(p_out)
    os.makedirs(future_dir, exist_ok=True)
    p_out += ".mkv"
    if os.path.exists(p_out):
        return
    p_quotes = "\"" + p + "\""
    p_out_quotes = "\"" + p_out + "\""
    mycmd = "ffmpeg -n -i " + p_quotes + \
        " -map 0 -c:v copy -c:a libopus -b:a 192K -hide_banner " + p_out_quotes
    p1 = subprocess.run(mycmd, text=True, shell=True, capture_output=True,
                        universal_newlines=True, encoding="utf-8")
    print(p_out)


for root, dirs, files in os.walk(in_dir, topdown=False):
    for f in files:
        p = os.path.join(root, f)
        do_something(p)
