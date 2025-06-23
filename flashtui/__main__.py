from textual.app import App, ComposeResult
from textual.containers import HorizontalGroup, VerticalScroll
from textual.widgets import Button, Footer, Header


class Flashtui(App):
    BINDINGS = [('d', 'toggle_dark', 'Toggle dark mode')]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == 'textual-light' else 'textual-light'
        )


if __name__ == "__main__":
    app = Flashtui()
    app.run()
