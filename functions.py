def python_foo():
    width = 80
    text = "spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def center_text(*args, sep=' '):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    return " " * left_margin +  text

#
# with open("centered", mode='w') as centered_file:


print(center_text(12))
print(center_text("spam and eggs"))
print(center_text("spam, spam and eggs"))
print(center_text("spam, spam, spam and eggs"))
print(center_text("first", "second", "third", "fourth", "spam", sep=":"))
