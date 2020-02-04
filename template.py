import yaml
import argparse
import pystache
import os
import pathlib
import errno

def get_template_files(path: str):
    for entry in os.scandir(path):
        if entry.is_dir():
            yield from get_template_files(entry.path)
        
        if entry.is_file() and entry.path.endswith(".template"):
            yield os.path.abspath(entry.path)

def ensure_path(filename: str):
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

def write_templates(method: str, item):
    print("Processing templates for '{:s}'...".format(method))

    # Get our templates paths
    template_path = os.path.join(method, '_templates')
    template_files = list(get_template_files(template_path))

    versions = item.get('versions')

    # Need to extract the version info
    for version_key in versions:
        print("----\n{:s}\n----".format(version_key))

        version = versions.get(version_key)
        version_data = version.get('data')
        
        path = os.path.join(method, version_key)

        # Template
        for template_file in template_files:
            print("Reading '{:s}'...".format(template_file))

            with open(template_file, 'r') as file_template:
                # The raw template string
                template_string = file_template.read()

                # Render the template
                rendered_template = pystache.render(template_string, version_data)

                outfile_path = os.path.abspath(os.path.join(path, os.path.relpath(template_file, template_path)[:-9]))

                # Create path if not exist
                ensure_path(outfile_path)

                print("Writting '{:s}'...".format(outfile_path))

                with open(outfile_path, 'w+') as outfile:
                    outfile.write(rendered_template)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('method', help='method', type=str)

    # Parse arguments
    args = parser.parse_args()
    if args.method == None:
        print("Unknown method")
        exit()

    # Open manifest file to read
    with open(r'manifest.yaml') as yaml_file:
        documents = yaml.load(yaml_file, Loader=yaml.FullLoader)
        item = documents.get(args.method)

        if item == None:
            print("Unknown method: " + args.method)
            exit()

        write_templates(args.method, item)

if __name__ == "__main__":
    main()

    print("\nFinished!")