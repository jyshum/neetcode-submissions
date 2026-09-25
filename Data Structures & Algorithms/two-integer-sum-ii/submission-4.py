class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # find the two indices that values add up to target, then return a list of those by appending
        # [i+1, j+2]

        # use a hash set to see if the value we're looking for each value that will equal to target is in the hash set
        # the problem is how do we make it so we return the index of the missingValue when the missingValue is the same of the value: "numbers.index()" returns the index of the first character's index.


        values = set(numbers)
        outputElseCase = []

        for value in numbers:
            missingValue = target-value
            if missingValue in values and value != missingValue:
                return [numbers.index(value)+1, numbers.index(missingValue)+1]
            elif missingValue in values and value == missingValue:
                outputElseCase.append(numbers.index(value)+1)
                numbers.remove(value)
                outputElseCase.append(numbers.index(value)+2)

        return outputElseCase
                


        

        