#!/usr/bin/env python

from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("template.html")

players = [
	{
		'first_name': 'Mike',
		'last_name' : 'Cruncher',
		'position' : 'Defence',
		'flavour' : 'Mike is a hunky defender that has broken as many heart as he has ankles.'
	},
	{
		'first_name': 'Tony',
		'last_name' : 'Cleaver',
		'position' : 'Defence',
		'flavour' : 'Tony doesn\'t think much, and then only in single syllables.'
	},
	{
		'first_name': 'Dave',
		'last_name' : 'Mallet',
		'position' : 'Defence',
		'flavour' : 'Dave loves smashing bones almost as much as he loves his old mum.'
	},
	{
		'first_name': 'Archibald',
		'last_name' : 'Talbot',
		'position' : 'Defence',
		'flavour' : 'Archie is as crafty as they come.'
	},
	{
		'first_name': 'Terence',
		'last_name' : 'Swiftfoot',
		'position' : 'Attack',
		'flavour' : 'You could call Terry quick, but he won\'t hear as he\'ll already be 40 yards away.'
	},
	{
		'first_name': 'Ethelbert',
		'last_name' : 'Skillton',
		'position' : 'Attack',
		'flavour' : 'Elthelbert is a practitioner of the beautiful game.'
	}
]

template_vars = {"title" : "This is a test",
                 "players": players}

html = template.render(template_vars)

HTML(string=html, base_url='.').write_pdf('/components_pdfs/players.pdf')
