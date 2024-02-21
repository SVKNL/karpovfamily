from icrawler.builtin import GoogleImageCrawler




def get_image(word):
    
    num=1
    google=GoogleImageCrawler(storage={'root_dir':'/Users/admin/karpovfamily/everythingatonce/media/images'})
    google.crawl(keyword=word, max_num=num)