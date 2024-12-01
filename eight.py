class Solution:
    def jobScheduling(self, startTime, endTime, profit):

        n = len(startTime)
        jobs = [[startTime[i], endTime[i], profit[i]] for i in range(n)]
        jobs.sort(key=lambda x: (x[1], x[0]))  # Sort jobs by end time

        dp = [0] * n  # Initialize dp array
        dp[0] = jobs[0][2]

        for i in range(1, n):  # Loop through jobs

            dp[i] = dp[i - 1]
            prev = 0
            l, r = 0, i - 1

            while l <= r:  # Binary search for non-overlapping job
                mid = (l + r) // 2 
                if jobs[mid][1] <= jobs[i][0]:  # Non-overlapping job found
                    prev = dp[mid]  # Update previous profit
                    l = mid + 1
                else:
                    r = mid - 1

            dp[i] = max(dp[i], jobs[i][2] + prev)

        return dp[n - 1]

solution = Solution()
startTime = [1, 2, 3, 3]
endTime = [3, 4, 5, 6]
profit = [50, 10, 40, 70]
result = solution.jobScheduling(startTime, endTime, profit)
print(result)  