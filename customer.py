# C-1. フルネームを取得できるA
"""
ken = Customer(first_name="Ken", family_name="Tanaka")
ken.full_name()  # "Ken Tanaka" という値を返す

tom = Customer(first_name="Tom", family_name="Ford")
tom.full_name()  # "Tom Ford" という値を返す
"""
# C-2. 年齢という概念の追加
"""
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.age  # 15 という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age= 57)
tom.age # 57 という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.age # 73 という値を返す
"""

# C-3. 年齢に応じた適切な入場料(entry_fee)を計算できる
"""
料金の計算ルール
こども料金(20歳未満): 1000円
おとな料金(20歳以上65歳未満): 1500円
シニア料金(65歳以上): 1200円

ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.entry_fee()  # 1000 という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age= 57)
tom.entry_fee() # 1500 という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.entry_fee() # 1200 という値を返す
"""

# C-4. 単一の顧客情報をCSV形式で取得できる
"""
c

tom = Customer(first_name="Tom", family_name="Ford", age= 57)
ken.info_csv()  # "Tom Ford,57,1500" という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.info_csv()  # "Ieyasu Tokugawa,73,1200" という値を返す
"""


class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        self.full_name = f'{self.first_name}{self.family_name}'
        return self.full_name


    def entry_fee(self):
        if self.age < 3:
            return 0
        if 3 < self.age < 20:
            return 1000
        if 20 <= self.age <= 65:
            return 1500
        if 65 < self.age < 75:
            return 1200
        if 75 < self.age:
            return 500

    def info_csv(self):
        list = [self.full_name(), str(self.age), str(self.entry_fee())]

        result = ','.join(list)
        print(result)


ken = Customer(first_name="Ken", family_name="Tanaka", age=2)

print(ken.age)
print(ken.entry_fee())
ken.info_csv()  # "Ken Tanaka,15,1000" という値を返す
