from note_module import NoteBook
from note_module import Note

quote_book = NoteBook("The Quoto Book")

new_note = Note()
new_note.write_content("Don't cry because it's over smile because it happened. -Dr.Seuss")

quote_book.add_note(new_note)

print(quote_book.get_number_of_pages())

quote_book.add_note(Note("Hello, World1"))
quote_book.add_note(Note("Hello, World2"))
quote_book.add_note(Note("Hello, World3"))
quote_book.add_note(Note("Hello, World4"))
quote_book.add_note(Note("Hello, World5"))

print(quote_book.get_number_of_pages())

my_note = quote_book.remove_note(1)
print(my_note)

print(quote_book.get_number_of_pages())
