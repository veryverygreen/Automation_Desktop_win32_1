import pytest
from pywinauto import Application
import time

"""Чистим файл от предыдущего текста"""
def clear_file(app):
    for i in range(1, 100):
        app.Notepad.type_keys("{BACKSPACE}")
        pass

@pytest.mark.parametrize("text", ["test_text"])
def test_notepad_plusplus(text):
    app = Application().start("C:\\Program Files\\Notepad++\\notepad++.exe")
    clear_file(app)
    app.Notepad.type_keys(text)
    time.sleep(8) #ожидание в 8 секунд, т.к. по умолчанию автосохранения в Notepad++ каждые 7 секунд
    app.kill()
    app = Application().start("C:\\Program Files\\Notepad++\\notepad++.exe")
    time.sleep(1)
    notepadpp = app.Notepad.child_window(class_name="Scintilla", found_index=0).wait('exists').window_text()
    assert notepadpp == text, "Текст сохранен после закрытия блокнота"
    app.kill()