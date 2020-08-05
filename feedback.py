import wikipediaapi
from serpapi import GoogleSearchResults

class Parser:

    def __init__(self, skill):
        self.skill = skill

    def parseForCoursera(self):
        senteces = self.skill.split()
        search_key = ''
        
        for i in range(len(senteces)-1):
            search_key+=senteces[i]
            search_key+='%20'
        search_key+= senteces[i+1]

        return search_key

    def parseForUdemy(self):
        senteces = self.skill.split()
        search_key = ''
        
        for i in range(len(senteces)-1):
            search_key+=senteces[i]
            search_key+='+'
        search_key+= senteces[i+1]

        return search_key

    def parseForPuralsight(self):
        return Parser.parseForCoursera(self)

    def parseForLynda(self):
        return Parser.parseForUdemy(self)

class FeedBack:

    webSitesDictionary = {
	'Algorithms': ['www.geeksforgeeks.org'],
	'DataBase': ['www.w3schools.com'],
	'SoftWareEngineering': ['www.tutorialspoint.com', 'stackoverflow.com'],
	'DataScience': ['www.datacamp.com']
    }
    
    def __init__(self, skill, question):
        self.skill = skill
        self.question = question

    def wikipediaSearch(self):
        wiki_wiki = wikipediaapi.Wikipedia('en')
        page_py = wiki_wiki.page('Python_(programming_language)')
        print(page_py.summary)
    
    def googleSearch(self):
        print('google search')
    
    #Done
    def courseraSearch(self):
        p = Parser(self.skill)
        search_key = p.parseForCoursera()
        link = 'https://www.coursera.org/search?query=' + search_key
        print(link)

    #Done
    def udemySearch(self):
        p=Parser(self.skill)
        search_key = p.parseForUdemy()
        link = 'https://www.udemy.com/courses/search/?q=' + search_key
        print(link)
    
    #Done
    def pluralsightSearch(self):
        p=Parser(self.skill)
        search_key  = p.parseForPuralsight()
        link = 'https://www.pluralsight.com/search?q=' + search_key
        print(link)

    def lyndaSearch(self):
        p=Parser(self.skill)
        search_key  = p.parseForLynda()
        link = 'https://www.lynda.com/search?q=' + search_key
        print(link)

    def search(self):
        self.wikipediaSearch()
        self.googleSearch()
        self.courseraSearch()
        self.udemySearch()
        self.pluralsightSearch()
        self.lyndaSearch()

# p = Parser('machine learning andrew eg')
# print(p.parseForCoursera())

f = FeedBack('machine learning', 'anyquestion')
f.search()