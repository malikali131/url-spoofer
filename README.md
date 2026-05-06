# Redirection-Analytics: Peer Security Awareness Tool

## 📌 Overview
This project is a **Social Engineering Simulation Tool** designed for cybersecurity researchers and educators. It demonstrates how attackers manipulate **Open Graph (OG) metadata** to spoof link previews in messaging apps like WhatsApp, Discord, and Telegram.

The tool provides a Flask-based redirection server that captures visitor telemetry (IP, User-Agent, Platform) before redirecting them to a safe destination.

## 🚀 Features
* **Dynamic Metadata Masking:** Generates convincing "Google Meet" link previews.
* **Real-time Telemetry:** Logs visitor IP addresses and device information for audit trails.
* **Automated Tunneling:** Integrated with `pyngrok` to make local research public instantly.
* **Intervention Page:** A brief loading screen to simulate professional redirection flows.

## 🛠️ Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Redirection-Analytics.git](https://github.com/YOUR_USERNAME/Redirection-Analytics.git)
   cd Redirection-Analytics
