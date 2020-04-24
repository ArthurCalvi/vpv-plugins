import typing

WinId = typing.NewType('WinId', str)

con = None

def is_mouse_clicked(button: int):
    return con.call('ismouseclicked', button)

def get_mouse_position():
    return con.call('get_mouse_position')

def get_windows():
    return [Window(WinId(w)) for w in con.call('get_windows')]

def _window_is_focused(win: WinId):
    return con.call('window_is_focused', win)

def _window_get_current_filename(win: WinId):
    return con.call('window_get_current_filename', win)

def get_focused_window():
    for w in get_windows():
        if w.focused:
            return w


class Window:

    def __init__(self, id: WinId):
        self.id = id

    @property
    def focused(self):
        return _window_is_focused(self.id)

    @property
    def current_filename(self):
        return _window_get_current_filename(self.id)

