

# #https://www.codewars.com/kata/6630da20f925eb3007c5a498

def blow_candles(st):
    final_count = 0

    while st != "0"*len(st):
        st_list = list(st)
        pos_0 = 0

        for i in st_list:
            if i == "0":
                pos_0 += 1

            else:
                break
        
        if (len(st) - pos_0) >= 3:
            st_list[pos_0] = str(max(int(st_list[pos_0]) - 1,0))
            st_list[pos_0 + 1] = str(max(int(st_list[pos_0 + 1]) - 1,0))
            st_list[pos_0 + 2] = str(max(int(st_list[pos_0 + 2]) - 1,0))

        elif (len(st) - pos_0) == 2:
            st_list[pos_0] = str(max(int(st_list[pos_0]) - 1,0))
            st_list[pos_0 + 1] = str(max(int(st_list[pos_0 + 1]) - 1,0))

        elif (len(st) - pos_0) == 1:
            st_list[pos_0] = str(max(int(st_list[pos_0]) - 1,0))

        st = "".join(st_list)
        final_count += 1

    return final_count




print(blow_candles("1321"))
print(blow_candles("0323456"))
print(blow_candles("2113"))


