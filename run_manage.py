import os
import sys

def main():
    # Adjust the path to point to where manage.py is supposed to be
    project_root = os.path.dirname(os.path.abspath(__file__))
    backend_path = os.path.join(project_root, 'Math-practice', 'backend')
    
    if backend_path not in sys.path:
        sys.path.append(backend_path)
    
    # Change directory to backend to make relative paths in django work
    os.chdir(backend_path)
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Pass arguments to execute_from_command_line
    # sys.argv[0] is this script, so we replace it or keep it, but we need to pass the rest
    args = ['manage.py'] + sys.argv[1:]
    execute_from_command_line(args)

if __name__ == '__main__':
    main()

