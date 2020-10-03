"""
Copyright 2020 Google LLC.
SPDX-License-Identifier: Apache-2.0
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