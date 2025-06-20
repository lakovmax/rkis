def func(string_list):

    result = [s for s in string_list if s.startswith("http://")]
    return result

lst = ["http://metanit.com", "https://google.com", "https://moodle.tomtit-tomsk.ru"]
filtered_list = func(lst)
print(filtered_list)