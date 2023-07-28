import moviepy.editor
import sys
import argparse
import platform


def generate_parser():
    parsrer = argparse.ArgumentParser()
    parsrer.add_argument("-s", type=str, help="Source name of the file")
    parsrer.add_argument("-n", type=str, help="Target name of the file")

    return parsrer


def main():
    parser = generate_parser()
    args = parser.parse_args(sys.argv[1:])
    delimiter = ""

    if platform.system() == "Linux":
        delimiter = "/"
    elif platform.system() == "Windows":
        delimiter = "\\"

    print("Video2Sound 1.0 Framework")
    
    if args.s is None:
        args.s = input("Path to the video to convert: ")
    if args.n is None:
        args.n = input("Title of the audio to be generated: ")

    video_file = moviepy.editor.VideoFileClip(args.s)
    audio_file = video_file.audio
    audio_file.write_audiofile(args.s[:args.s.rfind(delimiter) + 1] + args.n)

    return 0


if __name__ == "__main__":
    main()
