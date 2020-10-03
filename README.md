# Anki uncloze

This is an Anki add-on for version 2.1.34. It provides a custom field filter
called `uncloze` which will remove the cloze deletion tags from a field.

For example, if I have a note with field `Foo` containing `Canberra was founded
in {{c1::1913}}`. And I want to show the text on the front of a card without the
cloze tags like `Canberra was founded in 1913.` Then I can use this custom field
filter: `{{uncloze::Foo}}`
