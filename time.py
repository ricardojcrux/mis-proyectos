import time

times = []

def timeit():
    input("Press ENTER to start: ")
    start_time = time.time()
    input("Press ENTER to stop: ")
    end_time = time.time()
    the_time = round(end_time - start_time, 2)
    print(str(the_time))
    times.append(the_time)
    main()

def main():
    print ("Do you want to...")
    print ("1. Time your solving")
    print ("2. See your solvings")
    dothis = input(":: ")
    if dothis == "1":
        timeit()
    elif dothis == "2":
        sorte_times = times.sort()
        sorted_times = sorte_times.reverse()
        for curr_time in sorted_times:
            print("%d - %f" % ((sorted_times.index(curr_time)+1), curr_time))
    else:
        print ("WTF? Please enter a valid number...")
        main()

main()