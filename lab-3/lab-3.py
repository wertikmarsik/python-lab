class BookBuilder:
  def __init__(self, book_type):
    self.book = Book(book_type)

  def add_page(self, page_content):
    self.book.add_page(page_content)

  def build(self):
    return self.book

class Book:
  def __init__(self, book_type):
    self.book_type = book_type
    self.content = []

  def add_page(self, page_content):
    self.content.append(page_content)

class PageSingleton:
  _instance = None
  _page_id = set()

  def __new__(cls):
    if cls._instance is None:
      cls._instance = super(PageSingleton, cls).__new__(cls)
    return cls._instance
  
  @staticmethod
  def add_page(page_id):
    PageSingleton._page_id.add(page_id)

  @staticmethod
  def get_party_id():
    return list(PageSingleton._page_id)
  
pageSingleton = PageSingleton() 

scientific = BookBuilder("Science book")
scientific_book = scientific.build()

article={
  "Думи мої…":"віщати світові",
  "Катерина":"глузливо усміхається",
  "Гайдамаки":"не оправдав надії",
  "Назар Стодоля":"розжати руку"
}

i = 1
for key, desc in article.items():
  page_content = f"Page {i} - {key}: {desc}"
  scientific.add_page(page_content)
  pageSingleton.add_page(id(page_content))
  i+=1

novel_builder = BookBuilder("Novel")

novel = novel_builder.build()

characters = {
  "Herald from Rivia": "Witcher who kills all monsters in Poland",
  "Kartman": "Fatass guy",
  "Invoker": "Piano for yours crooked hands",
  "Pudge": "The same as Cartman, only kinder"
}

i = 1
for key, desc in characters.items():
  page_content = f"Page {i} - {key}: {desc}"
  novel.add_page(page_content)
  pageSingleton.add_page(id(page_content))
  i += 1

manual_builder = BookBuilder("Manual")

manual = manual_builder.build()

images = {
  "1": "https://www.pinterest.com/pin/cartman--33073378503342646/",
  "2": "https://www.pinterest.com/pin/141230138306880771/",
  "3": "https://www.pinterest.com/pin/604537949995175440/",
  "4": "https://www.pinterest.com/pin/south-park-in-2023--314337249005405425/",
  "5": "https://www.pinterest.com/pin/678284393903261096/",
  "6": "https://www.pinterest.com/pin/72690981479185097/"
}

for key, link in images.items():
  page_content = f"Page {key} - {link}"
  manual.add_page(page_content)
  pageSingleton.add_page(id(page_content))

page_ids = pageSingleton.get_party_id()

print("Science Book:")
print(vars(scientific_book))
print("\nNovel:")
print(vars(novel))
print("\nManual:")
print(vars(manual))
print("\nUnique Page IDs:", page_ids)