from django.core.paginator import Paginator
from django.shortcuts import render
from books.models import Book
import datetime

# сырой вариант, но пока только до него додумался. Логика в том, чтобы получать из URL дату,
# Далее группируем книги по датам издания, предварительно их отсортировав.
# Затем выбираем нужную группу и дергаем на страницу её. После смотрим, есть ли соседние по датам группы.
# Если есть, то дергаем их даты для ссылок

def books_view(request):
    pub_date = request.path.split('/')[-2]

# дергаем книги из базы и проверяем какой это url - совокупный или по дате

    books = Book.objects.all()
    if pub_date.find('-') != -1:
        template = 'books/books_list_date.html'
        pub_date = datetime.datetime.strptime(pub_date, '%Y-%m-%d')
        books_groups = []
        books_sorted = sorted(books, key=lambda x: x.pub_date)
        checker = 0
        count = 0
        context = {}
        for idx, book in enumerate(books_sorted):
            if idx == 0:
                checker = book.pub_date
                books_groups.append([(book.pub_date,), book])
                continue
            elif checker == book.pub_date:
                books_groups[count].append(book)
            else:
                books_groups.append([(book.pub_date,)])
                count += 1
                books_groups[count].append(book)
        for idx, books in enumerate(books_groups):
            if books[0][0] == pub_date.date():
                if idx != 0 and (len(books) - idx) != 1:
                    context = {'books': [el for idx, el in enumerate(books) if idx != 0],
                               'prev_date': books_groups[idx-1][0][0].strftime('%Y-%m-%d'),
                               'next_date': books_groups[idx+1][0][0].strftime('%Y-%m-%d'),
                               'has_next': True,
                               'has_prev': True}
                elif idx != 0:
                    context = {'books': [el for idx, el in enumerate(books) if idx != 0],
                               'prev_date': books_groups[idx - 1][0][0].strftime('%Y-%m-%d'),
                               'has_prev': True}
                elif (len(books) - idx) != 1:
                    context = {'books': [el for idx, el in enumerate(books) if idx != 0],
                               'next_date': books_groups[idx + 1][0][0].strftime('%Y-%m-%d'),
                               'has_next': True}
        return render(request, template, context)
    else:
        template = 'books/books_list.html'
        context = {'books': books}
    return render(request, template, context)
