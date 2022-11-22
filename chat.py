#能讀取input檔，產生一個檔案output
#我對轉換為清單的格式比較不直覺。其實最後轉為清單後再一條條寫出也有一樣的效果
#老師講解的架構為: 讀取->檔案存在清單中->轉換->轉換後也在另一個清單->寫出

#讀取對話檔案
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return(lines)

#轉換檔案
def convert(lines):
    new = []
    person = None
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person:
            new.append(person + ': ' + line)
    return new

def write_file(filename, lines):
    with open(filename, 'w', encoding = 'utf-8') as f:
        for line in lines:
            f.write(line + '\n')


def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt', lines)

main()