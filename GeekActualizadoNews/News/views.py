from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import requests
from bs4 import BeautifulSoup


def News(request,json=0):
    try:
        req = requests.get("https://medium.com/")
        soup = BeautifulSoup(req.text,'html.parser')
        #print(soup.prettify())
        div_Top_Stories = soup.find('div',attrs={'class':'streamItem streamItem--section js-streamItem'})
        #print(div_Top_Stories.prettify())
        list_Top_Stories = []
        for Top_Stories in div_Top_Stories:
            div_Top_Story = Top_Stories.find_all('div',attrs={'class':'u-flex u-sizeFullWidth u-height260 u-sm-flexWrap u-xs-heightAuto u-borderBox u-marginBottom20 u-backgroundColorWhite u-overflowHidden u-relative u-borderRadius2 u-borderBlackLightest'})
            #print(div_Top_Story)
            dic_Story = {}
            for div in div_Top_Story:
                dic_Story = {}
                dic_Story['href'] = div.find('a')['href']
                title = div.find('h3').string
                print(title)
                dic_Story['title'] = title
                a_img = div.find('a',attrs={'class':'u-block'})            
                img = a_img['style']
                url_img = img.replace('background-image: url(\"','').replace('\"); background-position: 50% 50% !important;','').replace('\"); background-repeat: repeat;','')
                dic_Story['img'] = url_img
                list_Top_Stories.append(dic_Story)

            '''
            dic_games = {}
            #############################################################
            title = games.find('a',attrs={'class':'title-5'})
            dic_games['title']  = title.string
            #############################################################
            if games.find('span',attrs={'class':'price_sale'}):
                price = games.find('span',attrs={'class':'price_sale'})
                dic_games['price']  = price.string
            elif games.find('span',attrs={'class':'price'}):
                price = games.find('span',attrs={'class':'price'})
                dic_games['price']  = price.string.replace('\n','').replace('  ','')
            else:
                price = "Not found"
                dic_games['price']  = "Not found"
            #############################################################
            img = games.find('img',attrs={'class':'image-fly img-responsive'})['src']
            dic_games['img']  = img
            #############################################################
            url = games.find('a',attrs={'class':'hoverBorder'})
            dic_games['url']  = "https://www.gamershop.com.mx"+url['href']
            #############################################################
            list_games.append(dic_games) 
            
        #############################################################
        if soup.find('div',attrs={'class':'total-item-number'}):
            total_games = int(soup.find('div',attrs={'class':'total-item-number'}).string.replace(' ITEMS ',''))
        else:
            total_games = "Not found"
        #############################################################
        pages = []
        if soup.find('ul',attrs={'class':'top-paginate'}):
            ul_total_pages = soup.find('ul',attrs={'class':'top-paginate'})                
            for li in ul_total_pages:
                try: 
                    pages.append(int(li.string))
                except ValueError:
                    pass                    
            total_pages = max(pages)
        else:
            total_pages = "Not found"
        #############################################################
        '''
        if json == 1:
            dict_json = {
                        #'page':int(page),
                        'results':list_Top_Stories}
                        
            return JsonResponse(dict_json)
        else:
            return render(request,'objetos/games.html',{
                        'title': 'PlayStation 4',
                        'console': 'playstation',
                        'page':int(page),
                        'pagination':pages,
                        'games': list_games
            })
    except UnboundLocalError:
            return render(request,'objetos/games.html', {'error': '404 Not Found'})

def Newsjson(request):
    return News(request,json=1)
