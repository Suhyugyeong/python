def search_num(n_list, m_list):
    for i in m_list:
        print(int(i in n_list))

def get_num_list():
    int(input())
    return [int(i) for i in input().split()]

n_list = get_num_list()
m_list = get_num_list()
search_num(n_list, m_list)