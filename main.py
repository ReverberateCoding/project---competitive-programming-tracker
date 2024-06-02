from atcoder_problems import atcoder_propagate
from models import question, problem_set

problem_sets = list()
atcoder_propagate(problem_sets=problem_sets)

with open("problemsets.txt", "w", encoding="utf-8") as file:
    for problem_set_item in problem_sets:
        file.writelines(problem_set_item.strlist())
        #for question_item in problem_set_item.question_list:
        #    print('wtf')
        #    file.write(str(question_item)+"\n")