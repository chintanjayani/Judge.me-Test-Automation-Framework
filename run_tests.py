import os
import sys
import subprocess
from utilities.os_utils import is_windows

def run_tests():
    """Run tests with OS-specific configurations"""
    # Set up environment variables
    os.environ['PYTHONPATH'] = os.path.dirname(os.path.abspath(__file__))
    
    # Determine OS-specific commands
    if is_windows():
        python_path = os.path.join('venv', 'Scripts', 'python')
    else:
        python_path = os.path.join('venv', 'bin', 'python')

    # Build pytest command
    cmd = [
        python_path,
        '-m',
        'pytest',
        '-v',
        '--html=reports/report.html',
        '--self-contained-html',
        'tests/'
    ]

    # Run tests
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Tests failed with exit code: {e.returncode}")
        sys.exit(e.returncode)

if __name__ == '__main__':
    run_tests()