from handeler import WebSiteLine


def main():
    web = WebSiteLine('https://niazmandiha.co/ads/بهترین-مرکز-دوره-آموزشی-ماساژور-پولسا/')
    list_appended = list()
    for a in list(web.website.find_source(class_name='row contact-box')):
        ss = str(a).replace('\n', '')
        list_appended.append(ss)
    list_appended2 = list()
    ss = list_appended[7]
    for i in str(ss).split('                  '):
        list_appended2.append(i)
    print(list_appended2[12][105:-12])
    print(list_appended2[14][105:-100])


if __name__ == '__main__':
    print(main())
