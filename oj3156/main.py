"""conan"""
def main():
    """main"""
    text = input()
    shift = int(input())
    shifted_text = ''
    for i in text:
        shifted_text += chr(((ord(i) + shift - 97) % 26) + 97)
    print(shifted_text)
main()
