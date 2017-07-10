class Solution:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        count = 0
        ranges = []
        for line in grid:
            last_ranges = ranges
            ranges, span = [], []
            flag = True  # have no 1 before
            for index, i in enumerate(line):
                # print '({}, {}), flag: {}'.format(index, i, flag)
                if i == 1:
                    if flag:
                        span = [index, index]
                        flag = False
                    elif not flag:
                        # print "span: {}".format(span)
                        span[1] = index
                    if index == len(line) - 1:
                        ranges.append(span)
                else:
                    if span:
                        ranges.append(span)
                        span = []
                        flag = True
            # add count
            # print last_ranges
            # print ranges
            if last_ranges:
                for r in ranges:
                    f = False
                    for l in last_ranges:
                        belong_island = (r[0] <= l[1] and r[0] >= l[0]) or (r[1] <= l[1] and r[1] >= l[0]) or (l[0] <= r[1] and l[1] >= r[0]) or (l[1] <= r[1] and l[1] >= r[0])
                        if belong_island:
                            f = True
                    if not f:
                        count += 1
            else:
                count += len(ranges)
            print '-----------------------------'
            print last_ranges
            print ranges
            print count
        return count






if __name__ == '__main__':
    m = [
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1]
    ]
    m1=[[1,0,0,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
        [1,0,0,1,1,0,0,1,0,0,0,1,0,1,0,1,0,0,1,0],
        [0,0,0,1,1,1,1,0,1,0,1,1,0,0,0,0,1,0,1,0],
        [0,0,0,1,1,0,0,1,0,0,0,1,1,1,0,0,1,0,0,1],
        [0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0],
        [1,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,1,0,1],
        [0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
        [0,0,0,1,0,1,0,0,1,1,0,1,0,1,1,0,1,1,1,0],
        [0,0,0,0,1,0,0,1,1,0,0,0,0,1,0,0,0,1,0,1],
        [0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,1,0],
        [1,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,1,0,1,0],
        [0,1,0,0,0,1,0,1,0,1,1,0,1,1,1,0,1,1,0,0],
        [1,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1],
        [0,1,0,0,1,1,1,0,0,0,1,1,1,1,1,0,1,0,0,0],
        [0,0,1,1,1,0,0,0,1,1,0,0,0,1,0,1,0,0,0,0],
        [1,0,0,1,0,1,0,0,0,0,1,0,0,0,1,0,1,0,1,1],
        [1,0,1,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0],
        [0,1,1,0,0,0,1,1,1,0,1,0,1,0,1,1,1,1,0,0],
        [0,1,0,0,0,0,1,1,0,0,1,0,1,0,0,1,0,0,1,1],
        [0,0,0,0,0,0,1,1,1,1,0,1,0,0,0,1,1,0,0,0]]
    solution = Solution()
    print solution.numIslands(m1)
