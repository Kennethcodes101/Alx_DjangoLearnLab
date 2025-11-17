### Registering and Customizing the Book Model in Admin

**File:** `bookshelf/admin.py`

```python
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)
```

**Explanation:**

- `@admin.register(Book)` registers the Book model in Django admin.
- `list_display` shows selected fields in a table list view.
- `search_fields` allows searching by title and author.
- `list_filter` adds filtering by publication year.
