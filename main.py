#!usr/bin/python3
import pandas as pd
from pprint import pprint


#setting pandas options
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


def read_csv(in_csv):
    csv_df = pd.read_csv(in_csv)
    df_ser = "source_ip.value = " + csv_df["source_ip__value"].astype(str) + " AND " + "dest_ip.value = " + csv_df["dest_ip__value"].astype(str) + " AND "+ "dest_port = " + csv_df["dest_port"].astype(str)#convert into a series or a list with the required items
    return df_ser


def get_dict(in_list):
    out_dict = {}
    for i in in_list:
        out_dict.setdefault(i,0)
        out_dict[i] += 1
    return out_dict


def main():
    list1 = read_csv('cdl_allow.csv')
    print(f'total entries in this log table are {len(list1)}')
    print('*'*20) 
    dict1 = get_dict(list1)
    # pprint(type(final_res))
    print(f'tuple with max denies is:{max(dict1, key = dict1.get)}')
    print("----")
    sort_tup = sorted(dict1.items(), key=lambda x:x[1], reverse = True)[:10]
    out_df = pd.DataFrame(sort_tup)
    out_df.to_csv('cdl_allow_result.csv', index = False, header = False)
    for i in sort_tup:
        print(i)


if __name__ == "__main__":
    main()
