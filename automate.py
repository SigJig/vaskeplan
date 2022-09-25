
import csv
from functools import reduce

tasks = [
    'vaske bad og do',
    'støvsuge gulv',
    'vaske gulv',
    'vaske kjøkken',
    'tørke støv'
]

people = ['sigmund', 'tora', 'bendik', 'emilie', 'magnus']

def main(**kwargs):
    wstart = kwargs.pop('week_start', 0)
    offset = int(kwargs.get('offset', 0))

    with open('out.csv', 'w', newline='') as fp:
        writer = csv.writer(fp)#, delimiter=' ', quotechar='|')
        writer.writerow(['uke', *tasks])

        for i in range(0, kwargs.get('week_end', 32) - wstart):
            writer.writerow([wstart+i, *[people[((offset + x) % len(people))] for x in range(0, len(people))]])
            offset = (offset + 1) % len(people)

if __name__ == '__main__':
    import sys

    def parse_arg(arg):
        split = arg.split('=')

        return {split[0]: split[1]}

    args = reduce(lambda x, y: {**x, **y}, map(parse_arg, sys.argv[1:]), {})
    wstart, wend = [int(x) for x in args.pop('weeks', '0-26').split('-')]

    main(
        week_start=wstart,
        week_end=wend,
        **args
    )

