import wikipediaapi
from googlesearch import search
# from flask import render_template

class Parser:

    def __init__(self, skill):
        self.skill = skill

    def parse(self, sign):
        
        sentence = self.skill.split()
        search_key = ''
        for i in range(len(sentence)-1):
            search_key += sentence[i]
            search_key += sign
        # print(sentence[-1])    
        search_key += sentence[-1]

        return search_key

class FeedBack:
    
    def __init__(self, skills):
        self.skills = skills

        

    #Done
    def wikipediaSearch(self, skill):
        wiki_wiki = wikipediaapi.Wikipedia('en')
        temp = wiki_wiki.page(skill)
        summary = temp.summary
        
        return summary
    
    #Done
    def googleSearch(self):
        skills = self.skills
        question = self.question
        result = []

        for skill in skills:
            query = question + ' + ' + skill['name']
            for j in search(query, tld="com", num=10, stop=1, pause=2): 
                result.append(str(j)) 

        return result

    #Done
    def courseraSearch(self, skill):
        p = Parser(skill)
        search_key = p.parse('%20')
        link = 'https://www.coursera.org/search?query=' + search_key
        # links = []
        # result = []
        # for search_key in search_keys:
        #     link = 'https://www.coursera.org/search?query=' + search_key
        #     links.append(link)
        
        # for link in links :
        #     result.append(link)

        return link

    #Done
    def udemySearch(self, skill):
        p = Parser(skill)
        search_key = p.parse('+')
        link = 'https://www.udemy.com/courses/search/?q=' + search_key
        # links = []
        # result = []
        # for search_key in search_keys:
        #     link = 'https://www.udemy.com/courses/search/?q=' + search_key
        #     links.append(link)
        
        # for link in links :
        #     result.append(link)

        return link
    
    #Done
    def pluralsightSearch(self, skill):
        p = Parser(skill)
        search_key = p.parse('%20')
        link = 'https://www.pluralsight.com/search?q=' + search_key
        # links = []
        # result = []
        # for search_key in search_keys:
        #     link = 'https://www.pluralsight.com/search?q=' + search_key
        #     links.append(link)
        
        # for link in links :
        #     result.append(link)

        return link

    #Done
    def lyndaSearch(self, skill):
        p = Parser(skill)
        search_key = p.parse('%20')
        link = 'https://www.lynda.com/search?q=' + search_key
        # links = []
        # result = []
        # for search_key in search_keys:
        #     link = 'https://www.lynda.com/search?q=' + search_key
        #     links.append(link)
        
        # for link in links :
        #     result.append(link)

        return link

    def create_a_skill_summary(self, skill):
        summary = self.wikipediaSearch(skill)
        return summary
    
    def create_a_skill_links(self, skill):
        links = []
        links.append(self.courseraSearch(skill))
        links.append(self.udemySearch(skill))
        links.append(self.pluralsightSearch(skill))
        links.append(self.lyndaSearch(skill))

        
        # result = {
        #     "skill1":
        #     {
        #     "summary": "From Weki",
        #     "links": [
        #         "https://...", "https://...", "https://...", "https://..."
        #     ]
        # }

        # }
             
        return links
    def create_feedback(self):

        dictionary = {

        }
        for skill in self.skills:
            dictionary[skill] = {}
            dictionary[skill]["summary"] = self.create_a_skill_summary(skill)
            dictionary[skill]["links"] = self.create_a_skill_links(skill)
        return dictionary

# p = Parser('machine learning andrew eg')
# print(    p.parseForCoursera())
if __name__ == "__main__":
    # p = Parser("data base")
    # print(p.parse('+'))
    f = FeedBack(["data base", "machine learning"])
    print(f.create_feedback())