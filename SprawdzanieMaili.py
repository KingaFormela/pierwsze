"""Skrypt służy do sprawdzenia, czy podany mail jest prawdziwy - sprawdza czy login użytkownika na konkretnej domenie jest wolny, czy zajęty."""
__author__ = "Kinga Formela"
__email__ = "kinga.formela@gmail.com"
from selenium import webdriver
import time
import smtplib
from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import NoSuchElementException
import datetime
# from selenium.webdriver.support.select import Select
# from random import *

'''driver = webdriver.Chrome(executable_path=r'C:\TestFiles\chromedriver.exe')
driver.get ('https://poczta.nazwa.pl/')
login = driver.find_element_by_name('login').send_keys('umowa@crossfinance.pl')
haslo = driver.find_element_by_name('password').send_keys('hRNDOmK2ajswEti'+ Keys.TAB + Keys.TAB + Keys.ENTER)
time.sleep(5)
body = driver.find_element_by_id('body').send_keys("desceds" + Keys.TAB + Keys.TAB + Keys.TAB + Keys.TAB + Keys.TAB + Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER)
body.send_keys("dcvcd")'''

print('wprowadz adres email do sprawdzenia')                    # pobranie od użytkownika maila i rozdzielenie loginu i domeny
mail = input()
(user, domena, ) = mail.split("@", 1)
print(user)
print(domena)

now = datetime.datetime.now()                                                               # komunikaty, które mogą się pojawić w mailu
komunikat1 = f"""\
Subject: Sprawdzenie maila {mail}
{now}  mail istnieje"""
komunikat2 = f"""\
Subject: Sprawdzenie maila {mail}
{now}  mail nie istnieje"""

server = smtplib.SMTP('smtp.gmail.com', 587)                    # połączenie z serwerem maila
server.starttls()
server.login("newtestserver1", "EWQewq321!")

# GMAIL - *DONE*
if domena == 'gmail.com':
    driver = webdriver.Chrome(executable_path=r'C:\TestFiles\chromedriver.exe')
    driver.get('https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp')
   # driver.minimize_window()
    imie = driver.find_element_by_class_name('whsOnd').send_keys('kinga' + Keys.TAB + 'formela' + Keys.TAB + user + Keys.TAB + "lewdsl345434" + Keys.TAB + "lewdsl345434" + Keys.TAB + "lewdsl345434" + Keys.ENTER)
    time.sleep(2)

    if driver.find_elements_by_class_name('uBOgn'):
        print(komunikat1)
        server.sendmail("newtestserver1", "kinga.formela@gmail.com", komunikat1)
    else:
        print(komunikat2)
        server.sendmail("newtestserver1", "kinga.formela@gmail.com", komunikat2)
    #zamknij = driver.__exit__()

# WP do poprawienia
if domena == 'wp.pl':
    driver = webdriver.Chrome(executable_path=r'C:\TestFiles\chromedriver.exe')
    driver.get('https://nowyprofil.wp.pl/rejestracja/')
    nazwa_uzytk = driver.find_element_by_class_name('sc-bZQynM').send_keys(Keys.TAB +Keys.TAB +Keys.TAB+ Keys.TAB+ Keys.TAB+Keys.TAB+Keys.TAB+Keys.TAB +user)
    time.sleep(3)

    if driver.find_elements_by_class_name('invalid'):
        print(komunikat1)
        server.sendmail("newtestserver1", "kinga.formela@gmail.com", komunikat1)
    else:
        print(komunikat2)
        server.sendmail("newtestserver1", "kinga.formela@gmail.com", komunikat2)

# OUTLOOK - *DONE*
if domena == 'outlook.com':
    driver = webdriver.Chrome(executable_path=r'C:\TestFiles\chromedriver.exe')
    driver.get('https://signup.live.com/signup?lcid=1033&wa=wsignin1.0&rpsnv=13&ct=1557410579&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26signup%3d1%26RpsCsrfState%3d59e41303-39e7-5d14-6b29-22bc0768a552&id=292841&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&lic=1&uaid=3d00ba6b08ac47519e17522b17916746')
    MemberName = driver.find_element_by_name("MemberName").send_keys(user)
    dalej = driver.find_element_by_id("iSignupAction").click()
    time.sleep(3)

    if driver.find_elements_by_link_text('zaloguj się'):
        print(komunikat1)
        server.sendmail("newtestserver1", "kinga.formela@gmail.com", komunikat1)
    else:
        print(komunikat2)
        server.sendmail("newtestserver1", "kinga.formela@gmail.com", komunikat2)

