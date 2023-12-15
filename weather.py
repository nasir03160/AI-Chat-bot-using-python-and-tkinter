# pip install requests-html
#pip install lxml
#user_agent 
#Asharaib user agent apna use karna 
from nturl2path import url2pathname
from requests_html import HTMLSession
import speech_to_text

s=HTMLSession()
query= "Karachi"
#r=s.get(#url, headers="{User_agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36}")
url="https://www.google.com/search?q=weather+karachi&rlz=1C1SQJL_enPK1045PK1045&oq=weather+karachi&gs_lcrp=EgZjaHJvbWUqCggAEAAYsQMYgAQyCggAEAAYsQMYgAQyCggBEAAYsQMYgAQyBwgCEAAYgAQyBwgDEAAYgAQyBwgEEAAYgAQyBwgFEAAYgAQyBwgGEAAYgAQyBwgHEAAYgAQyBwgIEAAYgAQyBwgJEAAYgATSAQgyOTg5ajFqN6gCALACAA&sourceid=chrome&ie=UTF-8+ {query}"
