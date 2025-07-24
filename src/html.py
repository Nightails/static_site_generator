import os
from markdown_blocks import markdown_to_html_node


def extract_title(markdown):
    title_line = markdown.split("\n", 1)[0]
    if not title_line.startswith("# "):
        raise Exception("Invalid markdown: Unable to extract title")
    return title_line[2:].strip()


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # hard code index.md, since it is the only markdown right now
    md_path = os.path.join(from_path, "index.md")
    if not os.path.exists(md_path):
        raise Exception(
            f'Error: missing index.md in content. "{md_path}" does not exists.'
        )

    # hard code index.html as well for same reason
    html_path = os.path.join(dest_path, "index.html")

    # template is placed in project's root by default
    tmpl_path = os.path.join(template_path, "template.html")
    if not os.path.exists(template_path):
        raise Exception(f'Error: missing template.html. "{tmpl_path}" does not exists.')

    md_content = get_file_content(md_path)
    template_content = get_file_content(tmpl_path)

    title = extract_title(md_content)
    contents = markdown_to_html_node(md_content).to_html()

    new_html = template_content.replace("{{ Title }}", title)
    new_html = new_html.replace("{{ Content }}", contents)

    write_file_content(html_path, new_html)


def get_file_content(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except Exception as e:
        raise Exception(f'Error: Failed to read file "{file_path}": {str(e)}')


def write_file_content(file_path, content):
    try:
        with open(file_path, "w") as file:
            file.write(content)
            print(f'Sucess writting to "{file_path}')
    except Exception as e:
        raise Exception(f'Error: Failed to write to "{file_path}": {str(e)}')
