import moviepy.editor


def main():
    video_name = input("Title of the video to convert: ")
    video_file = moviepy.editor.VideoFileClip(video_name)
    audio_file = video_file.audio
    audio_name = input("Title of the audio to be generated: ")
    audio_file.write_audiofile(audio_name)


if __name__ == "__main__":
    main()
