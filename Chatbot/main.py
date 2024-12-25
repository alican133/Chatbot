import sys
from PyQt5.QtWidgets import QApplication
from chatbot_ui import ChatbotUI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    chatbot_ui = ChatbotUI()
    chatbot_ui.show()
    sys.exit(app.exec_())
