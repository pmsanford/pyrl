class Keybindings:
    def __init__(self, filename):
        import json
        kb_file = open(filename)
        self.bindings = json.loads(kb_file.read())
        kb_file.close()

    def get_binding(self, keychar):
        uchar = keychar.upper()
        if uchar in self.bindings:
            return self.bindings[uchar]
        else:
            return None
