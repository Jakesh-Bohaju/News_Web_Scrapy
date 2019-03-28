from django.shortcuts import render

# Create your views here.
import requests as req
from bs4 import BeautifulSoup
from django.views import View

from Scrapy.models import NewsScrapy
from datetime import date


class Index(View):
    def get(self, request):
        newsscrapy = NewsScrapy()
        homepage_request = req.get('http://www.nepalihealth.com/')
        homepage_parsed = BeautifulSoup(homepage_request.content, "html.parser")
        # print(homepage_request.text)

        a_tags = homepage_parsed.find_all('a')
        links = set()

        # get present os date and convert into yyyy-mm-dd format
        today = str(date.today())
        year = today[0:4]
        month = today[5:7]
        day = today[8:10]
        print(year, month, day)
        present_date = year + '-' + month + '-' + day
        print(present_date)


        # a_tags is list of dictionary form
        for a_tag in a_tags:
            # print(a_tag.get('href'))
            # link = a_tag.get('href', '')
            if '/' + year + '/' + month + '/' + day + '/' in a_tag.get('href', ''):
                # print("link success")
                links.add(a_tag.get('href'))
                # links.add(link)

        for link in links:
            newsscrapy = NewsScrapy()
            single_news_request = req.get(link)
            # print(single_news_request.text)
            single_news_parsed = BeautifulSoup(single_news_request.content, "html.parser")

            title = single_news_parsed.find('h1').text
            print(title)
            if not Blog.title == title and Blog.blogdate == present_date:
                nc = single_news_parsed.find('div', {'class': 'entry-content'})
                ppp = nc.find_all('p')
                image = nc.find_all('img')
                a = []
                for innn in image:
                    a.append(innn['src'])
                a = a[1:2]
                # print(a)
                a = '\n'.join(a)
                # print(a)

                lists = []
                for i in ppp:
                    news = i.text
                    # print(news)
                    lists.append(news)
                lists = '\n'.join(lists)
                # print(lists)

                newsscrapy.title = title
                newsscrapy.image = a
                newsscrapy.news = lists
                newsscrapy.save()
                print("=========================New post============================================================")

        template_content = {
            'scraps': NewsScrapy.objects.all()
        }
        return render(request, 'index.html', template_content)
