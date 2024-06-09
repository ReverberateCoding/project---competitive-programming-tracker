import json

class question:
    def __init__(self, question_name, question_link, question_difficulty, question_judge, question_solved, question_id, question_tags):
        self.question_name = question_name
        self.question_link = question_link
        self.question_difficulty = question_difficulty
        self.question_judge = question_judge
        self.question_solved = question_solved
        self.question_id = question_id
        self.question_tags = question_tags
    def append(self, item):
        self.question_tags.append(item)
    def __repr__(self):
        return f"{self.question_name}{self.question_link}{self.question_difficulty}{self.question_judge}{self.question_solved}{self.question_id}{self.question_tags}"
    def __str__(self):
        return f"{self.question_name}{self.question_link}{self.question_difficulty}{self.question_judge}{self.question_solved}{self.question_id}{self.question_tags}"
    def displayTags(self):
        print(str(self.question_tags))
class problem_set:
    def __init__(self, contest_element, question_elements, judge):

        self.problem_set_name = None
        self.problem_set_link = None
        self.problem_set_judge = judge

        self.contest_element = contest_element
        self.question_elements = list()
        for question_element in question_elements:
            self.question_elements.append(question_element)
        
        self.question_list = list()

        if judge == "AtCoder":
            for contest_element_child in contest_element.children:
                if contest_element_child.name == "a":
                    self.problem_set_name = str(contest_element_child.text)
                    self.problem_set_link = str(contest_element_child.get("href"))

            for question_element in self.question_elements:
                question_name = None
                question_link = None
                question_difficulty = None 
                question_judge = "AtCoder"
                question_solved = None
                question_id = None
                question_tags = list()

                tag_attribute = question_element.name
                #print(f"Debug: Accessing question tagname: {str(tag_attribute)}")
                class_attribute = question_element.get("class")
                #print(f"Debug: Accessing question class: {str(class_attribute)}")

                if "table-problem-empty" in class_attribute:
                    continue

                if "table-success" in class_attribute:
                    question_solved = True
                    print(f"Question found solved while processing as question class, question is {question_element.text}")
                else:
                    question_solved = False
                
                for question_element_child in question_element.children:
                    if question_element_child.name == "a":
                        question_name = str(question_element_child.text)
                        question_link = str(question_element_child.get("href"))
                    if question_element_child.name == "div":
                        question_difficulty = str(question_element_child.text)
                
                question_id = question_link.split("/")[-1]

                with open("static/atcoder_tags.json") as file:
                    atcoder_categories = json.load(file)
                    for atcoder_category, atcoder_subcategories in atcoder_categories.items():
                        for atcoder_subcategory, question_ids in atcoder_subcategories.items():
                            if question_id in question_ids:
                                question_tags.append(f"{atcoder_category}_{atcoder_subcategory}")

                self.question_list.append(question(question_name=question_name, question_link=question_link, question_difficulty=question_difficulty, question_judge=question_judge, question_solved=question_solved, question_id=question_id, question_tags=question_tags))
    def __repr__(self):
        ret = "\n".join(map(str, self.question_list))
        ret = f"Contest Information: {self.problem_set_name}{self.problem_set_link}{self.problem_set_judge}\n" + ret + "\n"
        return ret
    def __str__(self):
        ret = "\n".join(map(str, self.question_list))
        ret = f"Contest Information: {self.problem_set_name}{self.problem_set_link}{self.problem_set_judge}\n" + ret + "\n"
        return ret
    def returnStringList(self):
        ret = list()
        ret.append(f"Contest Information: {self.problem_set_name}{self.problem_set_link}{self.problem_set_judge}\n")
        for i in self.question_list:
            ret.append(str(i)+"\n")
        return ret