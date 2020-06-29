'''
Parse tableschema to autogenerate documentation
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
    Create rst documentation fragment from tableschema fields

    Positional arguments
    fields -- tableschema fields
    '''
    output_file = Path('source/csv/standard.rst.part')
    core_template = """{ref_label}

{name}
{name_header}
{data_type}

{constraints}

{description}

{enumerations}

"""
    data_type_reference_url_tmpl = '../formatting/#{}'
    field_names = [field['name'] for field in fields]
    data_types = list(set([field['type'] for field in fields]))

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
                
                enum_list = []
                if 'enum' in field['constraints'] or 'esb$enum' in field['constraints']:
                    ''' For enums that cannot currently be enforced using tableschema tools
                    we still want them in our documentation, use esb$enum as magic string ''' 
                    for enum in (field['constraints'].get('enum') or []) + (field['constraints'].get('esb$enum') or []):
                        enum_list.append('- {}'.format(enum))
                
                    enumerations = 'The value of ``{}`` must be one of the following:\n\n'.format(
                        field['name']) + '\n'.join(enum_list)

            rst.write(core_template.format(
                ref_label='.. _{}:'.format(field['name']),
                name=field['name'],
                name_header='`' * len(field['name']),
                data_type='**Data Type:** `{}`_'.format(field['type']),
                constraints='*{}*'.format(constraints) if constraints else '',
                description=decorate_links(field['description'], field_names),
                enumerations=enumerations
            ))

        for data_type in data_types:
            rst.write('.. _{}: {}\n'.format(
                data_type,
                data_type_reference_url_tmpl.format(data_type)
            ))

def main():
    '''Starts the process of generating documentation'''
    tableschema = Path('../tableschema.json')

    if tableschema.exists():
        with tableschema.open() as data_file:
            data = json.loads(data_file.read())
            json_fields = [field for field in data['fields']]

            create_docs(json_fields)

if __name__=='__main__':
    main()
