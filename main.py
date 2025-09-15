# 在这个文件里编写代码
# 初始体重（单位：kg，可根据实际情况修改）
initial_weight = 60  
# 每年体重增长（单位：kg）
annual_growth = 0.5  
# 月球上的重量是地球上的比例
moon_weight_ratio = 0.165  

print("未来10年地球和月球上的体重变化：")
for year in range(1, 11):
    # 计算地球上的体重
    earth_weight = initial_weight + annual_growth * year  
    # 计算月球上的体重
    moon_weight = earth_weight * moon_weight_ratio  
    print(f"第{year}年：地球上的体重为{earth_weight:.2f}kg，月球上的体重为{moon_weight:.2f}kg")
