import sys
import getopt
import logging
import base64

config = {}

def to_str(s):
    if bytes != str:
        if type(s) == bytes:
            return s.decode('utf-8')
    return s

def print_help():
    print('''usage: pybase64 [OPTION]...
Options:
  -h, --help             show this help message and exit
  -e, --encode           encode input file to output file
  -d, --decode           decode input file to output file
  -i, --input            path to input file
  -o, --output           path to output file
''')

def get_config():
    global config
    shortopts = 'hedi:o:'
    longopts = ['help', 'encode', 'decode', 'input=', 'output=']
    try:
        optlist, args = getopt.getopt(sys.argv[1:], shortopts, longopts)
        for key, value in optlist:
            if key == '-e':
                config['cmd'] = base64.encode
            elif key == '-d':
                config['cmd'] = base64.decode
            elif key == '-i':
                config['input'] = to_str(value)
            elif key == '-o':
                config['output'] = to_str(value)
    except getopt.GetoptError as e:
        print(e, file=sys.stderr)
        print_help()
        sys.exit(2)

    if not config:
        logging.error('config not specified')
        print_help()
        sys.exit(2)

    config['cmd'] = config.get('cmd', base64.encode)
    config['input'] = config.get('input', 'input')
    config['output'] = config.get('output', config['input']+'.output')

def main():
    global config
    get_config()
    inputFile = open(config['input'], 'rb')
    outputFile = open(config['output'], 'wb')
    config['cmd'](inputFile, outputFile)
    inputFile.close
    outputFile.close

if __name__ == '__main__':
    main()
