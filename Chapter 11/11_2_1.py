# Greedy matching example
# In greedy matching, the regex engine will try to match the longest possible string
# that satisfies the pattern. It will consume as much text as possible.

# Import the regular expression module
import re

# Define a sample string that contains multiple colons
x = 'From: Using the : character'

# Use re.findall() to search for patterns in the string
# 'F.+:' is the pattern where:
# F - matches the literal character 'F'
# .+ - matches one or more of any character (except newline)
# : - matches the literal colon
# The greedy .+ will match as much as possible before the last colon
y = re.findall('F.+:', x)
print(y)  # Output: ['From: Using the :'] - matches everything up to the last colon

print("\n--- Non-greedy matching example ---\n")

# Non-greedy matching example
# In non-greedy matching, the regex engine will try to match the shortest possible string
# that satisfies the pattern. It will consume as little text as possible.

# Import the regular expression module (already imported above, but shown for clarity)
import re

# Use the same sample string
x = 'From: Using the : character'

# Use re.findall() with non-greedy matching
# 'F.+?:' is the pattern where:
# F - matches the literal character 'F'
# .+? - matches one or more of any character (except newline), but does so non-greedily
# : - matches the literal colon
# The non-greedy .+? will match as little as possible before the first colon
y = re.findall('F.+?:', x)
print(y)  # Output: ['From:'] - matches only up to the first colon