filter_genre = {'action': {'HBO':  ['Watchmen', 'The Pacific'],'TNT':  ['Top Gun', 'Terminator']},
                'romance': {'CBS': ['Mom', 'I love Lucy'],'ABC': ['The Bachelorette', 'Once Upon a Time']},
                'comedy': {'Fox': ['How I Met Your Mother', 'New Girl'],'Disney': ["That's So Raven", "Mickey's Playhouse"]}}

def all_genres():
    print(list(filter_genre.keys()))

def comedy_channels():
    print(list(filter_genre['comedy'].keys()))

def romance_channels():
    print(list(filter_genre['romance']))

def hbo_channel():
    print(filter_genre['action']['HBO'][1])

hbo_channel()