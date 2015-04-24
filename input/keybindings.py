class Keybindings:
    def __init__(self, filename):
        """
        :param str filename: Name of the keybinding file.
        """
        import json
        kb_file = open(filename)
        self.bindings = json.loads(kb_file.read())
        kb_file.close()

    def get_binding(self, keychar):
        """
        :param str keychar: The key pressed
        """
        uchar = keychar.upper()
        if uchar in self.bindings:
            return self.bindings[uchar]
        else:
            return None
