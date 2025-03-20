import sys
from PyQt5.QtWidgets import QApplication
from ui_components import NetworkTrafficAnalyzer

if __name__ == '__main__':
    app = QApplication(sys.argv)
    analyzer = NetworkTrafficAnalyzer()
    analyzer.show()
    sys.exit(app.exec_())

