import os
import shutil
import static
import html


static_dir = "./static"
content_dir = "./content"
public_dir = "./public"


def main():
    print("Deletings public directory...")
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
        os.mkdir(public_dir)

    print("Copyting static files to public directory...")
    static.copy_static_contents(static_dir, public_dir)
    print("Generating html files to public directory...")
    html.generate_page(content_dir, os.getcwd(), public_dir)


main()
