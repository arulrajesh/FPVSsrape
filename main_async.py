from requests_html import HTML, HTMLSession
import csv


def rcmumbai(max_pages):
    csv_file = open('rcmumbai.csv','w',encoding='utf-8')
    csv_writer = csv.writer(csv_file)
    session = HTMLSession()
    page = 1 
    csv_writer.writerow(['Site','Title','Link','Price','Old Price','Availability'])

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
            price=price.text
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



            print(name)
            print(link)
            print(price)
            print(old_price)
            print(stock_status)
            print('\n')
            csv_writer.writerow(['Rcmumbai',name,link,price,old_price,stock_status])
            page+=1
            print(page)
    csv_file.close()

rcmumbai(67)