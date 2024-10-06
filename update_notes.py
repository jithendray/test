import os
import re

# Define the path to your notes directory and the index file
notes_dir = "notes"
index_file = os.path.join(notes_dir, "index.md")

# Function to extract the title from the front matter of a Markdown file
def extract_title_from_markdown(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
        # Match the YAML front matter and extract the title if it exists
        # Regular expression to match the title in YAML front matter
        match = re.search(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
        
        if match:
            # Extract the front matter block
            front_matter = match.group(1)
            # Look for the 'title' field within the front matter
            title_match = re.search(r"title:\s*(.+)", front_matter)
            
            if title_match:
                return title_match.group(1).strip()
        
        # If no title is found, return a default title (filename without .md)
        return os.path.basename(file_path).replace(".md", "").replace("-", " ").capitalize()

def generate_note_sections():
    # This will store all the sections for each folder
    sections = []

    # Walk through each folder and file in the notes directory
    for root, dirs, files in os.walk(notes_dir):
        if root == notes_dir:
            # Skip the root folder (we're only interested in subfolders like 'linux', 'aws')
            continue

        # Get the folder name (e.g., 'linux', 'aws')
        folder_name = os.path.basename(root)

        # Add a heading (Heading 3 for folder name)
        section = f"### {folder_name.capitalize()}\n"

        # List all markdown files within the folder
        for file in sorted(files):
            if file.endswith(".md"):
                # Generate a relative path to the markdown file
                relative_path = os.path.join(folder_name, file).replace("\\", "/")

                # Extract the title from the markdown file
                title = extract_title_from_markdown(os.path.join(root, file))

                # Add a bullet point with the link
                section += f"- [{title}]({relative_path})\n"

        # Add the section to the list if it contains any notes
        if section.strip():
            sections.append(section)

    return sections

def update_index_md():
    # Create the header of the index.md file
    header = """---
layout: page
title: Notes
permalink: /notes
---

learning notes from various sources

"""

    # Generate sections for each folder and its markdown files
    sections = generate_note_sections()

    # Combine the header with the sections
    content = header + "\n".join(sections)

    # Write to the index.md file
    with open(index_file, "w") as f:
        f.write(content)

    print(f"{index_file} has been updated.")

if __name__ == "__main__":
    update_index_md()
