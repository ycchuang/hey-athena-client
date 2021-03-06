"""
    Handles most general questions (including math!)

    Requires:
        - WolframAlpha API key

    Usage Examples:
        - "How tall is Mount Everest?"
        - "What is the derivative of y = 2x?"
"""

import wolframalpha

from athena.classes.module import Module
from athena.classes.task import ActiveTask
from athena import settings


class AnswerTask(ActiveTask):

    def match(self, text):
        return True

    def action(self, text):
        query = wolframalpha.Client(settings.WOLFRAM_KEY).query(text)

        if len(query.pods) > 1 and query.pods[1].text:
            answer = query.pods[1].text.replace('|', '')
            self.speak(answer, show_text=True)
        else:
            self.speak(settings.NO_MODULES, show_text=True)


class Wolfram(Module):

    def __init__(self):
        tasks = [AnswerTask()]
        super(Wolfram, self).__init__('wolfram', tasks, priority=0)
