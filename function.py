heavenlyStemList = ["癸", "甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬"]  # 癸 甲 乙 丙
earthlyBranchList = [
    "亥",
    "子",
    "丑",
    "寅",
    "卯",
    "辰",
    "巳",
    "午",
    "未",
    "申",
    "酉",
    "戌",
]  # 亥 子 丑 寅
gong = [
    "命宮",
    "父母宮",
    "福德宮",
    "田宅宮",
    "官祿宮",
    "交友宮",
    "遷移宮",
    "疾厄宮",
    "財帛宮",
    "子女宮",
    "夫妻宮",
    "兄弟宮",
]  # 命宮 父母 福德 田宅

zw = ["紫微", 0, 0, 0, "廉貞", 0, 0, "天同", "武曲", "太陽", 0, "天機"]
tf = ["天府", "太陰", "貪狼", "巨門", "天相", "天梁", "七殺", 0, 0, 0, "破軍", 0]

element_mapping = {
    ("甲", "子"): "海中金",
    ("乙", "丑"): "海中金",
    ("壬", "申"): "劍鋒金",
    ("癸", "酉"): "劍鋒金",
    ("庚", "辰"): "白蠟金",
    ("辛", "巳"): "白蠟金",
    ("甲", "午"): "砂中金",
    ("乙", "未"): "砂中金",
    ("壬", "寅"): "金箔金",
    ("癸", "卯"): "金箔金",
    ("庚", "戌"): "釵釧金",
    ("辛", "亥"): "釵釧金",
    ("壬", "午"): "楊柳木",
    ("癸", "未"): "楊柳木",
    ("戊", "辰"): "大林木",
    ("己", "巳"): "大林木",
    ("庚", "寅"): "松柏木",
    ("辛", "卯"): "松柏木",
    ("戊", "戌"): "平地木",
    ("己", "亥"): "平地木",
    ("壬", "子"): "桑拓木",
    ("癸", "丑"): "桑拓木",
    ("庚", "申"): "石榴木",
    ("辛", "酉"): "石榴木",
    ("丙", "子"): "澗下水",
    ("丁", "丑"): "澗下水",
    ("甲", "申"): "泉中水",
    ("乙", "酉"): "泉中水",
    ("壬", "辰"): "長流水",
    ("癸", "巳"): "長流水",
    ("丙", "午"): "天河水",
    ("丁", "未"): "天河水",
    ("甲", "寅"): "大溪水",
    ("乙", "卯"): "大溪水",
    ("壬", "戌"): "大海水",
    ("癸", "亥"): "大海水",
    ("丙", "寅"): "爐中火",
    ("丁", "卯"): "爐中火",
    ("甲", "戌"): "山頭火",
    ("乙", "亥"): "山頭火",
    ("戊", "子"): "霹靂火",
    ("己", "丑"): "霹靂火",
    ("丙", "申"): "山下火",
    ("丁", "酉"): "山下火",
    ("甲", "辰"): "覆燈火",
    ("乙", "巳"): "覆燈火",
    ("戊", "午"): "天上火",
    ("己", "未"): "天上火",
    ("庚", "午"): "路傍土",
    ("辛", "未"): "路傍土",
    ("戊", "寅"): "城頭土",
    ("己", "卯"): "城頭土",
    ("丙", "戌"): "屋上土",
    ("丁", "亥"): "屋上土",
    ("庚", "子"): "壁上土",
    ("辛", "丑"): "壁上土",
    ("戊", "申"): "大驛土",
    ("己", "酉"): "大驛土",
    ("丙", "辰"): "砂中土",
    ("丁", "巳"): "砂中土",
}


def get_element(x, y):
    return element_mapping.get((x, y), None)


def water(day):
    if day == 22 or day == 23:
        x = 1
    if day == 1 or day == 24 or day == 25:
        x = 2
    if day == 2 or day == 3 or day == 26 or day == 27:
        x = 3
    if day == 4 or day == 5 or day == 28 or day == 29:
        x = 4
    if day == 6 or day == 7 or day == 30:
        x = 5
    if day == 8 or day == 9:
        x = 6
    if day == 10 or day == 11:
        x = 7
    if day == 12 or day == 13:
        x = 8
    if day == 14 or day == 15:
        x = 9
    if day == 16 or day == 17:
        x = 10
    if day == 18 or day == 19:
        x = 11
    if day == 20 or day == 21:
        x = 0
    y = (18 - x) % 12
    return [x, y]


