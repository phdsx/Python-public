import sys
scripts,encoding,errors=sys.argv

def main(language_file,encoding,errors):
    line=language_file.readline()
    if line:
        print_line(line,encoding,errors)
        return main(language_file,encoding,errors)

def print_line(line,encoding,errors):
    next_lang=line.strip()
    raw_betys=next_lang.encode(encoding,errors=errors)
    cooked_string=raw_betys.decode(encoding,errors=errors)

    print(raw_betys,"<------>",cooked_string)

languages=open("languages.txt",encoding="utf-8")

if __name__ == '__main__':
    main(languages,encoding,errors)
    t=input("kkkk")