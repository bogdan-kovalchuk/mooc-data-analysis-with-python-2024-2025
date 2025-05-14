#!/usr/bin/env python3


def file_extensions(filename):
    no_extensions = []
    with_extensions = {}

    with open(filename) as f:
        for line in f:
            file = line.strip()
            name, extension = (file.rsplit(".", 1) + [None])[:2]

            if extension:
                with_extensions.setdefault(extension, []).append(file)
            else:
                no_extensions.append(file)

    return no_extensions, with_extensions


def main():
    no_extensions, with_extensions = file_extensions("src/filenames.txt")
    print(f"{len(no_extensions)} files with no extension")
    for k, v in with_extensions.items():
        print(f"{k} {len(v)}")


if __name__ == "__main__":
    main()
