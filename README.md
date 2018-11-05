# MT5_to_Python

the repository show 2 ways to transfer data from mt5 to python.
description will be in Russian, if necessary, use Google translate


## MT5
в папке /mt5/MQL5/ все необходимое для работы, со всеми исходниками!

терминал от Alpari MT5 Version 5.00 build 1940

<p align="center">
  <img src="https://github.com/Lxbinary/MT5_to_Python/raw/master/img/mt5.png" width="400"/>
</p>

* Советник отправляет данные при изменении Close по выбранным инструментам
* Если список инструментов оставить пустым - будет слать по всем парам из обзора рынка


## Python
сделал 2 примера: 
1) непосредственного получения и обработки данных 
2) и тест скорости отправки. у меня по сокетам и по редис время, от отправки из терминала, до получения в питоне быстрее 0,001 sec (те Очень быстро и разницы на таком уровне нету)

Сам я остановился на варианте с Redis тк:
+ достаточно одного терминала на множество скриптов. (работа идет как с единым БД).
+ по скорости, для моих нужд, более чем быстро и не уступает socket

## Install
### Redis
Если под винды: https://github.com/MicrosoftArchive/redis/releases

## Conacts
Telegram: @Lxbinary
