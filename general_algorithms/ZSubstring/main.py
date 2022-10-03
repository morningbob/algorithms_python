from ZSubstring import Z_Substring

if __name__ == '__main__':

    #z = Z_Substring('aabza', 'abzcaabzaabza')
    z = Z_Substring('caa', 'acabacaa')
    #z = Z_Substring('caa', 'caabacaaff')
    table = z.construct_z_table()

    for item in table:
        print("value", item)