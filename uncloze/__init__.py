"""
This is an Anki add-on for version 2.1.34. It provides a custom field filter
called 'uncloze' which will remove the cloze deletion tags from a field.

For example, if I have a note with a field Foo containing:
    Canberra was founded in {{c1::1913}}.

And I want to show the text on the front of a card without the cloze tags like:
    Canberra was founded in 1913.

Then I can use this custom field filter:
    {{uncloze::Foo}}
"""

import re

from anki import hooks
from anki.template import TemplateRenderContext

cloze_regex = re.compile(r"{{c\d+::(?P<text>.*?)}}")
cloze_repl = r"\g<text>"

def uncloze_field_filter(
    field_text: str,
    field_name: str,
    filter_name: str,
    context: TemplateRenderContext
) -> str:
    if filter_name != "uncloze":
        return field_text
    return re.sub(cloze_regex, cloze_repl, field_text)

hooks.field_filter.append(uncloze_field_filter)