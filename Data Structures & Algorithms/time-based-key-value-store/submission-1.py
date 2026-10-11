class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            # key hasnt been set before, create the new values
            self.store[key] = [[timestamp, value]]
        else:
            # key has been set before, add to the existing values
            self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            # set was never made with this key, return ""
            return ""
        else:
            # set was made with this key before, return value of highest timestamp
            pairs = self.store[key] # list of lists that has a value and timestamp
            top = len(pairs) - 1 # last list of value and timestamp
            bottom = 0
            result = ""

            while top >= bottom:
                middle = (top+bottom) // 2 # checking the middle pair 
                if pairs[middle][0] <= timestamp:
                    # if time stamp of the middle pair <= given get. timestamp
                    result = pairs[middle][1] # save it
                    bottom = middle + 1 # move it up, to find g
                else: 
                    top = middle -1

            return result

