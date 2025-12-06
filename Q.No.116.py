books = []
def router(method, path, data=None):
    if method == "GET" and path == "/items":
        return books
    if method == "POST" and path == "/items":
        books.append(data)
        return {"added": True}
    if method == "GET" and path == "/stats":
        return {"total": len(books)}
    return {"error": "invalid request"}
print(router("POST", "/items", {"id": 1, "title": "Book A"}))
print(router("POST", "/items", {"id": 2, "title": "Book B"}))
print(router("GET", "/items"))
print(router("GET", "/stats"))


