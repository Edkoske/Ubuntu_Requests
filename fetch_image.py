import os
import requests
from urllib.parse import urlparse
import uuid

def fetch_image():
    # Prompt user for URL
    url = input("Enter the URL of the image: ").strip()

    # Create directory for fetched images
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)

    try:
        # Fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Check for HTTP errors

        # Extract filename from URL or generate one
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        if not filename:  # If no filename, generate one
            filename = f"image_{uuid.uuid4().hex}.jpg"

        # Full path for saving
        filepath = os.path.join(save_dir, filename)

        # Save image in binary mode
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✅ Image saved successfully as: {filepath}")

    except requests.exceptions.MissingSchema:
        print("❌ Invalid URL. Please include http:// or https://")
    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("❌ Connection error. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("❌ Request timed out. Try again later.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    fetch_image()
