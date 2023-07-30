import moviepy.editor
import sys
import argparse
import platform
import time


def generate_parser():
    parsrer = argparse.ArgumentParser()
    parsrer.add_argument("-s", type=str, help="Source name of the file")
    parsrer.add_argument("-n", type=str, help="Target name of the file")

    return parsrer


def convert_video_to_sound(video_name, audio_name, delim):
    video_file = moviepy.editor.VideoFileClip(video_name)
    audio_file = video_file.audio
    audio_file.write_audiofile(video_name[:video_name.rfind(delim) + 1] + audio_name)


def main():
    parser = generate_parser()
    args = parser.parse_args(sys.argv[1:])
    delimiter = ""

    if platform.system() == "Linux":
        delimiter = "/"
    elif platform.system() == "Windows":
        delimiter = "\\"

    print("Video2Sound 1.0 Framework")
    time.sleep(1)
    
    if args.s is None:
        args.s = input("Path to the video to convert: ")
    if args.n is None:
        args.n = input("Title of the audio to be generated: ")

    convert_video_to_sound(args.s, args.n, delimiter)

    return 0


if __name__ == "__main__":
    main()
