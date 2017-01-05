def format_list(li):
    string = ''
    if len(li) == 1:
        return li[0]
    else:
        string = li[0]
        for item in li[1:len(li) - 2]:
            string = string + ', ' + item
        return string + ' and ' + li[len(li) - 1]
