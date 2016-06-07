"""
Copyright (C) Solomon Astley
Code to generate SVG files for the US States based on a collection of SVG
files online, available at wikimedia.org
"""

import urllib.request
import fileinput
import sys
from bs4 import BeautifulSoup

url = 'https://commons.wikimedia.org/wiki/Category:LGBT_flag_maps_of_United_States'
response = urllib.request.urlopen(url)
soup = BeautifulSoup(response.read(), 'html.parser')

for link in soup.find_all('a'):
    url = link.get('href')
    if url != None:
        if 'flag_map_of' in url and 'United_States' not in url:
            url = 'https://commons.wikimedia.org' + url
            response = urllib.request.urlopen(url)
            soup2 = BeautifulSoup(response.read(), 'html.parser')
            link = soup2.find_all('a', { 'class' : 'internal' })
            url = link[0].get('href')

            sections = url.split('_')
            filename = sections[len(sections) - 2] + '_' + sections[len(sections) - 1]
            if 'of_' in filename:
                filename = sections[len(sections) - 1]
            print('Getting and editing ' + filename)

            with urllib.request.urlopen(url) as response, open(filename, 'w') as out_file:
                svg = response.read().decode('utf-8')
                out_file.write(svg)
                out_file.close()
            for line in fileinput.input(filename, inplace=True):
                strip = line.strip()
                if strip == 'style="fill:#e40303"':
                    sys.stdout.write(
                        '\t style="fill:#9FAEC0"\n'
                        '\t stroke="#9FAEC0"\n'
                        '\t stroke-width="10"\n'
                        '\t transform="translate(0, 125)"\n'
                    )
                elif strip == 'style="fill:#ff8c00"':
                    sys.stdout.write(
                        '\t style="fill:#9FAEC0"\n'
                        '\t stroke="#9FAEC0"\n'
                        '\t stroke-width="10"\n'
                        '\t transform="translate(0, 100)"\n'
                    )
                elif strip == 'style="fill:#ffed00"':
                    sys.stdout.write(
                        '\t style="fill:#9FAEC0"\n'
                        '\t stroke="#9FAEC0"\n'
                        '\t stroke-width="10"\n'
                        '\t transform="translate(0, 75)"\n'
                    )
                elif strip == 'style="fill:#008026"':
                    sys.stdout.write(
                        '\t style="fill:#9FAEC0"\n'
                        '\t stroke="#9FAEC0"\n'
                        '\t stroke-width="10"\n'
                        '\t transform="translate(0, 50)"\n'
                    )
                elif strip == 'style="fill:#004dff"':
                    sys.stdout.write(
                        '\t style="fill:#9FAEC0"\n'
                        '\t stroke="#9FAEC0"\n'
                        '\t stroke-width="10"\n'
                        '\t transform="translate(0, 25)"\n'
                    )
                elif strip == 'style="fill:#750787"':
                    sys.stdout.write(
                        '\t style="fill:#9FAEC0"\n'
                        '\t stroke="#9FAEC0"\n'
                        '\t stroke-width="10"\n'
                    )
                else:
                    sys.stdout.write(line)
