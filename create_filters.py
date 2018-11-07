import json
import requests

import constants

def main():
    filter = createQuestionFilter()
    getQuestions(filter)


def createFilter(includedFieldsList, excludedFieldsList):
    filterParams = {
        'base': 'default',
        'include': ';'.join(includedFieldsList),
        'exclude': ';'.join(excludedFieldsList),
    }

    filterResponse = requests.get(constants.BASEURL +
                                  constants.FILTER_URL_SUFFIX,
                                  filterParams)

    filterJson = json.loads(filterResponse.content)
    filter = filterJson['items'][0]['filter']
    return filter;


def createQuestionFilter():
    includedFields = (
        'question.answers',
        'question.body_markdown',
        'question.comments',
    )

    excludedFields = (
        'question.accepted_answer_id',
        'question.bounty_amount',
        'question.bounty_closes_date',
        'question.closed_reason',
        'question.community_owned_date',
        'question.link',
        'question.locked_date',
        'question.migrated_from',
        'question.migrated_to',
        'question.protected_date',
    )

    return createFilter(includedFields, excludedFields)


def createAnswerFilter():
    includedFields = (
        'answer.body_markdown',
        'answer.comments',
        'answer.tags',
        'answer.title',
    )

    excludedFields = (
        'answer.community_owned_date',
        'answer.can_flag',
        'answer.comment_count',
        'answer.locked_date',
    )

    return createFilter(includedFields, excludedFields)


def createCommentFilter():
    includedFields = (
        'comment.body_markdown',
        'comment.body',
    )

    excludedFields = (
        'comment.edited',
        'comment.reply_to_user',
    )

    return createFilter(includedFields, excludedFields)

