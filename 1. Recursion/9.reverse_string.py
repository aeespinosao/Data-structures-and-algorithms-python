def reverse(strng):
    if len(strng) == 1:
        return strng[0]
    return reverse(strng[1:]) + strng[0]

if __name__ == "__main__":
    print(reverse('python')) # 'nohtyp'
    print(reverse('appmillers')) # 'srellimppa'