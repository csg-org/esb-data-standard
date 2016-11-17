'''
Parse datapackage to autogenerate documentation
'''
import re
import json
from pathlib import Path

def decorate_links(text, words):
    '''
    Adds rst-style references to words that appear in text

    Positional arguments:
    text -- text to be parsed for references
    words -- words to look for in the provided text
    '''
    regex = re.compile('(\\b(?:{})\\b)'.format('|'.join(words)))

    # based on http://www.saltycrane.com/blog/2007/10/using-pythons-finditer-to-highlight/
    i = 0
    output = ''
    for match in regex.finditer(text):
        output += ''.join(
            [
                text[i:match.start()],
                ':ref:`',
                text[match.start():match.end()],
                '`'
            ])
        i = match.end()

    return ''.join([output, text[i:]])

def create_docs(fields):
    '''
    Create rst documentation fragment from datapackage fields

    Positional arguments
    fields -- datapackage fields
    '''
    output_file = Path('source/csv/standard.rst.part')
    core_template = """{ref_label}

{name}
{name_header}
{constraints}

{description}

{enumerations}

"""
    field_names = [field['name'] for field in fields]

    with output_file.open('w') as rst:
        for field in fields:
            constraints = ''
            unique = ''
            enumerations = ''

            if 'constraints' in field:
                if 'required' in field['constraints']:
                    constraints = 'This field is required'
                if 'unique' in field['constraints'] and field['constraints']['unique']:
                    unique = 'and must be unique'

                if 'required' in field['constraints'] or 'unique' in field['constraints']:
                    constraints = ' '.join([constraints, unique]).strip() + '.'

                if 'enum' in field['constraints']:
                    enum_list = []
                    for enum in field['constraints']['enum']:
                        enum_list.append('- {}'.format(enum))

                    enumerations = '\n'.join(enum_list)

            rst.write(core_template.format(
                ref_label='.. _{}:'.format(field['name']),
                name=field['name'],
                name_header='`' * len(field['name']),
                constraints='*{}*'.format(constraints) if constraints else '',
                description=decorate_links(field['description'], field_names),
                enumerations=enumerations
            ))


def main():
    '''Starts the process of generating documentation'''
    datapackage = Path('../datapackage.json')

    if datapackage.exists():
        with datapackage.open() as data_file:
            data = json.loads(data_file.read())
            json_fields = [field for field in data['resources'][0]['schema']['fields']]

            create_docs(json_fields)

if __name__=='__main__':
    main()
