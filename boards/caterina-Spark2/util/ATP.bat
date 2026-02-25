@echo off
:start
set /P SDATA="Serial Data: "
atprogram -d atmega32u4 -t avrdragon -i isp chiperase
atprogram -d atmega32u4 -t avrdragon -i isp write -fl -o 0x7FD0 --values %SDATA%
atprogram -d atmega32u4 -t avrdragon -i isp write -fs --values FFD8CB
atprogram -d atmega32u4 -t avrdragon -i isp program -f ../Caterina.hex
echo ----
goto start