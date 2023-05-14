import pytest
from pywinauto import Application
import time

"""Чистим файл от предыдущего текста"""
def clear_file(app):
    for i in range(1, 100):
        app.UntitledNotepad.type_keys("{BACKSPACE}")
        pass

@pytest.mark.parametrize("text", ["test_text"])
def test_notepad(text):
    app = Application().start("notepad.exe")
    app.UntitledNotepad.Edit.type_keys(text)
    time.sleep(8)
    app.kill()
    app = Application().start("notepad.exe")
    time.sleep(1)
    notepad = app.UntitledNotepad.child_window(class_name="Edit", found_index=0).wait('exists').window_text()
    assert notepad == text, "Текст не сохранен после закрытия блокнота"
    app.kill()
