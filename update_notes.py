import os
import re

# Define the path to your notes directory and the index file
notes_dir = os.path.join("notes")
index_file = os.path.join(notes_dir, "index.md")

# List of folders to ignore
ignored_folders = ['.obsidian', 'images', 'notes', 'dsa']

# Function to extract the title from the front matter of a Markdown file
def extract_title_from_markdown(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
        # Match the YAML front matter and extract the title if it exists
        match = re.search(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
        if match:
            front_matter = match.group(1)
            title_match = re.search(r"title:\s*(.+)", front_matter)
            if title_match:
                return title_match.group(1).strip()
        
        # If no title is found, return a default title (filename without .md)
        return os.path.basename(file_path).replace(".md", "").replace("-", " ").capitalize()

def generate_note_sections():
    sections = []
    
    # Walk through each folder and file in the notes directory
    for root, dirs, files in os.walk(notes_dir):
        # Skip the root folder itself (we want subfolders like 'linux', 'aws')
        if root == notes_dir:
            continue

        # Get the folder name (e.g., 'linux', 'aws')
        folder_name = os.path.basename(root)

        # Ignore the specified folders
        if folder_name in ignored_folders:
            continue

        # Add a heading (Heading 3 for folder name, no capitalization)
        section = f"### {folder_name}\n"

        # List all markdown files within the folder
        for file in sorted(files):
            if file.endswith(".md"):
                # Generate a relative path to the markdown file (Unix-style)
                relative_path = os.path.join(folder_name, file).replace("\\", "/")

                # Extract the title from the markdown file
                title = extract_title_from_markdown(os.path.join(root, file))

                # Add a bullet point with the link
                section += f"- [{title}]({relative_path})\n"

        # Only add the section if it contains files
        if section.strip():
            sections.append(section)

    return sections

def update_index_md():
    # Header of the index.md file
    header = """---
layout: page
title: Notes
permalink: /notes
---

A raw collection of my notes, seamlessly synced with my **OBSIDIAN** vault, capturing my ongoing explorations, and personal learning across various domains, continuously updated as part of my knowledge base.

"""

    # Generate sections for each folder and its markdown files
    sections = generate_note_sections()

    # Combine the header with the sections
    content = header + "\n".join(sections)

    # Write to the index.md file
    os.makedirs(os.path.dirname(index_file), exist_ok=True)  # Ensure 'notes' directory exists
    with open(index_file, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"{index_file} has been updated.")

if __name__ == "__main__":
    update_index_md()
