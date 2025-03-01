import urllib3
from bs4 import BeautifulSoup

def spider(name,url, found_titles, found):
    try:
        page = urllib3.urlopen(url)
        soup = BeautifulSoup(page,'html.parser')

        title = soup.title.string.lower()
        keywords = soup.select('meta[name="keywords"]')[0]['content'].lower().split(', ')

        if name in keywords:
            keywords.remove(name)
        
        cleaned_keywords = []
        for k in keywords:
            if k in title:
                cleaned_keywords.append(k)
        
        if len(cleaned_keywords) > 0 and title not in found_titles:
            found_titles.append(title)

            print (title)
            print (cleaned_keywords)
            print

            f=open('keyword_data.txt','a')
            f.write(
                title + "\t" + ' '.join(
                    k.replace(' ','_') for k in cleaned_keywords
                ) + "\n"
            )
            f.close()

        for a in soup.select('a[href]'):
            b = a['href'].replace('#replies', '')
            if 'https://' + name +'.com' in b and b not in found:
                found.append(b)
                spider(name, b, found_titles, found)
    
    except UnicodeEncodeError:
        pass
    #except urllib3.HTTPError:
        #pass
    except ValueError:
        pass
    except IndexError:
        pass
    #except urllib3.URLError:
        #pass
    except:
        pass
    

def main():
    name     = 'lifehacker'
    start_url = "https://lifehacker.com/im-doordash-ceo-tony-xu-and-this-is-how-i-work-1821196705"
    spider(name, start_url, [], [start_url])

if __name__ == "__main__":
    main()