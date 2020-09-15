class Sources:
    """
    Sources class to define source object
    """
    def __init__(self, id, name, description, url):
        self.id = id
        self.name = name
        self.description = description
        self.url = url



class Articles:
    """
    Articles class to define articles object
    """
    def __init__(self, author, title, description, url, urlToImage):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
