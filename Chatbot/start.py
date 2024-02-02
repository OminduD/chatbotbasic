from telegram_menu import BaseMessage, TelegramMenuSession, NavigationHandler

API_KEY = "6567480470:AAHSfwEOPyJ6W_1Ma-IrNA5e51iTQczVLhs"

class StartMessage(BaseMessage):
    """Start menu, create all app sub-menus."""

    LABEL = "start"

    def __init__(self, navigation: NavigationHandler) -> None:
        """Init StartMessage class."""
        super().__init__(navigation, StartMessage.LABEL)

    def update(self) -> str:
        """Update message content."""
        return "Hello, I'm WhiteBeard!"
TelegramMenuSession(API_KEY).start(StartMessage)



