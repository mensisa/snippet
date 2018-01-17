@echo off
ping -n 2 127.0.0.1 > nul

echo this batch will convert ".png" using -strip option from ImageMagick.
echo please make sure you place a batch file in the right location.

ping -n 1 127.0.0.1 > nul

for /f "tokens=* delims= " %%a in ('dir /s/b/a-d "*.png"') do (
magick identify "%%a"
magick convert "%%a" -strip "%%a"
magick identify "%%a")

echo finish..

ping -n 2 127.0.0.1 > nul
set /P user_input=Press any key to terminate...