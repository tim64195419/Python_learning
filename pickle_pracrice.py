# pickle 是一個緩存的方式可以寫入data,一段時間後再呼叫出來直接使用。
import pickle

data = {'foo': [1, 2, 3],
        'bar': ('Hello', 'wewewerld!'),
        'baz': True}
# 新建一個data.pkl 並且存入data
jar = open('data.pkl', 'wb')
pickle.dump(data, jar) # write the pickled data to the file jar
jar.close()

# 打開data.pkl file 並且載入file data
pkl_file = open('data.pkl', 'rb') # connect to the pickled data
data = pickle.load(pkl_file) # load it into a variable
print(data)
pkl_file.close()