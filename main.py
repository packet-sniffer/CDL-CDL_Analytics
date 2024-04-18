#!usr/bin/python3
import pandas as pd
from pprint import pprint


#setting pandas options
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


def read_csv_traffic(in_csv):
    csv_df = pd.read_csv(in_csv)
    df_ser = "source_ip.value = " + csv_df["source_ip__value"].astype(str) + " AND " + "dest_ip.value = " + csv_df["dest_ip__value"].astype(str) + " AND "+ "dest_port = " + csv_df["dest_port"].astype(str)#convert into a series or a list with the required items
    df_url = "url" + csv_df["URL"]
    return df_ser


def read_csv_url(in_csv):
    csv_df = pd.read_csv(in_csv)
    df_url = "url" + csv_df["URL"]
    return df_url


def get_dict(in_list):
    out_dict = {}
    for i in in_list:
        out_dict.setdefault(i,0)
        out_dict[i] += 1
    return out_dict


def main():
    print("what function do you want to run\n(a) URL entries\n(b) Source and Destination Traffic")
    input_1 = input()
    try:
        if input_1.capitalize() == "A":
            list1 = read_csv_url('url.csv')#input the name of yout csv file downloaded from SLS
            print(f'total entries in this log table are {len(list1)}')
            print('*'*20)
            dict1 = get_dict(list1)
            sort_tup = sorted(dict1.items(), key=lambda x:x[1], reverse = True)[:10]
            out_df = pd.DataFrame(sort_tup)# if no need to write comment this
            out_df.to_csv('cdl_url_result.csv', index = False, header = False)# Comment if no need to write
            for i in sort_tup:
                print(i)

        if input_1.capitalize() == "B":
            list1 = read_csv_traffic('traffic.csv')#input the name of yout csv file downloaded from SLS
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
                    
    except:
        print("error has occurred try again")


if __name__ == "__main__":
    main()
