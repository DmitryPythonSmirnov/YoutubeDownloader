'''
URL для тестов: https://www.youtube.com/watch?v=J0Aq44Pze-w
'''

import pytube
from pytube.exceptions import RegexMatchError
from typing import Union, List


###############################################################################
#                            Function "get_url"                               #
###############################################################################
def get_url() -> Union[str, None]:
    '''
    Функция запрашивает URL, проверяет его валидность,
    возвращает URL в виде строки, если он валидный,
    или None, если URL невалидный
    '''
    while True:
        url = input('Введите URL для скачивания видео с Youtube. '
                    'Для выхода введите q: ')
        if url == 'q':
            print('Выход')
            return None

        # Проверка URL на валидность
        try:
            pytube.YouTube(url)
        except RegexMatchError:
            print('Вы ввели невалидный URL')
            continue
        else:
            return url


###############################################################################
#                          Function "get_streams"                             #
###############################################################################
# TODO - разобраться с типом возвращаемых данных в списке
def get_streams(url: str):
    '''
    Функция получает URL в виде строки, обращается к Youtube через pytube,
    выводит в терминал пронумерованный список потоков (streams),
    возвращает список этих потоков (в виде объектов)
    '''
    yt = pytube.YouTube(
        url,
        on_progress_callback=progress_function,
        on_complete_callback=complete_function
    )

    all_streams = yt.streams
    print()  # Для отделения пустой строкой
    for i, stream in enumerate(all_streams, start=1):
        print(f'{i}: {stream}')
        
    print()  # Для отделения пустой строкой

    return all_streams


###############################################################################
#                          Function "get_itag"                                #
###############################################################################
# TODO - добавить тип all_streams
def get_itag(all_streams) -> Union[int, None]:
    '''
    Функция запрашивает порядковый номер потока для скачивания,
    получает itag этого потока и возвращает itag в виде числа
    '''
    while True:
        stream_num = input('Введите порядковый номер потока для скачивания. Для выхода введите q: ')
        if stream_num == 'q':
            print('Выход')
            return None
        
        if not stream_num.isdigit():
            print('Вы ввели не число')
            continue

        if int(stream_num) > len(all_streams):
            print('Такого номера потока нет в списке')
            continue

        itag = all_streams[int(stream_num) - 1].itag
        answer = input('Вы выбрали следующий поток для скачивания:\n'
                    f'{stream_num}: {all_streams[int(stream_num) - 1]}\n'
                    'Верно? (y/n) [y]: ')
        if not (answer.lower() == 'y' or answer == ''):
            print('Вы отменили выбор')
            continue

        return itag


###############################################################################
#                          Function "download"                                #
###############################################################################
# TODO - добавить тип all_streams
def download(all_streams, itag:int) -> None:
    '''
    Функция принимает список потоков и itag выбранного потока для скачивания.
    По эти данным происходит скачивание файла - в текущий каталог.
    '''
    print('Download is in progress...')
    all_streams.get_by_itag(itag).download()


###############################################################################
#                 progress_function and complete_function                     #
###############################################################################
# TODO - переделать функции в этом разделе

def progress_function(stream, chunk, bytes_remaining):
    percent = int((stream.filesize - bytes_remaining) * 100 / stream.filesize)
    print(f'Percent: {percent}%')


def complete_function(stream, file_path):
    print('Download completed!')


###############################################################################
#                              Function "main"                                #
###############################################################################
def main():
    url = get_url()
    if url is None:
        return None
    
    all_streams = get_streams(url)
    itag = get_itag(all_streams)
    if itag is None:
        return None

    download(all_streams, itag)



###############################################################################
#                              Executive part                                 #
###############################################################################
if __name__ == '__main__':
    main()
    input('Для выхода нажмите любую клавишу...')

