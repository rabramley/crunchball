#!/usr/bin/env python

import yaml
from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader
from shutil import copyfile

def produce_cards(card_type):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('{0}.html'.format(card_type))

    with open('{0}.yaml'.format(card_type), 'r') as players_yaml:
        cards = yaml.load(players_yaml)

    template_vars = {"cards": cards}

    html = template.render(template_vars)

    text_file = open('/components_pdfs/{0}.html'.format(card_type), "w")
    text_file.write(html)
    text_file.close()

    HTML(string=html, base_url='.').write_pdf('/components_pdfs/{0}.pdf'.format(card_type))

produce_cards('players')
produce_cards('plays')

copyfile('./main.css', '/components_pdfs/main.css')
copyfile('./players.css', '/components_pdfs/players.css')
copyfile('./plays.css', '/components_pdfs/plays.css')

