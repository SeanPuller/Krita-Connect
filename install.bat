@echo off
::Set Folders
set SOURCE_FOLDER=krita_connect
set SOURCE_FILE=krita_connect.desktop
set DESTINATION=%APPDATA%\krita\pykrita
set DESTINATIONFOLDER=%APPDATA%\krita\pykrita\krita_connect

::Remove folder and files if they exist already
if exist del /q "%APPDATA%\Krita\Pykrita\krita_connect.desktop"
if exist rd /s /q "%APPDATA%\Krita\Pykrita\krita_connect"

::Create docker_example folder
if not exist "%APPDATA%\Krita\Pykrita\krita_connect" mkdir "%APPDATA%\Krita\Pykrita\krita_connect"

::Add files
xcopy /s /y %SOURCE_FOLDER% %DESTINATIONFOLDER%
copy /y "%SOURCE_FILE%" %DESTINATION%

cmd /c "C:\Program Files\Krita (x64)\bin\krita.exe"