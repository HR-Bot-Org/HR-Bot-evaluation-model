import wikipediaapi
from googlesearch import search
# from flask import render_template

class Parser:

    def __init__(self, skills):
        self.skills = skills

    def parse(self, sign):
        sentences = []
        for skill in self.skills:
            sentences.append(skill['name'].split())
        
        search_keys = []
        search_key = ''

        for sentence in sentences:
            for i in range(len(sentences)-1):
                search_key += sentence[i]
                search_key += sign
            search_key += sentence[-1]
            search_keys.append(search_key)
            search_key = ''

        return search_keys

class FeedBack:
    
    def __init__(self, data):
        self.skills = data['skills']
        self.question = data['question']
        self.token = data['token']

        

    #Done
    def wikipediaSearch(self):
        result = ''
        wiki_wiki = wikipediaapi.Wikipedia('en')
        page_question = wiki_wiki.page(self.question)
        skills = self.skills
        
        for skill in skills:
            x = wiki_wiki.page(skill['name'])
            result +=x.summary
            result +='\n'

        return page_question.summary + '\n' + result
    
    #Done
    def googleSearch(self):
        skills = self.skills
        question = self.question
        result = ''

        for skill in skills:
            query = 'site:' + skill['site'] + ' ' + question + ' + ' + skill['name']
            for j in search(query, tld="com", num=10, stop=1, pause=2): 
                result +=str(j) 

        return result

    #Done
    def courseraSearch(self):
        p = Parser(self.skills)
        search_keys = p.parse('%20')
        links = []
        result = ''
        for search_key in search_keys:
            link = 'https://www.coursera.org/search?query=' + search_key
            links.append(link)
        
        for link in links :
            result+=link ; result+='\n'

        return result

    #Done
    def udemySearch(self):
        p = Parser(self.skills)
        search_keys = p.parse('+')
        links = []
        result = ''
        for search_key in search_keys:
            link = 'https://www.udemy.com/courses/search/?q=' + search_key
            links.append(link)
        
        for link in links :
            result+=link ; result+='\n'

        return result
    
    #Done
    def pluralsightSearch(self):
        p = Parser(self.skills)
        search_keys = p.parse('%20')
        links = []
        result = ''
        for search_key in search_keys:
            link = 'https://www.pluralsight.com/search?q=' + search_key
            links.append(link)
        
        for link in links :
            result+=link ; result+='\n'

        return result

    #Done
    def lyndaSearch(self):
        p = Parser(self.skills)
        search_keys = p.parse('%20')
        links = []
        result = ''
        for search_key in search_keys:
            link = 'https://www.lynda.com/search?q=' + search_key
            links.append(link)
        
        for link in links :
            result+=link ; result+='\n'

        return result

    def search(self):
        token = self.token 
        if token == "hr_bot_2019_2020":    
            result = ''
            result += self.wikipediaSearch() ; result+= '\n'
            result += self.googleSearch() ; result+= '\n'
            result += self.courseraSearch() ; result+= '\n'
            result += self.udemySearch() ; result+= '\n'
            result += self.pluralsightSearch() ; result+= '\n'
            result += self.lyndaSearch() ; result+= '\n'
            
            return result

        else:
            return None

# p = Parser('machine learning andrew eg')
# print(    p.parseForCoursera())
if __name__ == "__main__":
    pass