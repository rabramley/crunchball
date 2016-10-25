#!/usr/bin/env python

import yaml
from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader
from shutil import copyfile

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("players.html")

with open("players.yaml", 'r') as players_yaml:
	players = yaml.load(players_yaml)

template_vars = {"title" : "This is a test",
                 "players": players}

html = template.render(template_vars)

text_file = open("/components_pdfs/players.html", "w")
text_file.write(html)
text_file.close()

copyfile('./main.css', '/components_pdfs/main.css')
copyfile('./players.css', '/components_pdfs/players.css')

HTML(string=html, base_url='.').write_pdf('/components_pdfs/players.pdf')
