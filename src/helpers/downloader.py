import requests
from pathlib import Path

def download_to_local(url: str, out_path: Path, parent_mkdir: bool=True) -> None:
    """
    Downloads a file from the given URL and saves it to the specified local path.
    
    Args:
        url (str): The URL of the file to download.
        out_path (Path): The out path is the local path where the file should be saved.
    """
    if not isinstance(out_path, Path):
        raise ValueError(f"{out_path} is not a valid Path object.")
    
    if parent_mkdir:
        out_path.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an error for bad responses
        
        out_path.write_bytes(response.content)
        return True
    
    except requests.RequestException as e:
        print(f"Error downloading file from {url}: {e}")
        return False