def lookup_function(keys):
    for i in keys:
        print((i * 2) ** 1, "\n")




def main():
    print("Input keys and press enter to see the list: ")
    key = int(input('-->'))
    keys_list = []
    while True:
        try:
            keys_list.append(key)
            key = int(input('-->'))
        except:
            break

    lookup_function(keys_list)


main()
