import sys

from . import demo

# TODO: only use __main__.py if your package is a CLI tool


def main():
    arg = ' '.join(sys.argv[1:])
    if not arg:
        print('Got nothing to say?')
    else:
        print(demo.echo(arg))


if __name__ == '__main__':
    main()
