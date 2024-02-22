from icrawler.builtin import GoogleImageCrawler
import os



def get_image(word):
    if os.path.exists('/Users/admin/karpovfamily/everythingatonce/media/images/000001.jpg'):
            os.remove('/Users/admin/karpovfamily/everythingatonce/media/images/000001.jpg')
    if os.path.exists('/Users/admin/karpovfamily/everythingatonce/media/images/000001.png'):
            os.remove('/Users/admin/karpovfamily/everythingatonce/media/images/000001.png')        
    
    num=1
    google=GoogleImageCrawler(storage={'root_dir':'/Users/admin/karpovfamily/everythingatonce/media/images'})
    google.crawl(keyword=word, max_num=num)
    if os.path.exists('/Users/admin/karpovfamily/everythingatonce/media/images/000001.png'):
        return 'png'
    if os.path.exists('/Users/admin/karpovfamily/everythingatonce/media/images/000001.jpg'):
        return 'jpg'