@echo off
FOR /F "tokens=*" %%i IN (serials.txt) DO (
echo %%i
pause
atprogram -d atmega32u4 -t avrdragon -i isp chiperase
atprogram -d atmega32u4 -t avrdragon -i isp write -fl -o 0x7FD0 --values %%i
atprogram -d atmega32u4 -t avrdragon -i isp write -fs --values FFD8CB
atprogram -d atmega32u4 -t avrdragon -i isp program -f ../Caterina.hex
echo.
echo.
)
pause