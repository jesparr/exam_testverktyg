#
# class CatalogPage:
#     def __init__(self, page):
#         self.page = page
#
#         self.catalog_container = page.locator('.catalog-container')
#
#         self.book_items = page.locator('.book')
#
#     def is_visible(self):
#         return self.catalog_container.is_visible()
#
#     def get_book_count(self):
#         return self.book_items.count()