import os
import sys
from pathlib import Path

def get_comment(rel_path: str, is_dir: bool, name: str) -> str:
    """
    Return a comment string for a given path (relative to the root directory).
    Customize this function to add your own annotations.
    """
    # Normalize path separators
    rel_path = rel_path.replace('\\', '/')
    
    # Comments for specific directories
    if rel_path == 'onboarding':
        return "# النسخة القديمة (بعد التعديلات)"
    if rel_path in ('schedule', 'settings', 'support', 'tickets'):
        return "# النسخة القديمة"
    if rel_path == 'presentation/screens':
        return "# النسخة الجديدة (Clean Architecture)"
    if rel_path == 'presentation/screens/onboarding':
        return "# هذه تحتوي على نفس الكود (أو مجرد إعادة تصدير)"
    
    # Comments for specific files inside presentation/screens/
    if rel_path.startswith('presentation/screens/') and not is_dir and name.endswith('.dart'):
        # Skip the onboarding directory itself
        if 'onboarding' not in rel_path:
            return "(إعادة تصدير)"
    
    return ""

def print_tree(directory: Path, output_lines: list, prefix: str = "", is_last: bool = True, root_rel_path: str = ""):
    """
    Recursively build the directory tree lines and append to output_lines list.
    """
    # Determine the relative path from the root directory
    if root_rel_path == "":
        current_rel = ""
    else:
        current_rel = root_rel_path
    
    # Get all items in the directory, sorted (directories first, then files)
    try:
        items = list(directory.iterdir())
    except PermissionError:
        return
    
    items.sort(key=lambda x: (not x.is_dir(), x.name))
    
    for i, item in enumerate(items):
        is_last_item = (i == len(items) - 1)
        connector = "└── " if is_last_item else "├── "
        
        # Build the relative path for this item
        if current_rel:
            item_rel = f"{current_rel}/{item.name}"
        else:
            item_rel = item.name
        
        # Get comment if any
        comment = get_comment(item_rel, item.is_dir(), item.name)
        comment_str = f" {comment}" if comment else ""
        
        # Add the line to output list
        output_lines.append(f"{prefix}{connector}{item.name}{comment_str}")
        
        # Recurse into subdirectories
        if item.is_dir():
            extension = "    " if is_last_item else "│   "
            print_tree(item, output_lines, prefix + extension, is_last_item, item_rel)

def main():
    # Get directory path from command line argument or user input
    if len(sys.argv) > 1:
        dir_path = sys.argv[1]
    else:
        dir_path = input("Enter directory path: ").strip()
    
    root = Path(dir_path).resolve()
    if not root.exists() or not root.is_dir():
        print(f"Error: '{dir_path}' is not a valid directory.")
        return
    
    # Build output lines
    output_lines = [f"{root.name}/"]
    print_tree(root, output_lines)
    
    # Write to file
    output_file = Path("app-root.md")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))
    
    print(f"Directory tree written to {output_file.absolute()}")

if __name__ == "__main__":
    main()
