import requests

def download_image(image_url, save_path):
    try:
        
        response = requests.get(image_url)
        
        
        if response.status_code == 200:
            
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print(f"Image successfully downloaded: {save_path}")
        else:
            print(f"Failed to retrieve image. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")


image_url = input("Please enter the image URL: ")
save_path = input("Please enter the save path (including the filename and extension, e.g., 'downloaded_image.jpg'): ")

download_image(image_url, save_path)