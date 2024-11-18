
'''
Create a javascript file that imports all the other javascript files except main.js
'''

import os

def make_all():
    # Get all the javascript files in the current directory
    files = [f for f in os.listdir() if f.endswith('.js') and f != 'main.js' and f != 'all.js']

    # Create a string that imports all the files
    imports = ''
    for f in files:
        p = f.split('.')[0]
        imports += f'export * as {p} from "./{f}";\n'

    # Write the string to a file
    with open('all.js', 'w') as f:
        f.write(imports)

if __name__ == '__main__':
    make_all()
    print ('all.js created')
