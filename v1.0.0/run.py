# Run-Python module, made by Xty21223
# LISCENCE
# Boost Software License - Version 1.0 - August 17th, 2003

# Permission is hereby granted, free of charge, to any person or organization
# obtaining a copy of the software and accompanying documentation covered by
# this license (the "Software") to use, reproduce, display, distribute,
# execute, and transmit the Software, and to prepare derivative works of the
# Software, and to permit third-parties to whom the Software is furnished to
# do so, all subject to the following:

# The copyright notices in the Software and this entire statement, including
# the above license grant, this restriction and the following disclaimer,
# must be included in all copies of the Software, in whole or in part, and
# all derivative works of the Software, unless such copies or derivative
# works are solely in the form of machine-executable object code generated by
# a source language processor.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE, TITLE AND NON-INFRINGEMENT. IN NO EVENT
# SHALL THE COPYRIGHT HOLDERS OR ANYONE DISTRIBUTING THE SOFTWARE BE LIABLE
# FOR ANY DAMAGES OR OTHER LIABILITY, WHETHER IN CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.


#######################################################################


# THIS IS VERSION:
# Run V1.0.0 ALPHA

def pr(text, end="\n", color="black", raw="no"):
  color = color.lower()
  if color == "black":
    print(text)
  elif color == "red":
    print("\033[91m {}\033[00m" .format(text), end=end)
  elif color == "green":
    print("\033[92m {}\033[00m" .format(text), end=end)
  elif color == "yellow":
    print("\033[93m {}\033[00m" .format(text), end=end)
  elif color == "lightpurple" or color == "lpurple":
    print("\033[94m {}\033[00m" .format(text), end=end)
  elif color == "purple" or color == "juniaccent":
    print("\033[95m {}\033[00m" .format(text), end=end)
  elif color == "cyan" or color == "lightblue":
    print("\033[96m {}\033[00m" .format(text), end=end)
  elif color == "lightgray" or color == "lgray:
    print("\033[97m {}\033[00m" .format(text), end=end)
  else:
    raise NameError("\033[91mThat's not a color!\033[00m")
def pr_list(lst, fancy=True, join=", "):
  if fancy:  
    print(join.join(map(str,lst)))
  else:
    print(lst)