def wood(day):
    if day == 25:
        x = 1

    if day == 2 or day == 28:
        x = 2

    if day == 3 or day == 5:
        x = 3

    if day == 6 or day == 8:
        x = 4

    if day == 1 or day == 9 or day == 11:
        x = 5

    if day == 4 or day == 12 or day == 14:
        x = 6

    if day == 7 or day == 15 or day == 17:
        x = 7

    if day == 10 or day == 18 or day == 20:
        x = 8

    if day == 13 or day == 21 or day == 23:
        x = 9

    if day == 16 or day == 24 or day == 26:
        x = 10

    if day == 19 or day == 27 or day == 29:
        x = 11

    if day == 22 or day == 30:
        x = 0
    y = (18 - x) % 12
    return [x, y]


def gold(day):
    if day == 5:
        x = 1

    if day == 3 or day == 9:
        x = 2

    if day == 4 or day == 7 or day == 13:
        x = 3

    if day == 8 or day == 11 or day == 17:
        x = 4

    if day == 2 or day == 12 or day == 15 or day == 21:
        x = 5

    if day == 6 or day == 16 or day == 19 or day == 25:
        x = 6

    if day == 10 or day == 20 or day == 23 or day == 29:
        x = 7

    if day == 14 or day == 24 or day == 27:
        x = 8

    if day == 18 or day == 28:
        x = 9

    if day == 22:
        x = 10

    if day == 26:
        x = 11

    if day == 1 or day == 30:
        x = 0
    y = (18 - x) % 12
    return [x, y]


def mud(day):
    if day == 7:
        x = 1

    if day == 4 or day == 12:
        x = 2

    if day == 5 or day == 9 or day == 17:
        x = 3

    if day == 10 or day == 14 or day == 22:
        x = 4

    if day == 3 or day == 15 or day == 19 or day == 27:
        x = 5

    if day == 8 or day == 20 or day == 24:
        x = 6

    if day == 1 or day == 13 or day == 25 or day == 29:
        x = 7

    if day == 6 or day == 18 or day == 30:
        x = 8

    if day == 11 or day == 13:
        x = 9

    if day == 16 or day == 28:
        x = 10

    if day == 21:
        x = 11

    if day == 26 or day == 2:
        x = 0
    y = (18 - x) % 12
    return [x, y]


def fire(day):
    if day == 9 or day == 19:
        x = 1

    if day == 5 or day == 15 or day == 25:
        x = 2

    if day == 6 or day == 11 or day == 21:
        x = 3

    if day == 12 or day == 17 or day == 27:
        x = 4

    if day == 4 or day == 18 or day == 23:
        x = 5

    if day == 10 or day == 24 or day == 29:
        x = 6

    if day == 2 or day == 16 or day == 30:
        x = 7

    if day == 8 or day == 22:
        x = 8

    if day == 14 or day == 28:
        x = 9

    if day == 1 or day == 20:
        x = 10

    if day == 7 or day == 26:
        x = 11

    if day == 3 or day == 13:
        x = 0
    y = (18 - x) % 12
    return [x, y]


def createForm(year, month, day, hour):
    house = [
        [0 for _ in range(6)] for _ in range(12)
    ]  # 12個 [天干, 地支, 宮, 身宮與否, 紫微星系, 天府星系]

    house[(1 + month + hour) % 12][3] = "身宮"
    temp = 3 + month - hour
    for i in range(12):
        house[(temp + i) % 12][2] = gong[i]
        house[(3 + i) % 12][0] = heavenlyStemList[
            (((year - 1803) % 5) * 2 + 1 + i) % 10
        ]
        house[i][1] = earthlyBranchList[i]
    ny = get_element(house[(temp) % 12][0], house[(temp) % 12][1])
    if ny[-1] == "水":
        for i in range(12):
            house[(water(day)[0] + i) % 12][4] = zw[i]
            house[(water(day)[1] + i) % 12][5] = tf[i]
    elif ny[-1] == "木":
        for i in range(12):
            house[(wood(day)[0] + i) % 12][4] = zw[i]
            house[(wood(day)[1] + i) % 12][5] = tf[i]
    elif ny[-1] == "金":
        for i in range(12):
            house[(gold(day)[0] + i) % 12][4] = zw[i]
            house[(gold(day)[1] + i) % 12][5] = tf[i]
    elif ny[-1] == "土":
        for i in range(12):
            house[(mud(day)[0] + i) % 12][4] = zw[i]
            house[(mud(day)[1] + i) % 12][5] = tf[i]
    elif ny[-1] == "火":
        for i in range(12):
            house[(fire(day)[0] + i) % 12][4] = zw[i]
            house[(fire(day)[1] + i) % 12][5] = tf[i]

    return htmlrander(house)


