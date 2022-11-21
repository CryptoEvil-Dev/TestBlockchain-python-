import json
import hashlib
import os
import time


def Last_Block():
    files = os.listdir('Blockchain/')
    files = sorted([int(i) for i in files])

    last_file = files[-1]
    return last_file

def Show_Blocks():
    files = os.listdir('Blockchain/')
    files = sorted([int(i) for i in files])

    return files


def get_hash(block):
    file = open('Blockchain/' + str(block), 'rb').read()
    return hashlib.md5(file).hexdigest()

def Hash_Block():
    lb = Last_Block()
    file = open('Blockchain/' + str(lb), 'rb').read()

    return hashlib.md5(file).hexdigest()


def Add_Block(b_from, b_amount, b_to, b_hash=Hash_Block()):
    block = {
        "FROM": b_from,
        "AMOUNT": b_amount,
        "TO": b_to,
        "HASH": b_hash,
        "DATE": time.strftime("%d-%m-%Y %H:%M")
    }
    lb = Last_Block()
    with open('Blockchain/' + str(lb + 1), 'w') as write_file:
        json.dump(block, write_file, indent=4)






def Check_Blocks():
    files = Show_Blocks()
    results = []

    for file in files[1:]:
        f = open('Blockchain/' + str(file))
        h = json.load(f)['HASH']

        prev_file = str(file - 1)
        actual_hash = get_hash(prev_file)

        if h == actual_hash:
            res = 'Ok'
        else:
            res = 'Corrupted'

        results.append({'Block': prev_file, 'result': res})
        f.close()
    return results





def main():
    Add_Block('DNDSCAN', 100, 'DNDSCAN')
    print(Check_Blocks())


if __name__ == '__main__':
    main()