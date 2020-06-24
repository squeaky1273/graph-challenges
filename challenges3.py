from collections import deque

def wordLadderLength(self, beginWord, endWord, wordList):
    """Return the length of the shortest word chain from beginWord to endWord, using words from wordList."""
    length = len(beginWord)

    ladder = []
    queue = deque()

    ladder[beginWord] = ladder
    visited = {beginWord: True}

    while queue:
        current_word, level = queue.popleft()      
        for i in range(length):
            next_word = current_word[:i] + "*" + current_word[i+1:]

            for word in wordList:
                if beginWord == endWord:
                    break

                if word == endWord:
                    return level + 1
                    
                if word not in visited:
                    visited[word] = True
                    queue.append((word, level + 1))
            ladder[next_word] = []
            
    return 0
