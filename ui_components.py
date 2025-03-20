import os
from PyQt5.QtWidgets import QMainWindow, QAction, QFileDialog, QToolBar, QComboBox, QVBoxLayout, QWidget, QLabel, QMessageBox
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from data_analysis import DataAnalyzer

class NetworkTrafficAnalyzer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Network Traffic Analysis')
        self.df = None
        self.data_analyzer = DataAnalyzer()  # Initialize DataAnalyzer
        self.create_toolbar()
        self.create_file_info_label()
        self.create_main_frame()
        self.create_statusbar()  
        self.setGeometry(100, 60, 1020, 980) 
        self.showMaximized()


    def create_toolbar(self):
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        open_action = QAction('Open PCAP', self)
        open_action.triggered.connect(self.browse_file)
        toolbar.addAction(open_action)

        update_action = QAction('Update Plot', self)
        update_action.triggered.connect(self.update_plot)
        toolbar.addAction(update_action)

        toolbar.setStyleSheet("QToolButton { background-color: white;border: 1px solid gray;padding:20px}")

    def create_statusbar(self):
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')

    def create_main_frame(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.analysis_options = QComboBox()
        self.analysis_options.addItems(['Select Analysis', 'Packet Size Distribution', 'Packet Size vs Destination IP', 'Top Source IPs', 'Top Destination IPs'])
        self.setStyleSheet("QComboBox{ padding:20px;}")
        layout.addWidget(self.analysis_options)

        self.fig = plt.Figure(figsize=(5, 5))
        self.canvas = FigureCanvas(self.fig)
        layout.addWidget(self.canvas)
        self.ax = self.fig.add_subplot(111, position=[0.1, 0.2, 0.85, 0.75])

    def create_file_info_label(self):
        self.file_info_label = QLabel()
        self.file_info_label.setAlignment(Qt.AlignBottom)
        self.file_info_label.setMargin(5)
        self.statusBar().addWidget(self.file_info_label)

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open PCAP', '', 'PCAP files (*.pcap *.pcapng)')
        if file_path:
            self.df = self.data_analyzer.read_pcap_file(file_path)
            self.analysis_options.setEnabled(True)
            self.analysis_options.setCurrentIndex(0)
            self.statusbar.showMessage(f'File loaded: {file_path}')
        else:
            self.analysis_options.setEnabled(False)
            self.statusbar.showMessage('File selection canceled.')
            self.file_info_label.clear()

    def update_plot(self):
        selected_analysis = self.analysis_options.currentText()
        if selected_analysis == 'Select Analysis':
            QMessageBox.warning(self, 'No Analysis Selected', 'Please select an analysis from the dropdown menu.')
            return
        if self.df is not None:
            print(f"Selected Analysis: {selected_analysis}")
            self.data_analyzer.plot_analysis(selected_analysis, self.df, self.ax, self.canvas)
        else:
            QMessageBox.warning(self, 'No Data', 'Please open a PCAP file first.')