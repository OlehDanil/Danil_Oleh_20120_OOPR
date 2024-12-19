# list_integer_project/__main__.py

from list_integer_project.list_integer import ListInteger

def main():
    s = ListInteger((1, 2, 3))
    s[1] = 10
    s.append(11)
    print(s)
    try:
        s[0] = 10.5  # Ожидается TypeError
    except TypeError as e:
        print(e)

if __name__ == "__main__":
    main()
