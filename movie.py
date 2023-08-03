import moviepy.editor
import os.path

# Программа для конвертации видео-файлов в аудио-файлы
print('Эта программа поможет вам преобразовать преобразовать видео-файл в аудио-файл.')
movie = input('Введите путь в файлу:')
file = os.path.exists(movie)
if file == True:
    video = moviepy.editor.VideoFileClip(movie)
    audio =video.audio
    audio.write_audiofile('audio.mp3')
    print("Файл успешно был конвертирован.")
else:
    print('К сожалению пусть к файлу не найден...')
    input()
