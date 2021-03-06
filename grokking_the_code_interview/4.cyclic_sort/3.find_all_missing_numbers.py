def find_missing_numbers(nums):
  i = 0
  while i < len(nums):
    j = nums[i] - 1
    if nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]  # swap
    else:
      i += 1

  missingNumbers = []

  for i in range(len(nums)):
    if nums[i] != i + 1:
      missingNumbers.append(i + 1)

  return missingNumbers


def main():
  print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
  print(find_missing_numbers([2, 4, 1, 2]))
  print(find_missing_numbers([2, 3, 2, 1]))


main()


def find_missing_numbers(nums):
  missingNumbers = []
  set1=set(nums)
  set2=set()
  for i in range(1,len(nums)+1):
    set2.add(i)

  missingNumbers=list(set2-set1)
  # TODO: Write your code here
  return missingNumbers
