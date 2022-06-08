def strip_html(text):
    """ strips all html entities """

    from   html.parser import HTMLParser
    from   io          import StringIO

    class HTMLStripper(HTMLParser):
        """ Helper class to strip HTML """
        def __init__(self):
            super().__init__()
            self.reset()
            self.strict = False
            self.convert_charrefs= True
            self.text = StringIO()

        def handle_data(self, d):
            self.text.write(d)

        def get_data(self):
            return self.text.getvalue()


    s = HTMLStripper()
    s.feed(text)
    return s.get_data()

def strip_punctuation(text):
    import string
    return text.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation)))

def lower(text):
    return text.lower()

def min_length(num):
    def min_len(text):
        return ' '.join(t for t in text.split() if len(t) >= num)
    return min_len if num else lambda text : text
