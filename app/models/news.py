class News:

    '''
    News class that will define the objects of the news
    '''

    def __init__(self, author, title, description, publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.publishedAt = publishedAt


class Sources:

      def __init__(self, id, name, description, category, url):
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.url = url