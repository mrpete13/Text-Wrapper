import textwrap

def wrap():
    file_object = open('pi_million_digits.txt', 'r+')
    text = file_object.read()
    text = textwrap.fill(text, 80)
    wrapped = open('pi_million_digits.txt', 'w')
    wrapped.write(text)

# if __name__ == "__main__":
# wrap()
wrap()
