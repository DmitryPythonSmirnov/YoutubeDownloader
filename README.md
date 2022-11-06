### YoutubeDownloader
Программа для скачивания видео из Youtube - написана на Python. Необходим Python версии 3.6 и выше.  
Программа использует библиотеку pytube: https://pytube.io/en/latest/  
Данную библиотеку необходимо установить:

`pip install pytube`

(другие варианты установки приведены здесь: https://pytube.io/en/latest/user/install.html)

В процессе работы скрипт предоставляет список доступных потоков для скачивания. Рекомендуется выбирать вариант с progressive="True" - это аудио+видео в одном файле. Варианты с progressive="False" - только аудио или только видео. В выводе доступных потоков видны разрешения, например, res="720p".

Пример:
```
Введите URL для скачивания видео с Youtube. Для выхода введите q: https://www.youtube.com/watch?v=J0Aq44Pze-w&t=1s

1: <Stream: itag="17" mime_type="video/3gpp" res="144p" fps="12fps" vcodec="mp4v.20.3" acodec="mp4a.40.2" progressive="True" type="video">
2: <Stream: itag="18" mime_type="video/mp4" res="360p" fps="24fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">
3: <Stream: itag="22" mime_type="video/mp4" res="720p" fps="24fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video">
4: <Stream: itag="137" mime_type="video/mp4" res="1080p" fps="24fps" vcodec="avc1.640028" progressive="False" type="video">
5: <Stream: itag="248" mime_type="video/webm" res="1080p" fps="24fps" vcodec="vp9" progressive="False" type="video">
6: <Stream: itag="399" mime_type="video/mp4" res="1080p" fps="24fps" vcodec="av01.0.08M.08" progressive="False" type="video">
7: <Stream: itag="136" mime_type="video/mp4" res="720p" fps="24fps" vcodec="avc1.4d401f" progressive="False" type="video">
8: <Stream: itag="247" mime_type="video/webm" res="720p" fps="24fps" vcodec="vp9" progressive="False" type="video">
9: <Stream: itag="398" mime_type="video/mp4" res="720p" fps="24fps" vcodec="av01.0.05M.08" progressive="False" type="video">
10: <Stream: itag="135" mime_type="video/mp4" res="480p" fps="24fps" vcodec="avc1.4d401e" progressive="False" type="video">
11: <Stream: itag="244" mime_type="video/webm" res="480p" fps="24fps" vcodec="vp9" progressive="False" type="video">
12: <Stream: itag="397" mime_type="video/mp4" res="480p" fps="24fps" vcodec="av01.0.04M.08" progressive="False" type="video">
13: <Stream: itag="134" mime_type="video/mp4" res="360p" fps="24fps" vcodec="avc1.4d401e" progressive="False" type="video">
14: <Stream: itag="243" mime_type="video/webm" res="360p" fps="24fps" vcodec="vp9" progressive="False" type="video">
15: <Stream: itag="396" mime_type="video/mp4" res="360p" fps="24fps" vcodec="av01.0.01M.08" progressive="False" type="video">
16: <Stream: itag="133" mime_type="video/mp4" res="240p" fps="24fps" vcodec="avc1.4d4015" progressive="False" type="video">
17: <Stream: itag="242" mime_type="video/webm" res="240p" fps="24fps" vcodec="vp9" progressive="False" type="video">
18: <Stream: itag="395" mime_type="video/mp4" res="240p" fps="24fps" vcodec="av01.0.00M.08" progressive="False" type="video">
19: <Stream: itag="160" mime_type="video/mp4" res="144p" fps="24fps" vcodec="avc1.4d400c" progressive="False" type="video">
20: <Stream: itag="278" mime_type="video/webm" res="144p" fps="24fps" vcodec="vp9" progressive="False" type="video">
21: <Stream: itag="394" mime_type="video/mp4" res="144p" fps="24fps" vcodec="av01.0.00M.08" progressive="False" type="video">
22: <Stream: itag="139" mime_type="audio/mp4" abr="48kbps" acodec="mp4a.40.5" progressive="False" type="audio">
23: <Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">
24: <Stream: itag="249" mime_type="audio/webm" abr="50kbps" acodec="opus" progressive="False" type="audio">
25: <Stream: itag="250" mime_type="audio/webm" abr="70kbps" acodec="opus" progressive="False" type="audio">
26: <Stream: itag="251" mime_type="audio/webm" abr="160kbps" acodec="opus" progressive="False" type="audio">

Введите порядковый номер потока для скачивания. Для выхода введите q: 3
Вы выбрали следующий поток для скачивания:
3: <Stream: itag="22" mime_type="video/mp4" res="720p" fps="24fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video">
Верно? (y/n) [y]:
Download is in progress...
Percent: 23%
Percent: 47%
Percent: 70%
Percent: 94%
Percent: 100%
Download completed!
Для выхода нажмите Enter...

```
