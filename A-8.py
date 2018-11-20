# A-8 リストを要素に持つリスト

# 以下を出力
# "Name: Kazuma, Age: 35"
# "Name: Tom, Age: 57"
# "Name: Bob, Age: 77"
users_info = [["Kazuma", 35],
              ["Tom", 57],
              ["Bob", 77]]
print(f"Name: {users_info[0][0]}, Age: {users_info[0][1]}")
print(f"Name: {users_info[1][0]}, Age: {users_info[1][1]}")
print(f"Name: {users_info[2][0]}, Age: {users_info[2][1]}")