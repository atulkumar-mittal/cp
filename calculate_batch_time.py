def calc_time(b_size, run_time, job_size):
    max_time = 0
    for x in range(len(b_size)):
        mod = job_size[x] % b_size[x]
        # // is floor division operator and provides int value lesser than actual decimal value
        time = (job_size[x]//b_size[x])*run_time[x] if (mod == 0) else ((job_size[x]//b_size[x])+1) * run_time[x]
        max_time = time if time > max_time else max
    return max_time


print(calc_time([4, 5], [3, 4], [8, 8]))