def format_value(value):
    # 對每個值進行處理，確保它是字符串，並且過濾掉特殊字符
    return (
        str(value)
        .replace("'", "")
        .replace("[", "")
        .replace(",", "")
        .replace("0", "")
        .replace("]", "")
    )


def htmlrander(house_data):
    # formatted_data = "ooo".join([str(item) for item in house_data if item and item != 0])
    # formatted_data = "ooo".join([str(item) for item in house_data if item is not None and item != 0])
    html_str = """
    <table style="border-collapse: collapse; margin: 0px auto; width: 15rem; padding:0px; text-align: center;">
        <tr>
            <td style="background-color: #f0f0f0; color: #333; padding:10px; font-family: 'Arial', sans-serif; font-size:10px; font-weight: bold;"
                id="house6">{}</td>
            <td style="background-color: #f0f0f0; color: #333; padding:10px; font-family: 'Arial', sans-serif; font-size:10px; font-weight: bold;"
                id="house7">{}</td>
            <td style="background-color: #f0f0f0; color: #333; padding:10px; font-family: 'Arial', sans-serif; font-size:10px; font-weight: bold;"
                id="house8">{}</td>
            <td style="background-color: #f0f0f0; color: #333; padding:10px; font-family: 'Arial', sans-serif; font-size:10px; font-weight: bold;"
                id="house9">{}</td>
        </tr>
        <tr>
            <td style="background-color: #f0f0f0; color: #333; padding:10px; font-family: 'Arial', sans-serif; font-size:10px; font-weight: bold;"
                id="house5">{}</td>
                <td style="color: #333; padding:10px; font-family: 'Arial', sans-serif; font-size:10px; font-weight: bold;"
                id="house5"> </td>
            <td style="color: #333; padding:10px; font-family: 'Arial', sans-serif; font-size:10px; font-weight: bold;"
                id="house10"> </td>
            <td style="background-color: #f0f0f0; color: #333; padding:10px; font-family: 'Arial', sans-serif; font-size:10px; font-weight: bold;"
                id="house10">{}</td>
        </tr>
        <tr>
            <td style="background-color: #f0f0f0; color: #333; padding:10px; font-family: 'Arial', sans-serif; font-size:10px; font-weight: bold;"
                id="house4">{}</td>
                <td style="color: #333; padding:10px; font-family: 'Arial', sans-serif; font-size:10px; font-weight: bold;"
                id="house4"> </td>

            <td style="color: #333; padding:10px; font-family: 'Arial', sans-serif; font-size:10px; font-weight: bold;"
                id="house11"> </td>
            <td style="background-color: #f0f0f0; color: #333; padding:10px; font-family: 'Arial', sans-serif; font-size:10px; font-weight: bold;"
                id="house11">{}</td>
        </tr>
        <tr>
            <td style="background-color: #f0f0f0; color: #333; padding:10px; font-family: 'Arial', sans-serif; font-size:10px; font-weight: bold;"
                id="house3">{}</td>
            <td style="background-color: #f0f0f0; color: #333; padding:10px; font-family: 'Arial', sans-serif; font-size:10px; font-weight: bold;"
                id="house2">{}</td>
            <td style="background-color: #f0f0f0; color: #333; padding:10px; font-family: 'Arial', sans-serif; font-size:10px; font-weight: bold;"
                id="house1">{}</td>
            <td style="background-color: #f0f0f0; color: #333; padding:10px; font-family: 'Arial', sans-serif; font-size:10px; font-weight: bold;"
                id="house0">{}</td>
        </tr>
    </table>
    """.format(
        format_value(house_data[6]),
        format_value(house_data[7]),
        format_value(house_data[8]),
        format_value(house_data[9]),
        format_value(house_data[5]),
        format_value(house_data[10]),
        format_value(house_data[4]),
        format_value(house_data[11]),
        format_value(house_data[3]),
        format_value(house_data[2]),
        format_value(house_data[1]),
        format_value(house_data[0]),
    )

    head = """<div>this is head</div>"""
    html_str = head + html_str

    return html_str


# house_data = createForm(2002, 8, 16, 2)

# # 使用 htmlrander 函數生成 HTML 字串
# html_table = htmlrander(house_data)

# # 在實際應用中，你可以將這個 HTML 字串返回給前端，由前端渲染顯示。
# print(house_data)
# print(html_table)
