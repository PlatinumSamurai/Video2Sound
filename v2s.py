import moviepy.editor
import sys


def main():
    video_name = ""
    audio_name = ""

    if len(sys.argv) == 1:
        video_name = input("Path to the video to convert: ")
        video_file = moviepy.editor.VideoFileClip(video_name)
        audio_file = video_file.audio
        audio_name = input("Title of the audio to be generated: ")
        audio_file.write_audiofile(video_name[:video_name.rfind('\\') + 1] + audio_name)
        return 0

    if 1 < len(sys.argv) < 5:
        print("Too few parameters. You should execute program as follows: v2s.exe -s *source_file* -n *target_name*")
        return -1
    elif len(sys.argv) > 5:
        print("Too many parameters. You should execute program as follows: v2s.exe -s *source_file* -n *target_name*")
        return -1

    if sys.argv[1] == "-s":
        video_name = sys.argv[2]
    elif sys.argv[1] == "-n":
        audio_name = sys.argv[2]
    else:
        print(f"Incorrect parameter {sys.argv[1]}. You should execute program as follows: v2s.exe -s *source_file* -n *target_name*")
        return -1

    if sys.argv[3] == "-s":
        video_name = sys.argv[4]
    elif sys.argv[3] == "-n":
        audio_name = sys.argv[4]
    else:
        print(f"Incorrect parameter {sys.argv[3]}. You should execute program as follows: v2s.exe -s *source_file* -n *target_name*")
        return -1

    video_file = moviepy.editor.VideoFileClip(video_name)
    audio_file = video_file.audio
    audio_file.write_audiofile(video_name[:video_name.rfind('\\') + 1] + audio_name)
    return 0


if __name__ == "__main__":
    main()
