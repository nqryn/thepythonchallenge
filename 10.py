# len(a[30]) = ?
# a = [1, 11, 21, 1211, 111221, 

a = ['1', ]
cnt = 0

def get_next_nr(nr_str):
    curr_cnt = 1
    final_str = ''
    for idx in range(1, len(nr_str)):
        if nr_str[idx] == nr_str[idx-1]:
            curr_cnt += 1
        else:
            final_str += str(curr_cnt) + nr_str[idx-1]
            curr_cnt = 1
    # import pdb; pdb.set_trace()
    final_str += str(curr_cnt) + nr_str[-1]
    return final_str

while cnt < 31:
    nr = get_next_nr(a[cnt])
    a.append(nr)
    cnt += 1

print len(a[30])