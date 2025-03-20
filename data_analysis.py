import pandas as pd
from scapy.all import rdpcap
from PyQt5.QtWidgets import QMainWindow, QAction, QFileDialog, QToolBar, QComboBox, QVBoxLayout, QWidget, QLabel, QMessageBox
from PyQt5.QtCore import Qt

class DataAnalyzer:
    def read_pcap_file(self, file_path):
        packets = rdpcap(file_path)

        data = []
        for packet in packets:
            if packet.haslayer("IP"):
                data.append({
                    "source_ip": packet["IP"].src,
                    "destination_ip": packet["IP"].dst,
                    "protocol": packet["IP"].proto,
                    "packet_size": len(packet)
                })
        df = pd.DataFrame(data)
        return df
    
    def plot_packet_size_distribution(self, df, ax, canvas):
        ax.clear()
        ax.hist(df['packet_size'], bins=50, color='skyblue', edgecolor='black')
        ax.set_title('Distribution of Packet Sizes')
        ax.set_xlabel('Packet Size')
        ax.set_ylabel('Frequency')
        canvas.draw()

    def plot_packet_size_vs_destination_ip(self, df, ax, canvas):
        ax.clear()
        ax.scatter(df['packet_size'], df['destination_ip'], color='green', alpha=0.5)
        ax.set_title('Packet Size vs. Destination IP')
        ax.set_xlabel('Packet Size')
        ax.set_ylabel('Destination IP')
        canvas.draw()

    def plot_top_source_ips(self, df, ax, canvas):
        ax.clear()
        if df is not None:
            top_source_ips = df['source_ip'].value_counts().head(10)
            print("Top Source IPs Data:")
            print(top_source_ips)
            top_source_ips.plot(kind='bar', color='skyblue', ax=ax)
            ax.set_title('Top Source IPs')
            ax.set_xlabel('Source IP Address',labelpad=15)
            ax.set_ylabel('Total Packet Count')
            canvas.draw()
        else:
            QMessageBox.warning(None, 'No Data', 'Please open a PCAP file first.')

    def plot_top_destination_ips(self, df, ax, canvas):
        ax.clear()
        if df is not None:
            top_destination_ips = df['destination_ip'].value_counts().head(10)
            print("Top Destination IPs Data:")
            print(top_destination_ips)
            top_destination_ips.plot(kind='bar', color='skyblue', ax=ax)
            ax.set_title('Top Destination IPs')
            ax.set_xlabel('Destination IP Address',labelpad=15)
            ax.set_ylabel('Total Packet Count')
            canvas.draw()
        else:
            QMessageBox.warning(None, 'No Data', 'Please open a PCAP file first.')

    def plot_analysis(self, selected_analysis, df, ax, canvas):
        if selected_analysis == 'Packet Size Distribution':
            print("Plotting Packet Size Distribution")
            self.plot_packet_size_distribution(df, ax, canvas)
        elif selected_analysis == 'Packet Size vs Destination IP':
            print("Plotting Packet Size vs Destination IP")
            self.plot_packet_size_vs_destination_ip(df, ax, canvas)
        elif selected_analysis == 'Top Source IPs':
            print("Plotting Top Source IPs")
            self.plot_top_source_ips(df, ax, canvas)
        elif selected_analysis == 'Top Destination IPs':
            print("Plotting Top Destination IPs")
            self.plot_top_destination_ips(df, ax, canvas)
