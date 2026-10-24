import os, json, asyncio, subprocess, textwrap
import requests, edge_tts

SAMPLE = {"voice": "en-US-GuyNeural", "scenes": [
    {"text": "The ocean covers more than seventy percent of our planet.", "query": "ocean waves"},
    {"text": "Yet more than eighty percent of it has never been explored.", "query": "deep sea"},
    {"text": "Its deepest point is nearly eleven kilometers down.", "query": "underwater"}]}

job = json.loads(os.environ.get("JOB_JSON") or "null") or SAMPLE
KEY = os.environ["PIXABAY_API_KEY"]
VOICE = job.get("voice", "en-US-GuyNeural")
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
os.makedirs("out", exist_ok=True)
os.makedirs("tmp", exist_ok=True)

def run(cmd):
    subprocess.run(cmd, check=True)

def duration(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", path], capture_output=True, text=True, check=True)
    return float(r.stdout.strip())

def get_clip(query, i):
    r = requests.get("https://pixabay.com/api/videos/",
                     params={"key": KEY, "q": query, "per_page": 5, "safesearch": "true"}, timeout=30)
    r.raise_for_status()
    hits = r.json().get("hits", [])
    if not hits:
        raise SystemExit("No Pixabay video for: " + query)
    sizes = hits[0]["videos"]
    url = next(sizes[s]["url"] for s in ("medium", "large", "small", "tiny")
               if sizes.get(s, {}).get("url"))
    path = f"tmp/clip{i}.mp4"
    with requests.get(url, stream=True, timeout=120) as d:
        d.raise_for_status()
        with open(path, "wb") as f:
            for chunk in d.iter_content(1048576):
                f.write(chunk)
    return path, hits[0]["pageURL"]

credits = []
with open("tmp/list.txt", "w") as lst:
    for i, scene in enumerate(job["scenes"]):
        text = scene["text"]
        mp3 = f"tmp/voice{i}.mp3"
        asyncio.run(edge_tts.Communicate(text, VOICE).save(mp3))
        dur = duration(mp3) + 0.3
        clip, page = get_clip(scene["query"], i)
        credits.append(page)
        sub = f"tmp/sub{i}.txt"
        with open(sub, "w") as f:
            f.write("\n".join(textwrap.wrap(text, 24)))
        vf = ("scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,"
              f"drawtext=fontfile={FONT}:textfile={sub}:fontsize=64:fontcolor=white:"
              "borderw=5:bordercolor=black:line_spacing=12:x=(w-text_w)/2:y=h*0.68")
        run(["ffmpeg", "-y", "-stream_loop", "-1", "-i", clip, "-i", mp3, "-t", f"{dur:.2f}",
             "-vf", vf, "-af", "apad", "-map", "0:v:0", "-map", "1:a:0",
             "-c:v", "libx264", "-preset", "veryfast", "-pix_fmt", "yuv420p",
             "-c:a", "aac", "-ar", "44100", "-ac", "2", f"tmp/scene{i}.mp4"])
        lst.write(f"file 'scene{i}.mp4'\n")

run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", "tmp/list.txt", "-c", "copy", "out/final.mp4"])
with open("out/credits.txt", "w") as f:
    f.write("Stock footage: Pixabay\n" + "\n".join(credits) + "\n")
print("Done: out/final.mp4", duration("out/final.mp4"), "sec")
