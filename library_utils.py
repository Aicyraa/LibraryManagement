def search_book(books, title):
    book = ''
    for item in books:
        if title.lower() == item["title"]:
            book = item

    return book or "Title didn't match anything."

def count_available_books(books):
    available = 0
    for book in books:
        if book["isAvailable"]:
            available += 1

    return f"Available books: {available}"

def list_titles(books):
    title = []
    for book in books:
        title.append(book['title'])

    return title
