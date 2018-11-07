import json
import requests
import create_filters

BASEURL = "https://api.stackexchange.com/2.2/"

QUESTIONS_URL_SUFFIX = "questions"
ANSWERS_URL_SUFFIX = "answers"
COMMENTS_URL_SUFFIX = "comments"

def main():
    qFilter = create_filters.createQuestionFilter()
    aFilter = create_filters.createAnswerFilter()
    cFilter = create_filters.createCommentFilter()
    getComments(cFilter)
    #getQuestions(qFilter)
    #getAnswers(aFilter)


# TODO this only gets the first page from stackoverflow
def getQuestions(filter):
    requestParams = {
        "site": "stackoverflow",
        "filter": filter,
        "pagesize": "100",
    }

    questionsRequest = requests.get(BASEURL + QUESTIONS_URL_SUFFIX,
                                    params=requestParams)

    print(questionsRequest.json())

# TODO this only gets the first page from stackoverflow
def getAnswers(filter):
    requestParams = {
        "site": "stackoverflow",
        "filter": filter,
        "pagesize": "100",
    }

    answerRequest = requests.get(BASEURL + ANSWERS_URL_SUFFIX,
                                 params=requestParams)
    print(answerRequest.json())


# TODO this only gets the first page from stackoverflow
def getComments(filter):
    requestParams = {
        "site": "stackoverflow",
        "filter": filter,
        "pagesize": "100",
    }

    commentRequest = requests.get(BASEURL + COMMENTS_URL_SUFFIX,
                                 params=requestParams)
    print(commentRequest.json())


main()
