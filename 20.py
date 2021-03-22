cs116 = ["@507::empty in Q1/Q2::can list be empty::yes",
         "@1::CS116 W2015::Welcome to first post::Thanks!",
         "@19::Allowable functions::empty?, first, rest::"]
def search_piazza(post,keyword):
    result = []
    for i in post:
        if i.find(keyword) > 0:
            result.append(int(i[1 : i.find(':')]))
    return result
print(search_piazza(cs116,'empty'))
print(search_piazza(cs116,'Welcome'))
print(search_piazza(cs116,'First'))
print(search_piazza(cs116,'1'))