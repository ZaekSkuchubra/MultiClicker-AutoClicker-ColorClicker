@echo on
setlocal
set "script_dir=%~dp0"
set "subfolder=PythonBase"
set "file_name=Interface.pyw"
set "file_path=%script_dir%%subfolder%\%file_name%"
if exist "%file_path%" (
    start "" "%file_path%"
    exit
) else (
    echo File "%file_name%" not found in "%script_dir%%subfolder%".
)
pause
