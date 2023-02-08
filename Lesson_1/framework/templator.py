from jinja2 import Template


def render(template_name, **kwargs):
    with open(template_name, encoding='utf-8') as f:
        template = Template(f.read())
    return template.render(**kwargs)


if __name__ == '__main__':
    output_test = render('../templates/index.html',
                         object_list=[{'name': 'Leo'}, {'name': 'Kate'}])
    print(output_test)
