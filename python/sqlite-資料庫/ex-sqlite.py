'''

參考網站：
https://www.runoob.com/sqlite/sqlite-tutorial.html

DB Browser for SQLite 下載：
https://sqlitebrowser.org/dl/

'''


# 匯入 sqlite3 模組
import sqlite3

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

'''
PART 1
新增資料庫資料表及其欄位
'''
# 新增資料庫
conn = sqlite3.connect('example.db')

# 建立 cursor 物件
db = conn.cursor()

# 新增資料表及資料表欄位
'''
CREATE TABLE name (field1 type, field2 type, ...)

name：資料表名稱
field：資料欄位名稱
type：資料型態

PRIMARY KEY：將欄位設為主鍵
NOT NULL：欄位不能為空
AUTOINCREMENT：自動增值（使用時需同時將欄位設為主鍵且只能用於整數(integer)資料型態，否則會報錯）
'''
# db.execute("CREATE TABLE contacts (id integer PRIMARY KEY AUTOINCREMENT, date text, name text, number text)")

## 進行資料庫檔案更新
# conn.commit()
## 關閉資料庫
# conn.close()


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

'''
PART 2
新增資料
1. 新增至資料表 (每個欄位皆需賦予值)
2. 新增至資料表內指定欄位
'''

## 1. 新增資料至 contacts 資料表
# db.execute("INSERT INTO contacts VALUES ('2018-03-11','王小寶','1')")
# db.execute("INSERT INTO contacts VALUES (2, '2018-03-15','白采君','3')")
# db.execute("INSERT INTO contacts VALUES (3, '2018-03-12','吳有明','2')")

## 2. 也可以使用下面這種方式

# tdate = '2018-03-11'
# tname = '測試先生'
# for i in range(5):
#     tnumber = input()
#     db.execute("INSERT INTO contacts(date, name, number) values('{}', '{}', '{}');".format(tdate, tname, tnumber))

# # 進行資料庫檔案更新
# conn.commit()
# # 關閉資料庫
# conn.close()

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

'''
PART 3
讀取資料表資料

SELECT {filed1} FROM {table} ORDER BY {filed2} {type}

filed1：選擇資料表欄位 (*代表全部欄位)
table：選擇資料表
filed2：透過哪一個資料欄位進行排序動作
type：預設為升序(可以不用輸入ASC)

ASC：預設為升序排列
DESC：降序排列
'''

# for row in db.execute('SELECT * FROM contacts'):
#     print(row)

## 資料顯示透過 number 排序
# for row in db.execute('SELECT * FROM contacts ORDER BY number'):
#     print(row)

## 資料顯示透過 number 排序
# for row in db.execute('SELECT * FROM contacts ORDER BY number DESC'):
#     print(row)

# for row in db.execute('SELECT NUMBER FROM contacts ORDER BY number DESC'):
#     print(row)

## 關閉資料庫
# conn.close()

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

'''
PART 4
刪除資料表資料
'''
# # 刪除資料表欄位資料 (若欄位值一樣會將相同值的欄位刪除)
'''
DELETE FROM {table} WHERE {filed}="測試先生"

table：要刪除的資料表
filed：刪除指定欄位內包含某值的資料
'''
# db.execute('DELETE FROM contacts WHERE name="測試先生";')

# # 確認資料是否刪除
# for row in db.execute('SELECT * FROM contacts'):
#     print(row)


# # 進行資料庫檔案更新
# conn.commit()
# # 關閉資料庫
# conn.close()

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

'''
PART 5
修改資料表資料
'''

# # 修改資料表欄位資料
'''
UPDATE {table} SET {filed1} = "tt" WHERE {filed2} = 5

table：要修改的資料表
filed1：要修改的資料表欄位
filed2：要從資料表中的哪筆資料欄位進行修改
'''
#db.execute('UPDATE contacts SET NAME = "tt" WHERE ID = 2')
# db.execute('UPDATE contacts SET NAME = "trt" WHERE number = 1')


# # 進行資料庫檔案更新
#conn.commit()
# # 關閉資料庫
# conn.close()