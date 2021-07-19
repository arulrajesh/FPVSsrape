from requests_html import HTML, HTMLSession
import datetime
import csv


def rcmumbai(max_pages):
    csv_file = open('rcmumbai.csv','a',encoding='utf-8')
    csv_writer = csv.writer(csv_file)
    session = HTMLSession()
    page = 1 
    csv_writer.writerow(['Site','Title','Link','Price','Old Price','Availability','Date'])
    head = {
        "Host": "rcmumbai.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Alt-Used": "rcmumbai.com",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "1",
        "Cache-Control": "max-age=0"
    }
    while page <= max_pages:
        r = session.get(f'https://rcmumbai.com/latest?palxqb={page}')
        products= r.html.find('.product-item')
        for product in products:
            title = product.find('.product-item-details .product-item-name a', first =True)
            name = title.text
            link = title.attrs['href']
            price = product.find('.price-box .special-price .price',first =True)
            if price == None:
                price = product.find('.price-box .price',first =True)
            try:
                price=price.text
            except Exception as e:
                price='Not Available'

            old_price = product.find('.price-box .old-price .price',first =True)

            if old_price== None:
                old_price=None
            else:
                old_price=old_price.text

            stock_status = product.find('.product-item-details .product-item-actions .actions-primary .stock.unavailable',first = True)
            if stock_status == None:
                stock_status = 'Available'
            else:
                stock_status = stock_status.text
            csv_writer.writerow(['Rcmumbai',name,link,price,old_price,stock_status,datetime.datetime.now()])
        print(f'page: {page} scrape complete')
        page+=1
        
    csv_file.close()

rcmumbai(3)