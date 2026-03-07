def createTwoArr(row, column):
    """正确初始化的方法"""
    arr = [[0] * column for _ in range(row)]    # 注意行列的顺序
    return arr

def createTwoArr_error(row, column):
    """错误初始化的方法"""
    arr = [[0] * column] * row                  # 这种是错误的  这种初始化相当于是每行都相同
    return arr

if __name__ == "__main__":
    error_arr = createTwoArr_error(2, 3)
    print(f"before error_arr: {error_arr}")
    error_arr[0][0] = 1
    error_arr[0][1] = 2
    print(f"after error_arr: {error_arr}")

    print('---' * 10)

    right_arr = createTwoArr(2, 3)
    print(f"before right_arr: {right_arr}")
    right_arr[0][0] = 1
    right_arr[0][1] = 2
    print(f"after right_arr: {right_arr}")
