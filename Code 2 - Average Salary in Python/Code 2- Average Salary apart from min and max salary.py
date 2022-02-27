class Solution:
    def average(self, salary: List[int]) -> float:
        n = len(salary) - 2
        salary.remove(min(salary))
        salary.remove(max(salary))
        return(sum(salary)/n)  
        