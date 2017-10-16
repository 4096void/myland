# 复杂度🌰，大 O 记法
# from https://www.interviewcake.com/article/python/big-o-notation-time-and-space-complexity
# O(1) or constant time 常数复杂度
def print_first_item(list_of_items):
  print list_of_items[0]

 # O(n) or linear time 线性复杂度
def print_all_items(list_of_items):
  for item in list_of_items:
    print item

# O(n^2) or quadratic time 平方阶复杂度
def print_all_possible_ordered_pairs(list_of_items):
  for first_item in list_of_items:
    for second_item in list_of_items:
      print first_item, second_item

# n can be actual inputs or numbers of input items
# 1. 输入作为实际操作的 meat-data，比如：控制循环次数
# 2. 输入作为实际操作的具体对象，比如：处理数组

# O(n)
def say_hi_n_times(n):
  for time in range(n):
    print "hi"

# O(n)
def print_all_items_in_list(the_list):
  for item in the_list:
    print item

# drop constant
# 去掉常数复杂度

# O(2n) -> O(n)
def print_all_items_twice(the_list):
  for item in the_list:
    print item

  # once more, with feeling
  for item in the_list
    print item

# O(1 + n/2 + 100) -> O(n)
def print_first_item_then_first_half_then_say_hi_100_times(the_list):
  print the_list[0]

  middle_index = len(the_list) / 2
  index = 0

  while index < middle_index:
    print the_list[index]
    index += 1

  for time in range(100):
    print "hi"

# drop the less significant terms
# 去掉所有次要的

# O(n + n^2) -> O(n^2)
def print_all_numbers_then_all_pair_sums(list_of_numbers):

  print "these are the numbers:"
  for number in list_of_numbers:
    print number

  print "and these are their sums:"
  for first_number in list_of_numbers:
    for second_number in list_of_numbers:
      print first_number + second_number

# worst case

# worst case: O(n), best case: O(1)
# 最佳／最差情况

def contains(haystack, needle):

  # does the haystack contain the needle?
  for item in haystack:
    if item == needle:
      return True

  return false

# space complexity
# 空间复杂度

# O(1) 只用了一个变量
def say_hi_n_times(n):
  for time in range(n):
    print "hi"

# O(n) hi_list 的规模有时和 n 相关
def list_of_hi_n_times(n):
  hi_list = []
  for time in range(n):
    hi_list.append("hi")

  return hi_list

# O(1) 空间复杂度不考虑输入数据因素
def get_largest_item(list_of_items):
  largest = float('-inf')
  for item in list_of_items:
    if item > largest:
      largest = item

  return largest

# What we engineers cares:
# 1. runtime 运行次数
# 2. space 占用内存
# 3. implementation time
# 4. maintainability, readability
