def compress_string(input_string):
    result = ''
    count = 0

    for char in input_string:
        if char == '1':
            count += 1
        else:
            if count > 0:
                result += str(count)
                count = 0
            result += char
    
    if count > 0:
        result += str(count)

    return result

# 测试
input_str = '11k11N11/rN111111/Q1111111/111P1111/1111R111/1111B11K/11111111/11B11111'
output_str = compress_string(input_str)
print(output_str)  # 输出: '2k2N2/rN6/Q7/3P4/4R3/4B2K/8/2B5'
