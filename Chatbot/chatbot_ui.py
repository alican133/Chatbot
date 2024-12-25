from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTextBrowser, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
from chatbot_answer import cevap_ver


class ChatbotUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chatbot")
        self.setGeometry(300, 100, 600, 500)

        self.main_layout = QVBoxLayout(self)
        self.chat_layout = QVBoxLayout()
        self.input_layout = QHBoxLayout()

        self.chat_box = QTextBrowser(self)
        self.chat_box.setStyleSheet("background-color: #2E2E2E; color: #FFFFFF; font-size: 16px;")
        self.chat_layout.addWidget(self.chat_box)

        self.user_input = QLineEdit(self)
        self.user_input.setStyleSheet("background-color: #555555; color: #FFFFFF; font-size: 14px; padding: 5px;")
        self.user_input.setPlaceholderText("Mesajınızı yazın...")
        self.user_input.returnPressed.connect(self.trigger_send)
        self.input_layout.addWidget(self.user_input)

        self.send_button = QPushButton("Gönder", self)
        self.send_button.setStyleSheet("background-color: #0069D9; color: white; font-size: 14px; padding: 5px;")
        self.send_button.clicked.connect(self.send_message)
        self.input_layout.addWidget(self.send_button)

        self.main_layout.addLayout(self.chat_layout)
        self.main_layout.addLayout(self.input_layout)

    def send_message(self):
        user_text = self.user_input.text().strip()
        if user_text:
            self.chat_box.append(f'<div style="text-align: left; color: #00BFFF;">Sen: {user_text}</div>')

            bot_response = cevap_ver(user_text)

            self.chat_box.append(f'<div style="text-align: right; color: #90EE90;">Bot: {bot_response}</div>')

            self.user_input.clear()

    def trigger_send(self):
        self.send_button.click()
