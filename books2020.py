# class Library:
#     def __init__(self, total, signup_time, books_day, present_books):
#         self.total = total
#         self.signup_time = signup_time
#         self.books_day = books_day
#         self.present_books = present_books

    # def __str__(self):
    #     return ('Total Books: ' +  str(self.total) + ' Sign Up time: ' +  str(self.signup_time) + ' Books per day: ' + self.books_day)
    #     ('present_books:', self.present_books)

filename = input('Enter filename: ')
with open(filename) as fh:
    book_no, lib_no, total_days = list(map(int, fh.readline().split()))
    scores = list(map(int, fh.readline().split()))
    print(book_no, lib_no, total_days)
    print(scores)

    # lists
    libraries_list = []
    no_of_books_list = []
    no_of_days_list = []
    present_books_list = []
    books_per_day_list = []

    for i in range(lib_no):
        no_of_books, no_of_days, books_per_day = list(map(int, fh.readline().split()))
        present_books = list(map(int, fh.readline().split()))
        # libraries_list.append()
        no_of_books_list.append(no_of_books)
        no_of_days_list.append(no_of_days)
        books_per_day_list.append(books_per_day)
        present_books_list.append(present_books)
        # l = Library(no_of_books, no_of_days, books_per_day, present_books)
        # libraries.append(l)
def print_all():
    for i in range(lib_no):
        print('Total Books:', no_of_books_list[i])
        print('Sign Up time:', no_of_days_list[i])
        print('Books per day:', books_per_day_list[i])
        print('Present_books:', present_books_list[i])
        print()

# print_all()
# a_example.txt

'''
6 2 7
[1, 2, 3, 6, 5, 4]
[0, 1, 2, 3, 4, 5]
Total Books: 5
Sign Up time: 2
Books per day: 2
Present_books: [0, 1, 2, 3, 4]

Total Books: 4
Sign Up time: 3
Books per day: 1
Present_books: [0, 2, 3, 5]
'''



score = 0
finished_books = []
signed_up = 0
libraries = [[] for i in range(lib_no)]

books_per_day_dict = {v:k for k,v in enumerate(books_per_day_list)}
while total_days > 0 and book_no > 0:

    books_per_day = min(books_per_day_dict)
    lib_index = lowest_book_per_day_index = books_per_day_dict[books_per_day]

    del(books_per_day_dict[books_per_day])


    total_days -= no_of_days_list[lib_index]
    signed_up += 1

    # while :
    # sent_books = total_days * books_per_day
    # op_string1 = str(lib_index) + ' '
    # op_string2 = ''
    # lib_scores = scores
    # libraries[lib_index] = []
    scores_id = {scores[book_id]: book_id for book_id in present_books_list[lib_index]}
    ctr = 0
    for i in range(books_per_day):
        print('scores_id:\n', scores_id)

        max_score = max(scores_id)
        book_id = scores_id[max_score]
        print('max_score:', max_score, 'book_id:', book_id)
        # score += max_score
        if book_id not in finished_books:
            finished_books.append(book_id)
            libraries[lib_index].append(book_id)
            ctr += 1
            book_no -= 1
        scores_id.pop(max_score)


print('signed_up = ', signed_up)
print('libraries = ', libraries)
# for item in libraries:
#     print(libraries.index(item), len(item))
#     print(' '.join(list(map(str, item))))
