class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        n_list = list(range(1, n+1))
        print(n_list)
        for i in range(n):
            num = n_list[i]
            if num % 3 == 0:
                n_list[i] = "Fizz"
            if num % 5 == 0:
                if n_list[i] == "Fizz":
                    n_list[i] += "Buzz"
                else:
                    n_list[i] = "Buzz"
            if n_list[i] == num:
                n_list[i] = str(num)
        return n_list