# python3

def max_pairwise_product(nums):
    nums.sort()
    return nums[n-2] * nums[n-1]


if __name__ == '__main__':
    n = int(input())
    nums = [int(x) for x in input().split()]
    print(max_pairwise_product(nums))