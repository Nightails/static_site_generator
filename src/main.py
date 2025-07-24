import os
import shutil
import static
import content


static_dir = "./static"
content_dir = "./content"
public_dir = "./public"
template_path = "./template.html"


def main():
    print("Deletings public directory...")
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
        os.mkdir(public_dir)

    print("Copyting static files to public directory...")
    static.copy_static_contents(static_dir, public_dir)
    print("Generating pages...")
    content.generate_page(content_dir, template_path, public_dir)


main()
