def page_list(page,count):
    pageList = []
    if count <= 7:
        x = 0
        while x < 6:
            if count >= x + 3:
                pageList.append(x + 2)
            else:
                pageList.append(-1)
            x = x + 1
    elif page < 7:
        pageList = [2, 3, 4, 5, 6, 0]
    elif page > count - 6:
        pageList = [0, count - 5, count - 4, count - 3, count - 2, count - 1]
    else:
        pageList = [0, page - 2, page - 1, page, page + 1, 0]
    return pageList