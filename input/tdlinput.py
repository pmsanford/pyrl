class TdlInput:
    def __init__(self):
        import tdl
        self.tdl = tdl
        self.key_handlers = []
        self.quit_handlers = []
        self.mouse_handlers = []

    def add_event_handler(self, callback, type_filter = None):
        if type_filter is None or 'key' in type_filter:
            self.key_handlers.append(callback)

        if type_filter is None or 'quit' in type_filter:
            self.quit_handlers.append(callback)

        if type_filter is None or 'mouse' in type_filter:
            self.mouse_handlers.append(callback)

    def poll_events(self):
        for event in self.tdl.event.get():
            if event.type == 'KEYDOWN':
                for handler in self.key_handlers:
                    handler(event)
            if event.type == 'QUIT':
                for handler in self.quit_handlers:
                    handler(event)
