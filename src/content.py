import os
from markdown_blocks import markdown_to_html_node


def extract_title(markdown):
    title_line = markdown.split("\n", 1)[0]
    if not title_line.startswith("# "):
        raise Exception("Invalid markdown: Unable to extract title")
    return title_line[2:]


def generate_page(from_path, template_path, dest_path):
    # hard code some directories for now
    from_path = os.path.join(from_path, "index.md")
    dest_path = os.path.join(dest_path, "index.html")

    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    md_file = open(from_path, "r")
    md_content = md_file.read()
    md_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    title = extract_title(md_content)
    html = markdown_to_html_node(md_content).to_html()

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)
