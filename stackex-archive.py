import json
import requests

import constants
import create_filters

def main():
    qFilter = create_filters.createQuestionFilter()
    aFilter = create_filters.createAnswerFilter()
    cFilter = create_filters.createCommentFilter()
    getQuestions(qFilter)
    print('\n')
    #getAnswers(aFilter)
    print('\n')
    #getComments(cFilter)


# TODO this only gets the first page from stackoverflow
def getQuestions(filter):
    requestParams = {
        'site': 'stackoverflow',
        'filter': filter,
        'pagesize': constants.PAGE_SIZE,
    }

    questionsRequest = requests.get(constants.BASEURL + 
                                    constants.QUESTIONS_URL_SUFFIX,
                                    params=requestParams)

    print(questionsRequest.json())

# TODO this only gets the first page from stackoverflow
def getAnswers(filter):
    requestParams = {
        'site': 'stackoverflow',
        'filter': filter,
        'pagesize': constants.PAGE_SIZE,
    }

    answerRequest = requests.get(constants.BASEURL +
                                 constants.ANSWERS_URL_SUFFIX,
                                 params=requestParams)
    print(answerRequest.json())


# TODO this only gets the first page from stackoverflow
def getComments(filter):
    requestParams = {
        'site': 'stackoverflow',
        'filter': filter,
        'pagesize': constants.PAGE_SIZE,
    }

    commentRequest = requests.get(constants.BASEURL +
                                  constants.COMMENTS_URL_SUFFIX,
                                  params=requestParams)
    print(commentRequest.json())


main()
