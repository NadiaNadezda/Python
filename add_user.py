def add_user(username = None):
    if username == None:
        with open('database.txt', 'r') as database:
            for element in database:
                print(element)
    else:
        with open('database.txt', 'a') as database:
            database.write(str(username + '\n'))

def main():
    add_user('nana')
    add_user()
    add_user('petey')
    add_user('karen')
    add_user('ayaya')
    add_user()

if __name__ == '__main__':
    main()