import time
from multiprocessing import Process

def pi_naive(start, end, step):
    print ("Start: ", str(start))
    print ("End: ", str(end))
    sum = 0.0
    for i in range(start, end):
        x = (i+0.5) * step
        sum = sum + 4.0/(1.0+x*x)
    print(sum)

def create_steps(all_steps, n_procs):

    step_size = all_steps // n_procs
    
    if (all_steps % n_procs):
        remain = all_steps % n_procs

    for i in range(n_procs):
        


if __name__ == "__main__":

    n_procs = 6

    num_steps = 100_000_000 #100.000.000 (10+e8) = 8 seg. (2024)
    sums = 0.0
    step = 1.0/num_steps

    if (num_steps % n_procs):
        real_step = num_steps//n_procs
        resto = num_steps % n_procs
    
    procs = []
    for i in range(n_procs):
        s = int((num_steps/n_procs) * i)
        f = int((num_steps/n_procs) * (i+1))-1
        procs.append(Process(target=pi_naive, args=(s,f,step)))

    tic = time.time() # Tempo Inicial

    for i in range(n_procs):
        procs[i].start()

    for i in range(n_procs):
        procs[i].join()

    toc = time.time() # Tempo Final

    print ("Tempo Pi: %.8f s" %(toc-tic))