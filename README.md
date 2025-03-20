# Network Traffic Analyzer

This project is a **PCAP (packet capture) file analyzer** built using **PyQt5** and **Matplotlib**. It provides a graphical user interface (GUI) to analyze network traffic by visualizing various aspects of captured network packets.

## Features

- **Load and Analyze PCAP Files**: Open and process `.pcap` or `.pcapng` files to extract network packet details.
- **Multiple Analysis Options**:
  - **Packet Size Distribution**: Histogram of packet sizes.
  - **Packet Size vs Destination IP**: Scatter plot of packet sizes per destination IP.
  - **Top Source IPs**: Bar chart of the most frequent source IPs.
  - **Top Destination IPs**: Bar chart of the most frequent destination IPs.
- **Interactive GUI**:
  - Toolbar for opening files and updating plots.
  - Dropdown menu for selecting different analysis types.
  - Dynamic Matplotlib-based visualizations.

## Installation

### Prerequisites
Ensure you have **Python 3.x** installed along with the following dependencies:

```bash
pip install pandas scapy PyQt5 matplotlib
```

### Running the Application
Run the `main.py` file to start the GUI:

```bash
python main.py
```

## File Structure

- `main.py` – Entry point for the application.
- `ui_components.py` – Defines the GUI layout and interactions.
- `data_analysis.py` – Handles packet processing and data visualization.

## Usage

1. Open a `.pcap` file from the toolbar.
2. Choose an analysis type from the dropdown.
3. Click **Update Plot** to generate the visualization.

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

## Contributing

Feel free to submit issues and pull requests if you have any improvements or bug fixes.

## Acknowledgments

- Built using **PyQt5** for GUI
- **Scapy** for packet analysis
- **Matplotlib** for data visualization