# HOTMAIL - do poprawienia
if domena == 'hotmail.com':
    driver = webdriver.Chrome(executable_path=r'C:\TestFiles\chromedriver.exe')
    driver.get('https://signup.live.com/signup?lcid=1033&wa=wsignin1.0&rpsnv=13&ct=1557410579&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26signup%3d1%26RpsCsrfState%3d59e41303-39e7-5d14-6b29-22bc0768a552&id=292841&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&lic=1&uaid=3d00ba6b08ac47519e17522b17916746')
    MemberName = driver.find_element_by_name("MemberName").send_keys(user + Keys.TAB)
    ktora_skrzynka = driver.find_element_by_name("LiveDomainBoxList").send_keys('@hotmail.com')
    dalej = driver.find_element_by_id("iSignupAction").click()
    time.sleep(3)

    if driver.find_elements_by_link_text('zaloguj się'):
        print(mail+": mail już istnieje")
    else:
        print(mail+": mail nie istnieje")
# O2 - do poprawienia
if domena == 'o2.pl':
    driver = webdriver.Chrome(executable_path=r'C:\TestFiles\chromedriver.exe')
    driver.get('https://poczta.o2.pl/rejestracja/')
    MemberName = driver.find_element_by_class_name("sc-bZQynM").send_keys(Keys.TAB +Keys.TAB +Keys.TAB+ Keys.TAB+ Keys.TAB+Keys.TAB+Keys.TAB+Keys.TAB +user)
    dalej = driver.find_element_by_class_name("sc-kEYyzF").click()
    mailvalid = driver.find_element_by_id('2b39f139')
    is_invalid = "invalid" in mailvalid.get_attribute("class")
    print(is_invalid)
    time.sleep(3)

    if driver.find_elements_by_id('2b39f139-c632-fe4a-5fe7-314ec1977bde'):
        is_invalid = "invalid" in target_element.get_attribute("class")
        print(komunikat1)
        server.sendmail("newtestserver1", "kinga.formela@gmail.com", komunikat1)

    else:
        print(komunikat2)
    server.sendmail("newtestserver1", "kinga.formela@gmail.com", komunikat2)

# ONET (onet.pl, op.pl, adres.pl, vp.pl, onet.eu, cyberia.pl, pseudonim.pl, autograf.pl, opoczta.pl, spoko.pl, buziaczek.pl) - do poprawienia
if domena == 'onet.pl':
    driver = webdriver.Chrome(executable_path=r'C:\TestFiles\chromedriver.exe')
    driver.get('https://konto.onet.pl/register-email.html?app_id=poczta.onet.pl.front.onetapi.pl')
    nazwa_uzytk = driver.find_element_by_id('login_user').send_keys(mail)
    sprawdz = driver.find_element_by_name("checkLogin")
    time.sleep(3)
    #tu do napisania skrypt, który odczyta listę HTML-ową i sprawdzi na niej możliwości

    if driver.find_elements_by_class_name('invalid'):
        print(komunikat1)
        server.sendmail("newtestserver1", "kinga.formela@gmail.com", komunikat1)
    else:
        print(komunikat2)
        server.sendmail("newtestserver1", "kinga.formela@gmail.com", komunikat2)

# INTERIA, POCZTA.FM, INTERIA.EU, INTMAIL.COM, INTERIA.COM, ADRESIK.NET, INTERIOWY.PL, PISZ.TO, VIP.INTERIA.PL, PACZ.TO, OGARNIJ.SE
if domena == 'interia.pl':
    driver = webdriver.Chrome(executable_path=r'C:\TestFiles\chromedriver.exe')
    driver.get('https://konto-pocztowe.interia.pl/#/nowe-konto')
    nazwa_uzytk = driver.find_element_by_class_name('sc-bZQynM').send_keys(Keys.TAB +Keys.TAB +Keys.TAB+ Keys.TAB+ Keys.TAB+Keys.TAB+Keys.TAB+Keys.TAB +user)
    time.sleep(3)

    if driver.find_elements_by_class_name('invalid'):
        print(komunikat1)
        server.sendmail("newtestserver1", "kinga.formela@gmail.com", komunikat1)
    else:
        print(komunikat2)
        server.sendmail("newtestserver1", "kinga.formela@gmail.com", komunikat2)

