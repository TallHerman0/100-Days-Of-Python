# letters = []

# def lengthOfLongestSubstring(s: str) -> int:
#         global letters
#         count = 0
#         for letter in s:
#             if letter not in letters:
#                 count += 1
#                 letters.append(letter)
#             else:
#                 count = 0
#                 letters = []
#         return count

# count = lengthOfLongestSubstring(input("Enter a string: "))

# print(count)

from snake import Snake

snake = Snake()

snake.name = "katlego"

print(snake.name)