import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.ligamagic.com/')
except urllib.error.URLError:
    print('o site da Ligamagic não está acessível no momento.')
else:
    print('Acesso ao site da ligamagic está OK!')
    #print(site.read())
