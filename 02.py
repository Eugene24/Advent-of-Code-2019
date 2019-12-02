def bruteforce(a, b):
    input = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,5,23,2,10,23,27,2,27,13,31,1,10,31,35,1,35,9,39,2,39,13,43,1,43,5,47,1,47,6,51,2,6,51,55,1,5,55,59,2,9,59,63,2,6,63,67,1,13,67,71,1,9,71,75,2,13,75,79,1,79,10,83,2,83,9,87,1,5,87,91,2,91,6,95,2,13,95,99,1,99,5,103,1,103,2,107,1,107,10,0,99,2,0,14,0"
    input = [int(c) for c in input.split(",")]
    ### Setup req
    input[1] = int(a)
    input[2] = int(b)

    a = 0
    while True:
        ### EXIT
        if input[a] == 99:
            break
        ### '1' COMMAND
        if input[a] == 1:
            input[input[a + 3]] = input[input[a + 1]] + input[input[a + 2]]
            a += 4
            continue
        if input[a] == 2:
            input[input[a + 3]] = input[input[a + 1]] * input[input[a + 2]]
            a += 4
            continue
    return input[0]

for a in range(0, 99):
    for b in range(0, 99):
        val = bruteforce(a, b)
        if val == 19690720:
            print 100 * a + b
            break