# LIVE.COM - do dokończenia
if domena == 'live.com':
    driver = webdriver.Chrome(executable_path=r'C:\TestFiles\chromedriver.exe')
    driver.get('https://nowyprofil.wp.pl/rejestracja/')
    nazwa_uzytk = driver.find_element_by_class_name('sc-bZQynM').send_keys(Keys.TAB +Keys.TAB +Keys.TAB+ Keys.TAB+ Keys.TAB+Keys.TAB+Keys.TAB+Keys.TAB +user)
    time.sleep(3)

    if driver.find_elements_by_class_name('invalid'):
        print(komunikat1)
        server.sendmail("newtestserver1", "kinga.formela@gmail.com", komunikat1)
    else:
        print(komunikat2)
        server.sendmail("newtestserver1", "kinga.formela@gmail.com", komunikat2)

# ICLOUD.COM - do dokończenia - tutaj trzeba podać imię i nazwisko, żeby dokonać sprawdzenia
if domena == 'icloud.com':
    driver = webdriver.Chrome(executable_path=r'C:\TestFiles\chromedriver.exe')
    driver.get('https://iforgot.apple.com/appleid#!&section=appleid')
    nazwa_uzytk = driver.find_element_by_class_name('generic-input-field').send_keys('Kinga' + Keys.TAB + "Formela" + Keys.TAB + mail)
    kontynuuj = driver.find_element_by_class_name('right-nav').click()
    time.sleep(3)

    if driver.find_elements_by_class_name('has-errors'):
        print(komunikat1)
        server.sendmail("newtestserver1", "kinga.formela@gmail.com", komunikat1)
    else:
        print(komunikat2)
        server.sendmail("newtestserver1", "kinga.formela@gmail.com", komunikat2)

# GAZETA.PL - do dokończenia - obsługa wyjątków
if domena == 'gazeta.pl':
    driver = webdriver.Chrome(executable_path=r'C:\TestFiles\chromedriver.exe')
    driver.get('https://konto.gazeta.pl/konto/szybka-rejestracja.do')
    nazwa_uzytk = driver.find_element_by_name('login').send_keys(user + Keys.TAB + "gbvfrdfewdsf")
    time.sleep(3)

    if driver.find_element_by_class_name('error'):
        print(komunikat1)
        server.sendmail("newtestserver1", "kinga.formela@gmail.com", komunikat1)
    else:
        print(komunikat2)
        server.sendmail("newtestserver1", "kinga.formela@gmail.com", komunikat2)

# YAHOO.COM - *DONE*
if domena == 'yahoo.com':
    driver = webdriver.Chrome(executable_path=r'C:\TestFiles\chromedriver.exe')
    driver.get('https://login.yahoo.com/account/create?lang=&done=https%3A%2F%2Fmail.yahoo.com%2F%3F.lang%3Dpl-PL%26guce_referrer%3DaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8%26guce_referrer_sig%3DAQAAADaeZgC5Y1a0AZS6iMQ3gjxDjgKvXSXpGWXvyq3wH9ujNkCKgZZe2cKZ8NKCkbHAliSxz3w5sVl3ahXkMJOh-Gs9Fc1umJAvsjGTOh-lY-nbfd5J1_yYvqVuY0esZJZQjhA2sp4qOpScH_hdbj5fbKM8JrzDFvML64ztkJwYiCZu&src=ym&specId=yidReg')
    nazwa_uzytk = driver.find_element_by_name('yid').send_keys(user + Keys.TAB)
    time.sleep(3)

    if driver.find_elements_by_class_name('oneid-error-border'):
        print(komunikat1)
        server.sendmail("newtestserver1", "kinga.formela@gmail.com", komunikat1)
    else:
        print(komunikat2)
        server.sendmail("newtestserver1", "kinga.formela@gmail.com", komunikat2)
elif domena != 'gmail.com' and 'wp.pl' and 'onet.pl':
    print('domena nie została oprogramowana')

