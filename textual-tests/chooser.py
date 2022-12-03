from textual.app import App, ComposeResult
from textual.widgets import Static

TEXT = """
[b]Select Option[/b]
[@click=option_1()]Option 1[/]
[@click=option_2()]Option 2[/]
[@click=option_3()]Option 3[/]
"""


class ActionsApp(App):
    def compose(self) -> ComposeResult:
        yield Static(TEXT)


    def action_option_1(self) -> None:
        with open('output.txt', 'a', encoding='utf8') as outputFile:
            outputFile.write('Option 1\n')

    def action_option_2(self) -> None:
        with open('output.txt', 'a', encoding='utf8') as outputFile:
            outputFile.write('Option 2\n')

    def action_option_3(self) -> None:
        with open('output.txt', 'a', encoding='utf8') as outputFile:
            outputFile.write('Option 3\n')

if __name__ == "__main__":
    app = ActionsApp()
    app.run()
