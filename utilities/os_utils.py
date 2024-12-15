import platform
import os

def is_windows():
    return platform.system().lower() == 'windows'

def is_mac():
    return platform.system().lower() == 'darwin'

def is_linux():
    return platform.system().lower() == 'linux'

def get_screenshots_dir():
    """Get OS-appropriate screenshots directory"""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, 'reports', 'screenshots')

def ensure_dir_exists(dir_path):
    """Ensure directory exists, create if it doesn't"""
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)