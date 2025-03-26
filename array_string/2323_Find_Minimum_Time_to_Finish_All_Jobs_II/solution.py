class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        # Sort the lists to ensure that the largest jobs are matched with
        # the workers who can work the longest each day.
        jobs.sort()
        workers.sort()

        # Calculate the time taken for each worker to complete their assigned job.
        times = [(job_duration + worker_speed - 1) // worker_speed
                 for job_duration, worker_speed in zip(jobs, workers)]

        # The longest time taken by any job-worker pair determines the total time required.
        return max(times)
