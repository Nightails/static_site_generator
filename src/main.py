import os
import shutil
import static
import content


STATIC_DIR = "./static"
CONTENT_DIR = "./content"
PUBLIC_DIR = "./public"
TEMPLATE_PATH = "./template.html"


def main():
    print("Deletings public directory...")
    if os.path.exists(PUBLIC_DIR):
        shutil.rmtree(PUBLIC_DIR)
        os.mkdir(PUBLIC_DIR)

    print("Copyting static files to public directory...")
    static.copy_static_contents(STATIC_DIR, PUBLIC_DIR)
    print("Generating pages...")
    content.generate_page_recursive(CONTENT_DIR, TEMPLATE_PATH, PUBLIC_DIR)


main()
