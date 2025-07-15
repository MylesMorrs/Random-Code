import argparse

def get_args():
    parser = argparse.ArgumentParser(
        description='Jump The Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('number', metavar='str', help='Put A Damn Number')
    return parser.parse_args()

def main():
    #Dictionay to translate numbers into jump five, can code and decode
    jumper = {'1':'9','2':'8','3':'7', '4':'6', '5':'0', '9':'1', '8':'2', '7':'3', '6':'4', '0':'5'}
    args = get_args()
    print(''.join([jumper.get(char, char) for char in args.number]))

if __name__ == '__main__':
    main()
