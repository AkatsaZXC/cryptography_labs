def lookup_table(block_count_in, *key_params):
    i = 0
    while i <= block_count_in:
        for j in key_params:
            print((2 * int(key_params[j])) ** i, "\t")
            i += 1


def main():
    block_count = int(input("Enter count of blocks:"))
    print("Enter keys")
    key_list = input().split()
    print(*key_list)

    lookup_table(block_count, *key_list)


main()
