# from PySide6.QtGui import QAction
# from PySide6.QtWidgets import QApplication, QLabel, QMenu, QMainWindow
# from PySide6.QtCore import Qt
# import sys


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Right-Click Context Menu Example")
        
#         # Add a label or any other widget
#         self.label = QLabel("Right-click me!", self)
#         self.label.setAlignment(Qt.AlignCenter)
#         self.setCentralWidget(self.label)

#     def contextMenuEvent(self, event):
#         # Create the context menu
#         context_menu = QMenu(self)
        
#         # Add actions to the menu
#         action1 = QAction("Action 1", self)
#         action1.triggered.connect(self.do_action1)
        
#         action2 = QAction("Action 2", self)
#         action2.triggered.connect(self.do_action2)
        
#         # Add actions to the context menu
#         context_menu.addAction(action1)
#         context_menu.addAction(action2)
        
#         # Show the context menu at the mouse click position
#         context_menu.exec(event.globalPos())
        
#     def do_action1(self):
#         self.label.setText("Action 1 triggered")
    
#     def do_action2(self):
#         self.label.setText("Action 2 triggered")


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.resize(300, 200)
#     window.show()
#     sys.exit(app.exec())


import os


os.environ['LANGCHAIN_TRACING_V2']='True'
os.environ['LANGCHAIN_ENDPOINT']="https://api.smith.langchain.com"
os.environ['LANGCHAIN_API_KEY']="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"
os.environ['LANGCHAIN_PROJECT']="pr-notable-descent-17"




# import openai
# from langsmith.wrappers import wrap_openai
# from langsmith import traceable

# # Auto-trace LLM calls in-context
# client = wrap_openai(openai.Client())

# @traceable # Auto-trace this function
# def pipeline(user_input: str):
#     result = client.chat.completions.create(
#         messages=[{"role": "user", "content": user_input}],
#         model="gpt-3.5-turbo"
#     )
#     return result.choices[0].message.content

# pipeline("Hello, world!")
# # Out:  Hello there! How can I assist you today?