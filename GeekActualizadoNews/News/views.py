from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import requests
from bs4 import BeautifulSoup
from heapq import merge

def Medium():
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
                dic_Story['title'] = div.find('h3').string
                a_img = div.find('a',attrs={'class':'u-block'})            
                img = a_img['style']
                url_img = img.replace('background-image: url(\"','').replace('\"); background-position: 50% 50% !important;','').replace('\"); background-repeat: repeat;','')
                dic_Story['img'] = url_img
                dic_Story['res'] = div.find('h4').string
                dic_Story['time'] = div.find('time').string
                dic_Story['autor'] = div.find('a',attrs={'class':'link u-textColorDarker u-fontSize12 u-baseColor--link'}).string                
                dic_Story['img_page'] = "https://cdn.app.compendium.com/uploads/user/e7c690e8-6ff9-102a-ac6d-e4aebca50425/0eb8e772-8880-46b2-98ee-257cf9c2fa2c/File/d3a660af8932f6bd201f17bc6ce993c5/gjbzh1ue.jpg"
                dic_Story['page'] = "https://medium.com/"
                list_Top_Stories.append(dic_Story)                
    except:
            pass
    return list_Top_Stories

def Xataka():
    try:
        req = requests.get("https://xataka.com/")
        soup = BeautifulSoup(req.text,'html.parser')
        #print(soup.prettify())
        div_Top_Stories = soup.find('div',attrs={'class':'section-hero', })         
        list_Top_Stories = []              
        div_Top_Story = div_Top_Stories.find_all('article',attrs={'class':'hero-poster'})        
        #print(div_Top_Story) 
        for div in div_Top_Story:           
            print(div)
            dic_Story = {} 
            dic_Story['href'] = "https://www.xataka.com/"+div.find('a')['href']                        
            dic_Story['title'] = div.find('div',attrs={'class':'poster-figure'}).find('img')['alt']
            dic_Story['img'] = div.find('div',attrs={'class':'poster-figure'}).find('img')['src']
            dic_Story['img_page'] = "https://www.gravatar.com/avatar/46c418f19105a71eb554a1aa6835ee43?s=300&d=mm&r=g"            
            dic_Story['page'] = "https://xataka.com/"
            try:
                dic_Story['res'] = div.find('div',attrs={'class':'poster-summary'}).find('p').string        
            except:
                pass
            
            list_Top_Stories.append(dic_Story)              
    except:
            pass
    return list_Top_Stories

def News(request,json=0):
    list_Top_Stories = []
    list_Top_Stories.extend(Medium())
    list_Top_Stories.extend(Xataka())
    print(list_Top_Stories)
    if json == 1:
        dict_json = {                    
                    'results':list_Top_Stories}
                    
        return JsonResponse(dict_json)
    else:
        return render(request,'article.html',{                    
                    'articles': list_Top_Stories
            })

def Newsjson(request):
    return News(request,json=1)
