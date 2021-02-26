#!/bin/python3


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny',
    'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots',
    'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    from collections import deque
    import copy

    if start_word == end_word:
        return [start_word]

    stack = []
    stack.append(start_word)
    queue = deque()
    queue.appendleft(stack)
    word_list = []
    for x in open(dictionary_file).readlines():
        word_list.append(x.strip("\n"))
    while len(queue) != 0:
        top = queue.pop()
        for word in word_list:
            if _adjacent(word, top[-1]):
                C = copy.deepcopy(top)
                C.append(word)
                if word == end_word:
                    for i in range(1, len(C)-2):
                        if _adjacent(top[i-1], top[i+1]):
                            C.pop(i)
                    return(C)
                queue.appendleft(C)
                word_list.remove(word)


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    if ladder == []:
        return False
    for word1, word2 in zip(ladder, ladder[1:]):
        if not _adjacent(word1, word2):
            return False
    return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    if word1 == word2:
        return False
    if len(word1) == len(word2):
        differences = 0
        for n, m in zip(word1, word2):
            if n != m:
                if differences:
                    return False
                differences += 1
        return True
    else:
        return True
