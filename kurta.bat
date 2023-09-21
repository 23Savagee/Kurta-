@echo off
chcp 65001 >nul 2>&1
mode con lines=26 cols=120
cd /d "%~dp0"

:menu
chcp 65001 >nul
cls
echo.
echo                                            ██ ▄█▀ █    ██  ██▀███  ▄▄▄█████▓ ▄▄▄      
echo                                            ██▄█▒  ██  ▓██▒▓██ ▒ ██▒▓  ██▒ ▓▒▒████▄    
echo                                            ▓███▄░ ▓██  ▒██░▓██ ░▄█ ▒▒ ▓██░ ▒░▒██  ▀█▄  
echo                                            ▓██ █▄ ▓▓█  ░██░▒██▀▀█▄  ░ ▓██▓ ░ ░██▄▄▄▄██ 
echo                                            ▒██▒ █▄▒▒█████▓ ░██▓ ▒██▒  ▒██▒ ░  ▓█   ▓██▒
echo                                            ▒ ▒▒ ▓▒░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░  ▒ ░░    ▒▒   ▓▒█░
echo                                            ░ ░▒ ▒░░▒░ ░ ░   ░▒ ░ ▒░    ░      ▒   ▒▒ ░
echo                                            ░ ░░ ░  ░░░ ░ ░   ░░   ░   ░        ░   ▒   
echo                                            ░  ░      ░        ░                    ░  ░
echo.
echo.
echo                                                        [1] Start Installer 
echo                                                        [2] About Kurta
echo.
set /p choice=:                                                      Choose : 

if /i "%choice%"=="1" (
  goto Installer
) else if /i "%choice%"=="2" (
  goto AboutKurta
)

:Installer
@echo off
cls
echo.
echo Installing required libraries...
pip install base64 codecs lzma pystyle requests
echo Installation complete.
cls
echo.
echo                                            ██ ▄█▀ █    ██  ██▀███  ▄▄▄█████▓ ▄▄▄      
echo                                            ██▄█▒  ██  ▓██▒▓██ ▒ ██▒▓  ██▒ ▓▒▒████▄    
echo                                            ▓███▄░ ▓██  ▒██░▓██ ░▄█ ▒▒ ▓██░ ▒░▒██  ▀█▄  
echo                                            ▓██ █▄ ▓▓█  ░██░▒██▀▀█▄  ░ ▓██▓ ░ ░██▄▄▄▄██ 
echo                                            ▒██▒ █▄▒▒█████▓ ░██▓ ▒██▒  ▒██▒ ░  ▓█   ▓██▒
echo                                            ▒ ▒▒ ▓▒░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░  ▒ ░░    ▒▒   ▓▒█░
echo                                            ░ ░▒ ▒░░▒░ ░ ░   ░▒ ░ ▒░    ░      ▒   ▒▒ ░
echo                                            ░ ░░ ░  ░░░ ░ ░   ░░   ░   ░        ░   ▒   
echo                                            ░  ░      ░        ░                    ░  ░
echo                                                                  Done
pause
goto menu

:AboutKurta
cls
echo.
echo                                            ██ ▄█▀ █    ██  ██▀███  ▄▄▄█████▓ ▄▄▄      
echo                                            ██▄█▒  ██  ▓██▒▓██ ▒ ██▒▓  ██▒ ▓▒▒████▄    
echo                                            ▓███▄░ ▓██  ▒██░▓██ ░▄█ ▒▒ ▓██░ ▒░▒██  ▀█▄  
echo                                            ▓██ █▄ ▓▓█  ░██░▒██▀▀█▄  ░ ▓██▓ ░ ░██▄▄▄▄██ 
echo                                            ▒██▒ █▄▒▒█████▓ ░██▓ ▒██▒  ▒██▒ ░  ▓█   ▓██▒
echo                                            ▒ ▒▒ ▓▒░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░  ▒ ░░    ▒▒   ▓▒█░
echo                                            ░ ░▒ ▒░░▒░ ░ ░   ░▒ ░ ▒░    ░      ▒   ▒▒ ░
echo                                            ░ ░░ ░  ░░░ ░ ░   ░░   ░   ░        ░   ▒   
echo                                            ░  ░      ░        ░                    ░  ░
echo.
echo.
echo                                                         Kurta On Top
echo                                                Kurta is a script in development
echo                                                Your script version is 1.0.0
echo.
echo.
echo                                                Github: https://github.com/23Savagee
echo.
pause
goto menu
