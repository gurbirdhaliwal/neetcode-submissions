class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        check_list = self.timeMap[key]
        greatest = ""
        if len(check_list) == 0:
            return greatest

        left, right = 0, len(check_list) - 1
        while left <= right:
            middle = (left + right) // 2
            timestamp_prev = check_list[middle][1]
            if timestamp < timestamp_prev:
                right = middle - 1
            elif timestamp > timestamp_prev:
                greatest = check_list[middle][0]
                left = middle + 1
            else:
                return check_list[middle][0]
        return greatest
