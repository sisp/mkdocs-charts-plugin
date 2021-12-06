from pymdownx.superfences import _escape


def fence_vegalite_custom(source, language, class_name, options, md, **kwargs):
    """
    Inspired by https://github.com/facelessuser/pymdown-extensions/blob/8ee5b5caec8f9373e025f50064585fb9d9b71f86/pymdownx/superfences.py#L146
    """  # noqa

    classes = kwargs["classes"]
    id_value = kwargs["id_value"]
    attrs = kwargs["attrs"]

    if class_name:
        classes.insert(0, class_name)

    id_value = ' id="{}"'.format(id_value) if id_value else ""
    classes = ' class="{}"'.format(" ".join(classes)) if classes else ""
    attrs = (
        " " + " ".join('{k}="{v}"'.format(k=k, v=v) for k, v in attrs.items())
        if attrs
        else ""
    )

    # plan:
    # traverse upwards untill you find the `mkdocs.yml` file
    # read that,
    # find the directory of the docs_dir
    # parse the json, get the schema url, look in the docs_dir, read the JSON
    # return the source
    # import os
    # print(os.getcwd())
    # from pathlib import Path
    # import json
    # schema = json.loads(Path("docs/assets/charts/schemaone.json").read_text())

    print(f"name: {class_name}")
    print(f"attrs: {attrs}\n\n")
    return f"<vegachart style='width: 100%' {id_value}{classes}{attrs}>{_escape(source)}</vegachart>"
