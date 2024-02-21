from icrawler.builtin import GoogleImageCrawler




def get_image(word):
    if os.path.exists('/Users/admin/karpovfamily/everythingatonce/media/images/000001.jpg'):
            os.remove('/Users/admin/karpovfamily/everythingatonce/media/images/000001.jpg')
    num=1
    google=GoogleImageCrawler(storage={'root_dir':'/Users/admin/karpovfamily/everythingatonce/media/images'})
    google.crawl(keyword=word, max_num=num)