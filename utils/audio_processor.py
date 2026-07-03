import yt_dlp
from pydub import AudioSegment
import os
from typing import Optional

DOWNLOAD_DIR = "downloades"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def _base_ydl_opts(output_path: str) -> dict:
    return {
        "outtmpl": output_path,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
                "preferredquality": 192,
            }
        ],
        "quiet": True,
        "retries": 5,
        "fragment_retries": 5,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "http_headers": {
            "User-Agent": (
                "Mozilla/5.0 (Linux; Android 13; Pixel 7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Mobile Safari/537.36"
            )
        },
    }


def download_youtube_audio(url: str, cookies_from_browser: Optional[str] = None) -> str:
    """
    Download audio from a YouTube URL.

    YouTube periodically breaks specific yt-dlp "player clients" (web/android/ios),
    causing 403 errors that come and go without any code change on our side.
    Instead of relying on one fixed client, we try several strategies in order
    and fall back automatically if one gets blocked.

    IMPORTANT: This only works reliably if yt-dlp is up to date. Run:
        pip install -U yt-dlp
    before relying on this function — an outdated yt-dlp is the #1 cause of
    403s that no amount of client-spoofing here can fix.
    """
    output_path = os.path.join(DOWNLOAD_DIR, "%(title)s.%(ext)s")

    strategies = [
        {"format": "bestaudio/best", "extractor_args": {"youtube": {"player_client": ["android"]}}},
        {"format": "bestaudio/best", "extractor_args": {"youtube": {"player_client": ["ios"]}}},
        {"format": "best", "extractor_args": {"youtube": {"player_client": ["web"]}}},
        {"format": "18", "extractor_args": {"youtube": {"player_client": ["web"]}}},
    ]

    last_error = None
    for strategy in strategies:
        ydl_opts = _base_ydl_opts(output_path)
        ydl_opts.update(strategy)
        if cookies_from_browser:
            ydl_opts["cookiesfrombrowser"] = (cookies_from_browser,)

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info).replace(".webm", ".wav").replace(".m4a", ".wav").replace(".mp4", ".wav")
            return filename
        except yt_dlp.utils.DownloadError as e:
            print(f"Strategy {strategy['extractor_args']['youtube']['player_client']} failed: {e}")
            last_error = e
            continue

    raise RuntimeError(
        "All download strategies failed (likely YouTube blocking / outdated yt-dlp). "
        f"Last error: {last_error}. Try: pip install -U yt-dlp, or pass "
        "cookies_from_browser='chrome' if the video needs a logged-in session."
    )


def convert_to_wav(input_path : str) -> str:
    """Convert any audio/video file to WAV format using pydub."""
    output_path = os.path.splitext(input_path)[0] + "_converted.wav"
    audio = AudioSegment.from_file(input_path)
    audio = audio.set_channels(1).set_frame_rate(16000)
    audio.export(output_path, format="wav")
    return output_path

def chunk_audio(wav_path: str, chunk_minutes: int=10)-> list:
    audio = AudioSegment.from_wav(wav_path)
    chunk_ms = chunk_minutes * 60 * 1000

    chunks = []

    for i, start in enumerate(range(0, len(audio), chunk_ms)):
        chunk = audio[start : start + chunk_ms]
        chunk_path = f"{wav_path}_chunk_{i}.wav"
        chunk.export(chunk_path, format="wav")
        chunks.append(chunk_path)

    return chunks

def process_input(source: str) -> list:
    if source.startswith("http://") or source.startswith("https://"):
        print("detected youtube url. Downloading audio...")
        wav_path = download_youtube_audio(source)
    else:
        print("Detected local file. Converting to WAV...")
        wav_path = convert_to_wav(source)

    print("Chunking audio...")
    chunks = chunk_audio(wav_path)
    print(f"Audio ready - {len(chunks)} chunk(s) created.")
    return chunks
